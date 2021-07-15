import numpy as np

x = np.load("exp_scatter_shared_1.npy", allow_pickle=True)
print(np.shape(x[-1,1]))