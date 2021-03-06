# data.py will create 2 .csv files

import csv
import math
import pandas as pd
import numpy as np

def Babilonese(num, iterazioni):

    Q = 0
    Qprec = num / 2
    for _ in range(iterazioni):
        Q = (Qprec + num / Qprec) / 2
        Qprec = Q

    return float(Q)

def Errore(num, iterazioni):

    EPS = 0.000001    

    Q = 0
    esci = 0
    Qprec = num / 2
    for _ in range(iterazioni):
        if esci == 0:
            Q = (Qprec + num / Qprec) / 2
            errore = abs((Q - Qprec) / Q)
            if errore < EPS:
                esci = 1
            else:
                Qprec = Q
        else: 
            break

    return float(Q)

def Tangenti(num, iterazioni):

    x = 1.0
    for _ in range(iterazioni):
        x = (x / 2) + (num / (2 * x))

    return float(x)

def Inverso(num, iterazioni):

    iterazioni = 50
    x = 2e-8
    for _ in range(iterazioni):
        x = 0.5 * x * (3 - (num * x * x))
    
    return 1.0 /float(x)


def main():

    radicando = np.arange(0.00000001, 0.0001, 0.00000005).tolist()
    iterazioni = 10

    with open("risultatiMini.csv", mode="w") as risultati:

        headers = ("Radicando", "Babilonese", "Errore", "Tangenti", "Inverso", "Sqrt")
        
        fileWriter = csv.writer(risultati, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
        fileWriter.writerow(headers)

        for num in radicando:

            babilonese = Babilonese(float(num), iterazioni)
            errore = Errore(float(num), iterazioni)
            tangenti = Tangenti(float(num), iterazioni)
            inverso = Inverso(float(num), iterazioni)
            sqrt = math.sqrt(float(num))

            fileWriter.writerow([num, babilonese, errore, tangenti, inverso, sqrt])

if __name__ == "__main__":

    main()

    data = pd.read_csv("risultatiMini.csv")
    print(data.head())