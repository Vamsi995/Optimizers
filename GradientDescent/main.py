from matplotlib import pyplot as plt
import numpy as np
from descent import GradientDescent


def main():

    grad = GradientDescent(0.2)
    grad.plotContour()


if __name__ == "__main__":
    main()