# Adding lines to plots
# From http://stackoverflow.com/questions/12864294/adding-an-arbitrary-line-to-a-matplotlib-plot-in-ipython-notebook

import numpy as np
from matplotlib import pyplot as plt
np.random.seed(5)
x = np.arange(1, 101)
y = 20 + 3 * x + np.random.normal(0, 60, 100)
p =  plt.plot(x, y, "o")
plt.vlines(70,100,250)
plt.show()