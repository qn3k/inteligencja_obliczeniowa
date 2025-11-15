import pandas as pd
from sklearn.model_selection import train_test_split
df = pd.read_csv("iris.crv")

(train_set, test_set) = train_test_split(df.values, train_size = 0.7, random_state=285711)

