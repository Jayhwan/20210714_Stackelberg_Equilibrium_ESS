import numpy as np
import matplotlib.pyplot as plt

load1 = np.array([0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.1, 1.2, 1.3,
                  1.35, 1.3, 1.25, 1.15, 1.1, 1.0, 0.85, 0.75, 0.65, 0.53, 0.48, 0.36])
load2 = np.array([0.36, 0.51, 0.75, 0.98, 1.28, 1.38, 1.32, 1.25, 1.10, 0.86, 0.75, 0.68,
                  0.59, 0.53, 0.51, 0.48, 0.41, 0.36, 0.33, 0.28, 0.19, 0.16, 0.1, 0.04])

plt.plot(load1)
plt.plot(load2)
plt.show()

x = np.load("exp_scatter_random_ec_1.npy", allow_pickle=True)

print(np.shape(x))