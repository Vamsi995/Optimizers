from matplotlib import pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.lines import Line2D


class GradientDescent:

    def __init__(self, lr, gamma):
        self.weights = np.random.uniform(-5, 5, 2)
        self.lr = lr
        self.gamma = gamma
        self.vt = self.weights
        self.pvt = self.weights
        self.fn = lambda x, y: (x ** 2) + (y ** 2)
        self.dfn = [lambda x: 2 * x, lambda y: 2 * y]

        self.xlist = np.linspace(-5.0, 5.0, 10000)
        self.ylist = np.linspace(-5.0, 5.0, 10000)
        X, Y = np.meshgrid(self.xlist, self.ylist)
        Z = (X ** 2) + (Y ** 2)
        self.fig, (self.ax, self.ax1) = plt.subplots(1, 2)
        cp = self.ax.contour(X, Y, Z)
        self.line, = self.ax.plot([], [], lw=2)
        self.xdata = []
        self.ydata = []

        self.loss = Line2D([], [], color='black')
        self.ax1.add_line(self.loss)
        self.loss_xdata = []
        self.loss_ydata = []

    def find_gradient(self, weights):
        ret = np.array([self.dfn[0](weights[0]), self.dfn[1](weights[1])])

        return ret

    def gradient_update(self):
        iter = 10000

        for i in range(iter):
            self.weights -= self.lr * (self.find_gradient(self.weights))

    def animate(self, i):
        self.vt = self.pvt * self.gamma + self.lr * (self.find_gradient(self.weights - self.pvt * self.gamma))
        self.weights -= self.vt
        self.pvt = self.vt
        self.xdata.append(self.weights[0])
        self.ydata.append(self.weights[1])

        self.loss_xdata.append(i)
        self.loss_ydata.append(self.fn(self.weights[0], self.weights[1]))

        self.ax1.plot(self.loss_xdata, self.loss_ydata)

        self.line.set_data(self.xdata, self.ydata)

        return self.line,

    def plotContour(self):
        anim = FuncAnimation(self.fig, self.animate,
                             frames=100, interval=20, blit=True)
        anim.save('growingCoil.mp4', writer='ffmpeg', fps=5)
