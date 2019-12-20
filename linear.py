import pandas
import random
import sys
learning_rate=0.2
data_csv=pandas.DataFrame()
data=[]
weights=[]
prediction=[]
activation=[]
arguments=sys.argv
col_names=[]


# for predict the value according to weights 

def predict():
        prediction=[]
        for d in data:
            p= (weights[1]*d[0]) + weights[0]
            prediction.append(p)
        return prediction
def errorSolving(predicted):
        # cost = sum([data**2 for data in (y-y_current)]) / N
        cost=0
        i=0
        while i<len (predicted):
            cost=cost+ (data[i][1]-predicted[i])**2
            i=i+1
        cost=cost/2*i
        gradient_0=0
        gradient_1=0
        for j in range (0,len(data)):
            gradient_1= gradient_1-(1/i) *data[j][0] * (data[j][1] - predicted[j])
            gradient_0 =gradient_0 -(1/i) *(data[j][1]- predicted[j])
        weights[0] = weights[0] - (learning_rate * gradient_0)
        weights[1] = weights[1] - (learning_rate * gradient_1)
     

#inialize the weights and threshould randomly
def initialize():  
    weights.append(random.uniform(learning_rate,1))     
    for j in range(0,len(data_csv.columns)-1):
        ran=random.uniform(0,1)
        weights.append(ran)

# learn weights from given data file
def learn():
    i=0
    while i<20:
        predictions=predict()
        errorSolving(predictions)
        save()
        i=i+1
            
    print("Done")
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

# when program learn from given data
 
if arguments[1]=="--learn":
    data_csv=pandas.read_csv(arguments[2])
    data=data_csv.values.tolist()
    initialize()
    for i in range(0,len(weights)):
        col_names.append('w'+str(i))
    mdf=pandas.DataFrame(columns=col_names)
    learn()
 
# when program use for testing
    
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
    weights=learningFile[len(learningFile)-1]
    for i in range(0,len(data)):
        values=[]
        predictedvalue=weights[0]+(weights[1]*data[i][0])
        values.append(data[i][0])
        k=len(data_csv.columns)-1
        values.append(data[i][k])
        values.append(predictedvalue)
        mdf.loc[len(mdf)]=values
    mdf.to_csv("testpredict.csv", index=False)
    print("Done")

    