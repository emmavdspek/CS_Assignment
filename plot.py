import numpy as np
import matplotlib.pyplot as plt

xdata = np.linspace(0, 1, 1000)
ydata = np.sin(xdata)

plt.plot(xdata, ydata)
