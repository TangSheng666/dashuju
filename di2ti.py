import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

np.random.seed(20200605)
lam = 48 / 3
size = 50000
x = np.random.poisson(lam, size)

print(np.sum(x == 3) / size)

plt.hist(x)
plt.xlabel('')
plt.ylabel('')
plt.show()

x = stats.poisson.pmf(3, lam)
print(x)