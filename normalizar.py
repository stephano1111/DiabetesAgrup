from fileinput import filename
from socket import herror
import pandas as pd

filename = "Base/diabetes.csv"
headers = ["preg","plas","pres","skin","insu","mass","pedi","age","class"]

db = pd.read_csv(filename, names = headers)

print("\n", db.head())

print("\n Numero de instancias: ", len(db.axes[0]))

"""
print("\n", type(db["class"][0]), "\n")


for i in range(len(db.axes[0])):
    if db["class"][i] == "tested_positive":
        db["class"][i] = 1
    else: db["class"][i] = 0
"""
db.loc[db['class'] == 'tested_negative', 'class'] = '0'
db.loc[db['class'] == 'tested_positive', 'class'] = '1'

print("\n", db.head())