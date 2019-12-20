import pandas
import random
import sys
data_csv=pandas.read_csv("ANDGate.csv")
data=data_csv.values.tolist()
weight=[]
prediction=[]
activation=[]
def predict(row, weights):
	activation = weights[0]
	for i in range(1,len(row)-1):
		activation += weights[i] * row[i]
	return 1.0 if activation >= 0.0 else 0.0
def errorSolving(error,weights,row):
    for i in range (len(weights)):
        weight[i]=weight[i]+0.2*(error)*row[i]
    return weights
for j in range(0,len(data_csv.columns)-1):
    ran=random.uniform(0,1)
    print(ran)
    weight.append(ran)
for i in range(0,len(data)):
    value=predict(data[i],weight)
    actualOutput=data[i][len(data_csv.columns)-1]
    error=value-actualOutput
    weight=errorSolving(error,weight,data[i])
    print(weight)
     
sum = 1*weight[1] + 1*weight[2]
print(sum)