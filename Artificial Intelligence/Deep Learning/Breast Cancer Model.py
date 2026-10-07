import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from torch.optim import AdamW
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report

device = "cuda" if torch.cuda.is_available() else "cpu"

data = pd.read_csv("patient_clinical_risk_5000.csv")
print(data.head())

X = data.drop(columns="target").values
Y = data["target"].values

feature_names = [ col for col in data.columns if col !="target"]

X_train,X_temp,Y_train,Y_temp = train_test_split(
    X, Y,
    test_size=0.3,
    random_state=42,
    stratify=Y
)

X_val, X_test, Y_val, Y_test = train_test_split(
    X_temp, Y_temp,
    test_size=0.5,
    random_state=42,
    stratify=Y_temp
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)
X_test = scaler.transform(X_test)

class ClinicalRiskDataset(Dataset):
    def __init__(self,X,Y):
        super().__init__()
        self.X = torch.tensor(X,dtype=torch.float32).to(device)
        self.Y = torch.tensor(Y,dtype=torch.float32).to(device)

    def __len__(self):
        return len(self.X)

    def __getitem__(self, index):
        return self.X[index],self.Y[index]


train_dataloader = DataLoader(dataset=ClinicalRiskDataset(X_train,Y_train),batch_size=64,shuffle=True)

validaton_dataloader = DataLoader(dataset=ClinicalRiskDataset(X_val,Y_val),batch_size=64,shuffle=False)

test_dataloader = DataLoader(dataset=ClinicalRiskDataset(X_test,Y_test),batch_size=64,shuffle=False)

class ClinicalRiskModel(nn.Module):
    def __init__(self, input_dim):
        super().__init__()

        self.network = nn.Sequential(
            nn.Linear(in_features=input_dim,out_features=64),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(in_features=64,out_features=32),
            nn.BatchNorm1d(32),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(in_features=32,out_features=1),
        
        )
    def forward(self,x):
        return self.network(x)

model = ClinicalRiskModel(input_dim=len(feature_names )).to(device)

criterion = nn.BCEWithLogitsLoss()

optimizer = AdamW(model.parameters(), lr=0.001, weight_decay=1e-2)
history = {"train_loss": [], "val_loss": [], "val_acc": []}
EPOCHS = 10
for epoch in range(EPOCHS):
    model.train()
    train_loss=0.0
    for X_train_batch,Y_train_batch in train_dataloader:
        X_train_batch,Y_train_batch=X_train_batch.to(device),Y_train_batch.unsqueeze(1).to(device)
        optimizer.zero_grad()
        predictions = model(X_train_batch)

        loss = criterion(predictions,Y_train_batch)

        loss.backward()

        optimizer.step()

        train_loss += loss.item()
    model.eval()
    val_loss = 0.0
    correct = 0
    with torch.inference_mode():
        for X_val_batch,Y_val_batch in validaton_dataloader:
            X_val_batch,Y_val_batch=X_val_batch.to(device),Y_val_batch.unsqueeze(1).to(device)

            val_logits = model(X_val_batch)

            loss = criterion(val_logits,Y_val_batch)

            preds = (torch.sigmoid(val_logits) > 0.5).float()
            val_loss += loss.item()
            correct  +=(preds == Y_val_batch).sum().item()
    avg_train_loss = train_loss / len(train_dataloader)
    avg_val_loss = val_loss / len(validaton_dataloader)
    val_acc = correct / len(validaton_dataloader.dataset)
    history["train_loss"].append(avg_train_loss)
    history["val_loss"].append(avg_val_loss)
    history["val_acc"].append(val_acc)
    if (epoch + 1) % 10 == 0 or epoch == 0:
        print(f"Epoch {epoch+1:03d}/{EPOCHS} | Train Loss: {avg_train_loss:.4f} | Val Loss: {avg_val_loss:.4f} | Val Acc: {val_acc*100:.2f}%")
# 6. Final Evaluation on Test Set

model.eval()
test_loss = 0.0
all_preds = []
all_targets = []

with torch.inference_mode():
    for X_test_batch, Y_test_batch in test_dataloader:
        X_test_batch = X_test_batch.to(device)
        Y_test_batch = Y_test_batch.unsqueeze(1).to(device)

        test_logits = model(X_test_batch)
        loss = criterion(test_logits, Y_test_batch)
        test_loss += loss.item()

        # Convert logits to binary predictions (0 or 1)
        preds = (torch.sigmoid(test_logits) > 0.5).float()

        # Move to CPU / NumPy for scikit-learn metrics
        all_preds.extend(preds.cpu().numpy())
        all_targets.extend(Y_test_batch.cpu().numpy())

avg_test_loss = test_loss / len(test_dataloader)
all_preds = np.array(all_preds).flatten()
all_targets = np.array(all_targets).flatten()


test_accuracy = (all_preds == all_targets).mean() * 100

print(f"\n--- FINAL TEST RESULTS ---")
print(f"Test Loss: {avg_test_loss:.4f} | Test Acc: {test_accuracy:.2f}%")
print("\nClassification Report:")
print(classification_report(all_targets, all_preds, target_names=["Stable (0)", "Readmitted (1)"]))







