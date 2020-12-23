from matplotlib import pyplot as plt
import numpy as np
from descent import GradientDescent


def main():

    grad = GradientDescent(0.2)
    grad.plotContour()


def plotContour():
    xlist = np.linspace(-3.0, 3.0, 100)
    ylist = np.linspace(-3.0, 3.0, 100)
    X, Y = np.meshgrid(xlist, ylist)
    Z = (X**2) + (Y ** 2)
    fig, ax = plt.subplots(1, 1)
    cp = ax.contourf(X, Y, Z)
    fig.colorbar(cp)
    ax.set_title('Filled Contours Plot')
    ax.set_ylabel('y (cm)')
    plt.show()


if __name__ == "__main__":
    main()