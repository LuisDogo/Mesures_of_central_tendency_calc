import numpy as np

def calculate(lista):
    if(len(lista) != 9):
        raise Exception("List must contain nine numbers")
    else:
        #[(1,2,3),(4,5,6),(7,8,9)]
        matriz = np.array([(lista[0:3]),(lista[3:6]),(lista[6:9])])
        print(matriz)
        flat_mean = matriz.mean()
        flat_stdev = np.std(matriz)
        flat_var = np.var(matriz)
        flat_min = matriz.min()
        flat_max = matriz.max()
        flat_sum = matriz.sum()
        ax1Mean = [] # col
        ax1StdDev = []
        ax1Var = []
        ax1Min = []
        ax1Max = []
        ax1Sum = []
        ax2Mean = [] # i
        ax2StdDev = []
        ax2Var = []
        ax2Min = []
        ax2Max = []
        ax2Sum = []
        for i in range(0,3):
            ax1Mean.append(matriz[:,i].mean())
            ax1StdDev.append(np.std(matriz[:,i]))
            ax1Var.append(np.var(matriz[:,i]))
            ax1Min.append(matriz[:,i].min())
            ax1Max.append(matriz[:,i].max())
            ax1Sum.append(matriz[:,i].sum())
            ax2Mean.append(matriz[i,:].mean())
            ax2StdDev.append(np.std(matriz[i,:]))
            ax2Var.append(np.var(matriz[i,:]))
            ax2Min.append(matriz[i,:].min())
            ax2Max.append(matriz[i,:].max())
            ax2Sum.append(matriz[i,:].sum())

        calculations = {
            "mean" : [ax1Mean,ax2Mean,flat_mean],
            "variance" : [ax1Var,ax2Var,flat_var],
            "standard deviation" : [ax1StdDev,ax2StdDev,flat_stdev],
            "max" : [ax1Max,ax2Max,flat_max],
            "min" : [ax1Min,ax2Min,flat_min],
            "sum" : [ax1Sum,ax2Sum,flat_sum]
        }

    return calculations