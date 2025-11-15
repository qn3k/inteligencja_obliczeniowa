import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt

df = pd.read_csv("diabetes.csv")

df["class"] = df["class"].map({
    "tested_negative": 0,
    "tested_positive": 1
})

cols_with_zero = [
    "glucose-concentr",
    "blood-pressure",
    "skin-thickness",
    "insulin",
    "mass-index"
]

for col in cols_with_zero:
    df[col] = df[col].replace(0, np.nan)
    df[col] = df[col].fillna(df[col].median())

X = df.drop("class", axis=1)
y = df["class"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, train_size=0.7, random_state=42, stratify=y
)

classifiers = {
    "Drzewo decyzyjne": DecisionTreeClassifier(random_state=42),
    "kNN (5)": KNeighborsClassifier(n_neighbors=5),
    "Naive Bayes": GaussianNB(),
    "MLP (5)": MLPClassifier(hidden_layer_sizes=(5,), max_iter=1500, random_state=42),
    "MLP (10,5)": MLPClassifier(hidden_layer_sizes=(10,5), max_iter=1500, random_state=42),
    "MLP (20,10,5)": MLPClassifier(hidden_layer_sizes=(20,10,5), max_iter=1500, random_state=42),
}

accuracies = {}
conf_matrices = {}

for name, model in classifiers.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    accuracies[name] = acc
    conf_matrices[name] = cm

#wykresik
plt.bar(accuracies.keys(), accuracies.values())
plt.xticks(rotation=45, ha="right")
plt.ylabel("Accuracy")
plt.title("Porównanie klasyfikatorów (diagnosis diabetes)")
plt.show()

#macierz bledow
for name, cm in conf_matrices.items():
    print(f"\n=== {name} ===")
    print("Accuracy:", round(accuracies[name]*100, 2), "%")
    print("Macierz błędów:")
    print(pd.DataFrame(
        cm,
        index=["Prawdziwe 0 (negatyw)", "Prawdziwe 1 (pozytyw)"],
        columns=["Przewidziane 0", "Przewidziane 1"]
    ))
    tn, fp, fn, tp = cm.ravel()
    print("\n=== ", name, " ===")
    print("FP =", fp)
    print("FN =", fn, "<-- najpoważniejszy błąd")

