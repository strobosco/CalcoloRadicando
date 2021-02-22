import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd


def printPlot():

    data = pd.read_csv("risultatiMini.csv")
    print(data.head())

    data = data.iloc[ :5000, :]
    
    #data.pivot("Radicando", ["Babilonese", "Errore", "Tangenti", "Inverso", "Sqrt"])
    #print(data.head())

    mpl.style.use('seaborn')

    plt.plot(
        data["Radicando"],
        data["Babilonese"],
        label="Babilonese"
    )
    plt.plot(
        data["Radicando"],
        data["Errore"],
        label="Errore"
    )
    plt.plot(
        data["Radicando"],
        data["Tangenti"],
        label="Tangenti"
    )
    plt.plot(
        data["Radicando"],
        data["Inverso"],
        label="Inverso"
    )
    plt.plot(
        data["Radicando"],
        data["Sqrt"],
        label="Sqrt"
    )
    plt.title("Paragone Metodi")
    plt.xlabel("Radicando")
    plt.ylabel("Valore Radice")
    plt.legend(loc="center right")
    plt.show()

if __name__ == "__main__":

    printPlot()