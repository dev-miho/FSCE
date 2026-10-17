
import torch
import torch.nn as nn
import pandas as pd
import numpy as np 
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from torch.utils.data import Dataset,DataLoader
from torch.optim import AdamW
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay

# 1. Device & Seeds
device = "cuda" if torch.cuda.is_available() else "cpu"
torch.manual_seed(42)
np.random.seed(42)

# 2. Data Loading & Preprocessing
data  = pd.read_csv('industrial_pump_telemetry_dataset.csv').dropna()

X = data.drop(columns="machine_status").values
Y = data["machine_status"].values

# Encode labels to 0, 1, 2, ... (handles strings or numbers)
encoder = LabelEncoder()
Y = encoder.fit_transform(Y)
num_classes = len(encoder.classes_)
feature_names = [col for col in data.columns if col != "machine_status"]

# Split data: Train (70%), Val (15%), Test (15%) with stratification
X_train,X_temp,Y_train,Y_temp = train_test_split(X,Y,test_size=0.3,stratify=Y,random_state=42)
X_val,X_test,Y_val,Y_test = train_test_split(X_temp,Y_temp,test_size=0.5,stratify=Y_temp,random_state=42)

# Feature Scaling (Fit only on train to prevent leakage)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)
X_test = scaler.transform(X_test)

# 3. Dataset (Targets must be torch.long for CrossEntropyLoss)

class IndustrialPumpTelemetryDataset(Dataset):
    def __init__(self,X,Y):
        self.X = torch.tensor(X,dtype=torch.float32)
        self.Y = torch.tensor(Y,dtype=torch.long)

    def __len__(self):
        return len(self.X)

    def __getitem__(self, index):
        return self.X[index],self.Y[index]

train_loader = DataLoader(IndustrialPumpTelemetryDataset(X_train,Y_train,),batch_size=64,shuffle=True)
validation_loader = DataLoader(IndustrialPumpTelemetryDataset(X_val,Y_val,),batch_size=64,shuffle=False)
test_loader = DataLoader(IndustrialPumpTelemetryDataset(X_test,Y_test,),batch_size=64,shuffle=False)

class IndustrialPumpTelemetryModel(nn.Module):
    def __init__(self, in_features,num_classes):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(in_features, 256),
            nn.BatchNorm1d(256),
            nn.GELU(),
            nn.Dropout(0.15),
            
            nn.Linear(256, 128),
            nn.BatchNorm1d(128),
            nn.GELU(),
            nn.Dropout(0.15),
            
            nn.Linear(128, 64),
            nn.BatchNorm1d(64),
            nn.GELU(),
            
            nn.Linear(64, num_classes)
        )
    def forward(self,x):
        return self.network(x)

model = IndustrialPumpTelemetryModel(len(feature_names),num_classes).to(device)
criterion = nn.CrossEntropyLoss()
optimizer = AdamW(model.parameters(),lr=0.001,weight_decay=1e-3)

EPOCHS = 50
history = {"train_loss": [], "val_loss": [], "val_acc": []}
best_val_loss = float("inf")

for epoch in range(EPOCHS):
    model.train()
    train_loss = 0.0
    for X_batch,Y_batch in train_loader:
        X_batch,Y_batch = X_batch.to(device),Y_batch.to(device)
        optimizer.zero_grad()
        prediction = model(X_batch)
        loss = criterion(prediction,Y_batch)
        loss.backward()
        optimizer.step()
        train_loss += loss.item()
    model.eval()
    val_loss = 0.0
    correct = 0
    with torch.inference_mode():
        for X_val_batch, y_val_batch in validation_loader:
            X_val_batch, y_val_batch = X_val_batch.to(device), y_val_batch.to(device)

            val_logits = model(X_val_batch)
            loss = criterion(val_logits, y_val_batch)
            val_loss += loss.item()
            preds = torch.argmax(val_logits,dim=1)
            correct += (preds == y_val_batch).sum().item()
    avg_train_loss = train_loss / len(train_loader)
    avg_val_loss = val_loss / len(validation_loader)
    val_acc = correct / len(validation_loader.dataset)

    history["train_loss"].append(avg_train_loss)
    history["val_loss"].append(avg_val_loss)
    history["val_acc"].append(val_acc)
    if avg_val_loss < best_val_loss:
        best_val_loss = avg_val_loss
        torch.save(model.state_dict(), "best_pump_telemetry_model.pt")
    if (epoch + 1) % 10 == 0 or epoch == 0:
        print(f"Epoch {epoch+1:03d}/{EPOCHS} | Train Loss: {avg_train_loss:.4f} | Val Loss: {avg_val_loss:.4f} | Val Acc: {val_acc*100:.2f}%")
epochs_range = range(1, EPOCHS + 1)
plt.figure(figsize=(14, 5))
# График 1: Training vs Validation Loss
plt.subplot(1, 2, 1)
plt.plot(epochs_range, history["train_loss"], label="Train Loss", color="royalblue", linewidth=2)
plt.plot(epochs_range, history["val_loss"], label="Val Loss", color="darkorange", linestyle="--", linewidth=2)
plt.title("Training & Validation Loss", fontsize=14)
plt.xlabel("Epoch", fontsize=12)
plt.ylabel("Loss", fontsize=12)
plt.legend()
plt.grid(True, linestyle=":", alpha=0.6)
# График 2: Validation Accuracy
plt.subplot(1, 2, 2)
# Ги множиме со 100 за да бидат во проценти (%)
plt.plot(epochs_range, [acc * 100 for acc in history["val_acc"]], label="Val Accuracy", color="seagreen", linewidth=2)
plt.title("Validation Accuracy", fontsize=14)
plt.xlabel("Epoch", fontsize=12)
plt.ylabel("Accuracy (%)", fontsize=12)
plt.legend()
plt.grid(True, linestyle=":", alpha=0.6)
plt.tight_layout()
plt.show()


model.load_state_dict(torch.load("best_pump_telemetry_model.pt"))
test_loss = 0.0
correct = 0

all_preds = []
all_targets = []
with torch.inference_mode():
    for X_test_batch, y_test_batch in test_loader:
        X_test_batch, y_test_batch = X_test_batch.to(device), y_test_batch.to(device)

        test_logits = model(X_test_batch)
        loss = criterion(test_logits,y_test_batch)
        test_loss +=loss.item()
        preds = torch.argmax(test_logits,dim=1)
        all_preds.extend(preds.cpu().numpy())
        all_targets.extend(y_test_batch.cpu().numpy())

        correct += (preds == y_test_batch).sum().item()
avg_test_loss = test_loss/len(test_loader)
test_accuracy = correct/len(test_loader.dataset)
print(f" Test Loss: {avg_test_loss:.4f} | Test Acc: {test_accuracy*100:.2f}%")

print("\nClassification Report:")
print(classification_report(all_targets, all_preds, target_names=[str(c) for c in encoder.classes_]))

cm = confusion_matrix(all_targets, all_preds)
fig, ax = plt.subplots(figsize=(7, 6))
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=encoder.classes_)
disp.plot(ax=ax, cmap=plt.cm.Blues, values_format="d")
plt.title("Test Set Confusion Matrix", fontsize=14)
plt.grid(False)
plt.show()
