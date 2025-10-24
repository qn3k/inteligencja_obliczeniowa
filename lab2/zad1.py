import pandas as pd
from sklearn.model_selection import train_test_split   

df = pd.read_csv("iris.csv")

#print(df)

(train_set, test_set) = train_test_split(df.values, train_size = 0.7, random_state=11)

#print(train_set)
#print(test_set.shape[0])

def classify_iris(sl, sw, pl, pw):
    if (sl>2.6 and sw>2.2 and pl<2 and pw<0.7):
        return("Setosa")
    elif (sl>5.5 and sw<4 and pl>2 and pw>1):
        return("Virginica")
    else:
        return("Versicolor")

good_predictions = 0 
len = test_set.shape[0]

for i in range(len):
    if classify_iris(test_set[i][0], test_set[i][1], test_set[i][2], test_set[i][3]) == test_set[i][4]:
        good_predictions = good_predictions + 1

print(good_predictions)
print(good_predictions/len*100, "%")