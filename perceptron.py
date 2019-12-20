# Importing necessory modules
import pandas
import random
import sys
# Declaring global variables
learning_rate=0.2
data_csv=pandas.DataFrame()
data=[]
weights=[]
prediction=[]
activation=[]
arguments=sys.argv
col_names=[]
# Function to fix threshold
def fixThreshold(error):
    newBiase=weights[0]+learning_rate*(error)
    if newBiase>learning_rate and newBiase<1 :
        weights[0]=newBiase
# Function to predict output for an amaple in dataset
def predict(row):
    activation=0
    for i in range(1,len(weights)):
        activation+=weights[i]*row[i-1]
    activation-=weights[0]
    return 1 if activation>=0 else 0
# Function to update the weights according to the error
def errorSolving(error,row):
    for i in range (1,len(weights)):
        weights[i]=weights[i]+learning_rate*(error)*row[i-1]

# Function to initialize weights and threshold randomly
def initialize():  
    weights.append(random.uniform(learning_rate,1))     
    for j in range(0,len(data_csv.columns)-1):
        ran=random.uniform(0,1)
        weights.append(ran)
# Main entry point function to start learning 
def learn():
    flag=True
    while flag==True:
        flag=False
        for i in range(0,len(data)):
            value=predict(data[i])
            actualOutput=data[i][len(data_csv.columns)-1]
            error=actualOutput-value
            errorSolving(error,data[i])
            fixThreshold(error)
            save()
            if error!=0.0:
                flag=True  
    print("Done")
# Function to find Accuracy
def Accuracy():
    data_csv=pandas.read_csv('testpredict.csv')
    data=data_csv.values.tolist()
    actualIndex=len(data_csv.columns)-2
    predictedIndex=len(data_csv.columns)-1
    correct=0
    Truepositive=0
    for i in range(0,len(data)):
        if data[i][actualIndex]==data[i][predictedIndex]:
            correct=correct+1
    Accuracy=correct/len(data)*100
    print("Accuracy is: "+str(Accuracy)+"%")  
# Function to save weights calculated in each episode in a file
def save():
    values=[]
    for i in range(0,len(weights)):
        values.append(weights[i])
    mdf.loc[len(mdf)]=values
    print(values)
    if len(arguments)<4:
        mdf.to_csv("data.csv", index=False)
    else:  
        mdf.to_csv(arguments[4]+".csv", index=False) 

if arguments[1]=="--learn":
    data_csv=pandas.read_csv(arguments[2])
    data=data_csv.values.tolist()
    initialize()
    for i in range(0,len(weights)):
        col_names.append('w'+str(i))
    mdf=pandas.DataFrame(columns=col_names)
    values=[]
    for i in range(0,len(weights)):
        values.append(weights[i])
    mdf.loc[len(mdf)]=values
    learn()
if arguments[1]=="--test":
    data_csv=pandas.read_csv(arguments[2])
    data=data_csv.values.tolist()
    if len(arguments)<4:
        learningFile_csv=pandas.read_csv("data.csv")
        learningFile=learningFile_csv.values.tolist()
    else:
        learningFile_csv=pandas.read_csv(arguments[4])
        learningFile=learningFile_csv.values.tolist()
    prdictedValue=0
    for i in range(1,len(data_csv.columns)):
        col_names.append('x'+str(i))
    col_names.append('actualAnswer')
    col_names.append('Predicted')
    mdf=pandas.DataFrame(columns=col_names)
    for i in range(0,len(data)):
        values=[]
        activation=0
        for j in range(0,len(data_csv.columns)-1):
            values.append(data[i][j])
            activation+=learningFile[len(learningFile)-1][j+1]*data[i][j]
        activation=activation-learningFile[len(learningFile)-1][0]   
        if activation>=0:
            predictedValue=1
        else:
            predictedValue=0
        k=len(data_csv.columns)-1
        values.append(data[i][k])
        values.append(predictedValue)
        mdf.loc[len(mdf)]=values
        mdf.to_csv("testpredict.csv", index=False)
    print("Done")
    Accuracy()