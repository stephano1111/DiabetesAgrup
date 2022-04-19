import normalizar
import kms

#Normalizar los datos del dataframe:
#dbN = normalizar.normaliza()
dbN = normalizar.minMaxScaler("preg","pres")
print("\n DataFrame Normalizado: \n", dbN.head())
#Fin de normalizar datos del dataframe.

kms.kMENS(dbN,"preg","pres")