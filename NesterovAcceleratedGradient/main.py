from Descent.descent import GradientDescent


def main():

    grad = GradientDescent(0.2,0.5, "NAG")
    grad.plotContour()


if __name__ == "__main__":
    main()