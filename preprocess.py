import pandas
import sys
data_csv=pandas.DataFrame()
out_data=pandas.DataFrame()
data=[]
classifier=0
className=""
arguments=sys.argv
def classify():
    for i in range(0,len(data)):
        if data[i][classifier]==className:
            data[i][classifier]=1
        else:
            data[i][classifier]=0
        out_data.loc[len(out_data)]=data[i]
if arguments[1]=='--classify':  
    if len(arguments)==7:
        data_csv=pandas.read_csv(arguments[2])
        data=data_csv.values.tolist()
        out_data=pandas.DataFrame(columns=data_csv.columns)
        classifier=int(arguments[4])
        className=arguments[6]
        classify()
        out_data.to_csv("preprocessed.csv", index=False)
if arguments[1]=='--remove':
    data_csv=pandas.read_csv(arguments[2])
    if arguments[3]=="--column":
        out_data=data_csv.drop(data_csv.columns[int(arguments[4])] , axis=1)
    elif arguments[3]=="--row":
        out_data=data_csv.drop(int(arguments[4]))
    out_data.to_csv("preprocessed.csv", index=False)