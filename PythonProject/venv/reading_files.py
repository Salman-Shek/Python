import pandas as pd
sales = pd.read_csv("C:\\Users\\ssalman\\OneDrive - HARMAN\\Desktop\\sms\\100-Sales-Records\\100 Sales Records.csv")
print(sales.head())

def load_csv(filepath):
    data =  []
    col = []
    checkcol = False
    with open(filepath) as f:
        for val in f.readlines():
            val = val.replace("\n","")
            val = val.split(',')
            if checkcol is False:
                col = val
                checkcol = True
            else:
                data.append(val)
    df = pd.DataFrame(data=data, columns=col)
    return df

file = load_csv("C:\\Users\\ssalman\\OneDrive - HARMAN\\Desktop\\sms\\100-Sales-Records\\100 Sales Records.csv")

print(file)

###################

import numpy as np
file2 = np.loadtxt(fname="C:\\Users\\ssalman\\OneDrive - HARMAN\\Desktop\\sms\\test2.txt",delimiter='|')
print(file2)

file3 = np.genfromtxt(fname="C:\\Users\\ssalman\\OneDrive - HARMAN\\Desktop\\sms\\100-Sales-Records\\100 Sales Records.csv",delimiter=',')
print(file3)


file3 = np.genfromtxt(fname="C:\\Users\\ssalman\\OneDrive - HARMAN\\Desktop\\sms\\100-Sales-Records\\100 Sales Records.csv",delimiter=',', dtype=None, names=True, encoding='utf-8')
print(pd.DataFrame(file3))

######################
import pickle

with open('test.pkl','wb') as f:
    pickle.dump(sales, f)

with open("test.pkl", "rb") as f:
    file4 = pickle.load(f)

print(file4)