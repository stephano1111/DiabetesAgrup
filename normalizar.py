from fileinput import filename
from socket import herror
import pandas as pd

filename = "Base/diabetes.csv"
headers = ["preg","plas","pres","skin","insu","mass","pedi","age","class"]

db = pd.read_csv(filename, names = headers)

print(db.head())