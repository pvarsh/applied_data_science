# Linear example regression using scipy
# From:  http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html

from scipy import stats
import numpy as np

from matplotlib import pyplot as plt

np.random.seed(1234)
x = np.random.random(10)
y = np.random.random(10)
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

plt.plot(x, y, 'co')
plt.xlim(-.1, 1.1)
plt.ylim(-.1, 1.1)
plt.show()

