'''
import math

print(math.log(10))
print(math.exp(5))
print(math.sqrt(256))

import numpy as np

income = np.array([20, 30, 40, 10])
print(income)
print(income[0])

'''
import pandas as pd
test1 = pd.read_csv('C:\\Users\\ssalman\\OneDrive - HARMAN\\Desktop\\sms\\test1.txt')
print(test1)

test2 = pd.read_csv('C:\\Users\\ssalman\\OneDrive - HARMAN\\Desktop\\sms\\test2.txt')
print(test2)

hub = pd.read_csv('C:\\Users\\ssalman\\OneDrive - HARMAN\\Desktop\\sms\\HubTransaction1.csv')
print(hub)
print(type(hub))

print(len(hub))
print(hub.shape)

print(hub.head(10))
pd.set_option('display.max.columns',5)
pd.set_option('display.precision',2)
print(hub.tail())

hub.info()                  # -- number of columns and datatype
print(hub.describe())       # -- min, max, avg of number colus
print(hub['PmcTransactionId'].value_counts())   # -- Count of records per PmcTransactionId / duplicate count
print(hub['PharmName'].value_counts())
print(hub['PharmName'].agg)

''' 
import requests
response = requests.get('https://github.com/Salman-Shek/salman2sms/blob/main/HubTransaction1.csv')
print(response.status_code)

with open('hubfile.csv', 'wb') as f:
    f.write(response.content)

nba = pd.read_csv('hubfile.csv')
print(nba)
'''


