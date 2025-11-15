import pandas as pd
from sklearn.model_selection import train_test_split
import math

df = pd.read_csv("siatkowka.csv")

train_set, test_set = train_test_split(df, train_size=0.8, random_state=285711)

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def forwardPass(wiek, waga, wzrost):
    hidden1 = (-0.46122 * wiek) + (0.97314 * waga) + (-0.38203 * wzrost) + 0.80109
    hidden1_act = sigmoid(hidden1)

    hidden2 = (0.78548 * wiek) + (2.16684 * waga) + (0.57847 * wzrost) + 0.43259
    hidden2_act = sigmoid(hidden2)

    output = (-0.81546 * hidden1_act) + (1.0375 * hidden2_act) + (-0.22368)

    return output

# Testowanie
good_predictions = 0
total = len(test_set)

for i in range(total):
    wiek = test_set.iloc[i, 0]
    waga = test_set.iloc[i, 1]
    wzrost = test_set.iloc[i, 2]
    prawdziwa_etykieta = test_set.iloc[i, 3]
    
    wynik = forwardPass(wiek, waga, wzrost)
    przewidziana_etykieta = 1 if wynik > 0.5 else 0 
    
    if przewidziana_etykieta == prawdziwa_etykieta:
        good_predictions += 1

print("Poprawne przewidywania:", good_predictions)
print("Dokładność:", round(good_predictions / total * 100, 2), "%")
