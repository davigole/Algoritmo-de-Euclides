import numpy as np
from mpl_toolkits import mplot3d
from matplotlib import pyplot as plt

import Iterações

INTERVAL = [0, 100]
ARANGE_SEP = .5
UPPER_BOUND = 100

FUNCTIONS = {
    "Solução Ingênua": Iterações.SolucaoIngenua,
    "Algoritmo de Euclides": Iterações.AlgoritmoDeEuclides,
    "Fatoração Prima": Iterações.FatoraçãoPrima,
}

def create_data(name):
    func = FUNCTIONS[name]
    
    x = y = np.arange(*INTERVAL, ARANGE_SEP)
    X, Y = np.meshgrid(x, y)
    Z = np.array([[func(int(i), int(j)) for j in x] for i in y])

    return X, Y, Z
def plot_data(X, Y, Z, name=""):
    ax = plt.axes(projection="3d")
    
    ax.set_xlim3d(0, UPPER_BOUND)
    ax.set_ylim3d(0, UPPER_BOUND)
    ax.set_zlim3d(0, UPPER_BOUND)
    
    ax.set_xlabel("A")
    ax.set_ylabel("B")
    ax.set_zlabel("Número de Iterações")
    
    ax.plot_surface(X, Y, Z)
    plt.title(name)
    plt.show()

def main():
    for name in FUNCTIONS.keys():
        plot_data(*create_data(name), name)


if __name__ == '__main__': main()