import numpy as np


def calculate(list):

    if len(list) != 9: 
        raise ValueError ("List must contain nine numbers.")
           
    else:
        a=np.array(list)
        a=a.reshape(3, 3)

#mean
        m0 = np.mean(a, axis=0).tolist()
        m1 = np.mean(a, axis=1).tolist()
        mf = np.mean(a).tolist()
        media = [m0,m1,mf]

#variance
        v0 = np.var(a, axis=0).tolist()
        v1 = np.var(a, axis=1).tolist()
        vf = np.var(a).tolist()
        varianza = [v0,v1,vf]

#standard desviation
        d0 = np.std(a, axis=0).tolist()
        d1 = np.std(a, axis=1).tolist()
        df = np.std(a).tolist()
        desviacion_estandar = [d0,d1,df]

#max
        max0 = np.max(a, axis=0).tolist()
        max1 = np.max(a, axis=1).tolist()
        maxf = np.max(a).tolist()
        maximo = [max0,max1,maxf]

#min
        min0 = np.min(a, axis=0).tolist()
        min1 = np.min(a, axis=1).tolist()
        minf = np.min(a).tolist()
        minimo = [min0,min1,minf]

#sum
        sum0 = np.sum(a, axis=0).tolist()
        sum1 = np.sum(a, axis=1).tolist()
        sumf = np.sum(a).tolist()
        suma = [sum0,sum1,sumf]

        calculations = {
            'mean': media,
            'variance': varianza,
            'standard deviation': desviacion_estandar,
            'max': maximo,
            'min': minimo,
            'sum': suma
        }
    return calculations
    
