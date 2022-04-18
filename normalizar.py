import pandas as pd
import numpy as np
from sklearn import preprocessing

"""
filename = "Base/diabetes.csv"
headers = ["preg","plas","pres","skin","insu","mass","pedi","age","class"]

db = pd.read_csv(filename, names = headers)
pd.options.mode.chained_assignment = None

print("\nDataFrame Normal: \n", db.head())

print("\n Numero de instancias: ", len(db.axes[0]))

db.loc[db['class'] == 'tested_negative', 'class'] = '0'
db.loc[db['class'] == 'tested_positive', 'class'] = '1'

print("\nDataFrame Class val 0/1: \n", db.head())
"""
#print("\n", headers[0])

"""
pregArr = np.array(db['preg'])
print("\n", pregArr)
arrayNorm = preprocessing.normalize([pregArr])
print("\n", arrayNorm[0])

print("\n", len(arrayNorm[0]))
"""
def normaliza():
    filename = "Base/diabetes.csv"
    headers = ["preg","plas","pres","skin","insu","mass","pedi","age","class"]

    db = pd.read_csv(filename, names = headers)
    pd.options.mode.chained_assignment = None

    print("\nDataFrame Normal: \n", db.head())

    print("\n Numero de instancias: ", len(db.axes[0]))

    db.loc[db['class'] == 'tested_negative', 'class'] = '0'
    db.loc[db['class'] == 'tested_positive', 'class'] = '1'

    print("\nDataFrame Class val 0/1: \n", db.head())
    dbN = db
    for i in range(len(headers)-1):
        arrDim = np.array(db[headers[i]])
        arrayNorm = preprocessing.normalize([arrDim])
        for j in range(len(arrayNorm[0])):
            dbN[headers[i]][j] = arrayNorm[0][j]
    return dbN

"""
dbN = normaliza(db)
print("\n DataFrame Normalizado: \n", dbN.head())
"""