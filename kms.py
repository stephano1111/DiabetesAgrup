import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans


def Km(db):
    km = KMeans(n_clusters=2, init='random', 
            max_iter=200, random_state=0)
    yKm = km.fit_predict(db)
    return yKm, km

def kMENS(dbN2,a,b):
    
    #dbN2 = db
    #for i in headers:
        #if i != a:
            #if i != b:
                #dbN2 = dbN2.drop(i, axis=1)
    yKm, km = Km(dbN2)         
    #dbN2 = pd.DataFrame(data=[dbN2[a],dbN2[b]], columns=[0,1])  
    print("\n DataFrame con las columnas a visualizar: \n", dbN2.head())
    
    plt.figure(figsize=(8,8))
    plt.scatter(dbN2[yKm == 0][0], dbN2[yKm == 0][1], 
                s=50, c='green', marker='o', 
                edgecolor='black', label='cluster 1')
    plt.scatter(dbN2[yKm == 1][0], dbN2[yKm == 1][1],  
                s=50, c='orange', marker='s', 
                edgecolor='black', label='cluster 2')
    plt.scatter(km.cluster_centers_[:, 0], 
                km.cluster_centers_[:, 1], s=200, 
                marker='*', c='red', 
                edgecolor='black', label='centroides')
    plt.legend(loc="best")
    plt.grid()
    dbN2.plot.scatter(x=a, y=b, c='DarkGreen')
    plt.show()
    return 