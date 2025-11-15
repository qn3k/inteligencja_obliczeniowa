from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import numpy as np
import pandas as pd

iris = load_iris()
X = iris.data
y = iris.target.reshape(-1, 1)
target_names = iris.target_names

#one-hot encoding
enc = OneHotEncoder(sparse_output=False)
y_onehot = enc.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y_onehot, train_size=0.7, random_state=285711, stratify=y
)

scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

topologie = {
    "MLP_1": (2,),
    "MLP_2": (3,),
    "MLP_3": (3, 3)
}

wyniki = []
for nazwa, struktura in topologie.items():
    
    model = MLPClassifier(hidden_layer_sizes=struktura,
                          max_iter=2000,
                          random_state=285711,
                          activation='relu')
    
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)

    #zamiana one-hot na etykiety
    y_pred_labels = np.argmax(y_pred, axis=1)
    y_test_labels = np.argmax(y_test, axis=1)

    acc = accuracy_score(y_test_labels, y_pred_labels)
    cm = confusion_matrix(y_test_labels, y_pred_labels)

    wyniki.append((nazwa, acc, cm))

for nazwa, acc, cm in wyniki:
    print(f"{nazwa}: dokładność: {acc*100:.2f}%")
    print("Macierz błędów:")
    print(pd.DataFrame(
        cm,
        index=[f"Prawdziwa {n}" for n in target_names],
        columns=[f"Przewidziana {n}" for n in target_names]
    ))
    print()
