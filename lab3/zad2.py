from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import numpy as np
import pandas as pd

iris = load_iris()
X = iris.data        
y = iris.target     
target_names = iris.target_names  

mapping = {i: name for i, name in enumerate(target_names)}
#print("Mapowanie etykiet numerycznych na nazwy klas:")
#print(mapping)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=0.7, random_state=285711, stratify=y
)

scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

topologie = {
    "MLP_1": (2,),       # jedna warstwa z 2 neuronami
    "MLP_2": (3,),       # jedna warstwa z 3 neuronami
    "MLP_3": (3, 3),     # dwie warstwy: 3 i 3 neurony
}

wyniki = []
for nazwa, struktura in topologie.items():
    model = MLPClassifier(hidden_layer_sizes=struktura,
                          max_iter=1000, random_state=285711)
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    
    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    wyniki.append((nazwa, acc, cm))

for nazwa, acc, cm in wyniki:
    print(f"{nazwa}: dokładność: {acc*100:.2f}%")
    print("Macierz błędów:")
    print(pd.DataFrame(cm, 
                       index=[f"Prawdziwa {n}" for n in target_names],
                       columns=[f"Przewidziana {n}" for n in target_names]))
    print()