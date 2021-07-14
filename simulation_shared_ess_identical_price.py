from common_function import *

load1 = np.array([0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.1, 1.2, 1.3,
                  1.35, 1.3, 1.25, 1.15, 1.1, 1.0, 0.85, 0.75, 0.65, 0.45, 0.3, 0.12])
load2 = np.array([0.12, 0.17, 0.24, 0.36, 0.49, 0.59, 0.75, 0.98, 1.15, 1.26, 1.41, 1.32,
                  1.25, 1.10, 0.86, 0.75, 0.68, 0.51, 0.41, 0.36, 0.28, 0.19, 0.1, 0.04])

loads = np.array([load1, load2])

load = np.array([loads[i % 2] for i in range(100)])


a_o = np.ones((2, time_step))
a_o[1] *= 2

a_o, a_f = iterations(50, time_step, load, a_o)
