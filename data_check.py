import matplotlib.pyplot as plt
import numpy as np
from common_function import *
from indiv_function import *
from scipy.stats import truncnorm

load1 = np.array([0.7, 1.12, 1.32, 1.3, 1.13, 0.9,
                  0.73, 0.42, 0.30, 0.33, 0.41, 0.51])
load2 = np.array([0.35, 0.31, 0.39, 0.59, 0.78, 0.85,
                  1.01, 1.27, 1.33, 1.23, 0.93, 0.65])

loads = np.array([load1, load2])

#load = np.array([loads[i % 2] + truncnorm.rvs(-0.1, 0.1, size=12) for i in range(100)])
#np.save("two_type_load.npy", load)
load = np.load("two_type_load.npy", allow_pickle=True)
for i in range(100):
    plt.plot(load[i])
plt.show()


#x = np.load("exp_scatter_random_ec_1.npy", allow_pickle=True)

#print(np.shape(x))

#a_o = 0 * np.random.random((2, time_step)) + 1 * np.ones((2, time_step))
#tmp = np.minimum(a_o[0], a_o[1])
#a_o[1] = np.maximum(a_o[0], a_o[1])
#a_o[0] = tmp

#a_o, a_f = iterations_indiv(20, time_step, load, a_o)

for i in range(51):
    exps = []
    np.save("exp_shared_identical_price_"+str(i)+".npy", exps)
    np.save("exp_individual_identical_price_"+str(i)+".npy", exps)
    np.save("exp_shared_random_identical_price_"+str(i)+".npy", exps)

