from common_function import *

load1 = np.array([0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.1, 1.2, 1.3,
                  1.35, 1.3, 1.25, 1.15, 1.1, 1.0, 0.85, 0.75, 0.65, 0.45, 0.3, 0.12])
load2 = np.array([0.12, 0.17, 0.24, 0.36, 0.49, 0.59, 0.75, 0.98, 1.15, 1.26, 1.41, 1.32,
                  1.25, 1.10, 0.86, 0.75, 0.68, 0.51, 0.41, 0.36, 0.28, 0.19, 0.1, 0.04])

loads = np.array([load1, load2])

load = np.array([loads[i % 2] for i in range(100)])

exp_random_ec = []
exp_random_par = []

for i in range(101):
    print("active user :", i)
    max_scatter = 2000
    ec_list = []
    par_list = []
    for _ in range(max_scatter):
        if i == 0:
            ec = get_ec(i, time_step, load, None, None)
            pa = get_par(i, time_step, load, None, None)
            ec_list += [ec]
            par_list += [pa]
            continue
        a_o = 3 * np.random.random((2, time_step)) + 0 * np.ones((2, time_step))
        a_o[0] = np.minimum(a_o[0], a_o[1])

        result, x_s, x_b, l, time = follower_action(i, time_step, a_o, load)
        a_f = np.array([x_s, x_b, l])

        if result == - np.inf:
            print("fail")
            continue
        else:
            ec = get_ec(i, time_step, load, a_o, a_f)
            pa = get_par(i, time_step, load, a_o, a_f)
            ec_list += [ec]
            par_list += [pa]
            print(ec, pa)
    exp_random_ec += [ec_list]
    exp_random_par += [par_list]
    np.save("exp_scatter_random_ec_1.npy", exp_random_ec)
    np.save("exp_scatter_random_par_1.npy", exp_random_par)