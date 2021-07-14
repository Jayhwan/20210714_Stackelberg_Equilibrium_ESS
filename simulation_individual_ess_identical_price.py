from common_function import *
from indiv_function import *

load1 = np.array([0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.1, 1.2, 1.3,
                  1.35, 1.3, 1.25, 1.15, 1.1, 1.0, 0.85, 0.75, 0.65, 0.45, 0.3, 0.12])
load2 = np.array([0.12, 0.17, 0.24, 0.36, 0.49, 0.59, 0.75, 0.98, 1.15, 1.26, 1.41, 1.32,
                  1.25, 1.10, 0.86, 0.75, 0.68, 0.51, 0.41, 0.36, 0.28, 0.19, 0.1, 0.04])

loads = np.array([load1, load2])

load = np.array([loads[i % 2] for i in range(100)])

a_o_init = np.ones((2, total_user, time_step))

exp_our_model = []

def find_good_initial_point_indiv(act_user, t, load_matrix):
    max_scatter = 2000
    min_ec = np.inf
    min_par = np.inf
    best_ec_a_o = None
    best_par_a_o = None
    best_ec_index=0
    best_par_index=0
    for i in range(max_scatter):
        a_o = 3 * np.random.random((2, t))+1 * np.ones((2, t))
        a_o[0] = np.minimum(a_o[0], a_o[1])
        a_o[1] = np.maximum(a_o[0], a_o[1])

        result, x_s, x_b, l, time = follower_action_indiv(act_user, t, a_o, load_matrix)
        a_f = np.array([x_s, x_b, l])
        if result == - np.inf:
            print("fail")
            continue
        else:
            ec = get_ec(act_user, t, load_matrix, a_o, a_f)
            pa = get_par(act_user, t, load_matrix, a_o, a_f)
            if ec < min_ec:
                best_ec_a_o = a_o
                best_ec_index = i
                min_ec = ec
                print(ec, pa)
            elif pa < min_par:
                best_par_a_o = a_o
                best_par_index = i
                min_par = pa
    print(min_ec, min_par, best_ec_index, best_par_index)
    return best_ec_a_o, best_par_a_o


exp_scatter = []
for i in range(101):
    print("active user number :", i)
    if i==0:
        a_o = None
        a_f = None
    else:
        best_a_o, _ = find_good_initial_point_indiv(i, time_step, load)
        a_o, a_f = iterations_indiv(i, time_step, load, best_a_o)
    exp_scatter += [[a_o, a_f, load]]
    np.save("exp_scatter_indiv_1.npy", exp_scatter)