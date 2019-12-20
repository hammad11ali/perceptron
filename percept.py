import pandas
import random
data_csv=pandas.read_csv("ANDGate.csv")
data=data_csv.values.tolist()
weight=[]
prediction=[]
activation=[]

def main():
    for j in range(0,len(data_csv.columns)-1):
        ran=random.uniform(0,1)
        print(ran)
        weight.append(ran)
    for i in range(0,len(data)):
        value=predict(data[i])
        actualOutput=data[i][len(data_csv.columns)-1]
        error=value-actualOutput
        weight=errorSolving(error,data[i])
    print(weight)

def errorSolving(error,row):
    for i in range (0,len(weights)):
        weight[i]=weight[i]+0.9*(error)*row[i]

def predict(row):
    activation=weights[0]
    for i in range(1,len(row)-1):
        activation += weights[i] * row[i]
	return 1.0 if activation >= 0.0 else 0.0