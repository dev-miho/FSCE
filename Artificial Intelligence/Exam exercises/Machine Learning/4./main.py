import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'

from dataset_script_anomaly import dataset
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
import warnings

warnings.filterwarnings("ignore")


if __name__ == '__main__':
    
    C=int(input())
    N=int(input())
    S=int(input())

    data=[]

    for row in dataset:
        new_row = row.copy()
        new_row[-1] = 1 if new_row[-1] > 50 else 0
        
        data.append(new_row)


    split=int(len(data)*0.7)

    train_set=data[:split]
    test_set=data[split:]

    train_x=[row[:-1] for row in train_set]
    train_y=[row[-1] for row in train_set]

    test_x=[row[:-1] for row in test_set]
    test_y=[row[-1] for row in test_set]

    model=MLPClassifier(hidden_layer_sizes=(50,),activation="relu",learning_rate_init=0.001,max_iter=25,random_state=0)
    model.fit(train_x,train_y)
    
    original_accuracy=model.score(test_x,test_y)

    

    scaler=StandardScaler()

    s_train_x=scaler.fit_transform(train_x)
    s_test_x=scaler.transform(test_x)

    model.fit(s_train_x,train_y)
    
    scaled_accuracy=model.score(s_test_x,test_y)

    
    ##################################################################################################

    ids=[3,4,5]
    r_train_x=[]
    for row in train_x:
        new_row=[]
        for index,element in enumerate(row):
            if index not in ids:
                new_row.append(element)
            elif index == ids[0]:
                new_row.append(element if element <= C else C)
            elif index == ids[1]:
                new_row.append(element if element <= N else N)
            elif index == ids[2]:
                new_row.append(element if element<=S else S)
        r_train_x.append(new_row)
    
    r_test_x=[]
    for row in test_x:
        new_row=[]
        for index,element in enumerate(row):
            if index not in ids:
                new_row.append(element)
            elif index == ids[0]:
                new_row.append(element if element <= C else C)
            elif index == ids[1]:
                new_row.append(element if element <= N else N)
            elif index == ids[2]:
                new_row.append(element if element<=S else S)
        r_test_x.append(new_row)
    
    model.fit(r_train_x,train_y)
    
    removed_accuracy = model.score(r_test_x,test_y)


    rs_train_x=scaler.fit_transform(r_train_x)
    rs_test_x=scaler.transform(r_test_x)

    model.fit(rs_train_x,train_y)
    
    removed_scaled_accuracy=model.score(rs_test_x,test_y)

    print(f"Accuracy with: \n"
          f"The original dataset: {original_accuracy} \n"
          f"Removed anomalies: {removed_accuracy} \n"
          f"Scaled attributes: {scaled_accuracy} \n"
          f"Removed anomalies and scaled attributes: {removed_scaled_accuracy} \n")

          

    
    


