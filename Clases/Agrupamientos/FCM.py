import numpy as np, pandas as pd
from fcmeans import FCM
from matplotlib import pyplot as plt

def fcm_process(dS_C):

    modelo =FCM(n_clusters=2)
    modelo.fit(dS_C)
    fcm_C = modelo.centers
    fcm_L = modelo.predict(dS_C)

    f, ejes = plt.subplots(1, 2, figsize=(8,8))
    ejes[0].scatter(dS_C[:,0], dS_C[:,1], alpha=.1)
    ejes[1].scatter(dS_C[:,0], dS_C[:,1], c=fcm_L, alpha=.1)
    ejes[1].scatter(fcm_C[:,0], fcm_C[:,1], marker="+", s=500, c='w')
    plt.show()
