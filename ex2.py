import numpy as np

h = 1

def create_n(N):
    """ creates all possoble sites n in binary represantation,
     output is list of strings like '101' """

    all_n = np.array([])
    max_bin_len = len(bin(2 ** N - 1)[2:])  # need this for 2 -> 010 instead of 10

    for i in range(2**N):
        all_n = np.append(all_n, bin(i)[2:].zfill(max_bin_len))

    return all_n



def calc_H(J, N):
    """ calculates H matrix for given coupling J"""

    H = np.array([[0.0] * 2 ** N for i in range(2 ** N)])
    max_bin_len = len(bin(2 ** N - 1)[2:])  # need this for 2 -> 010 instead of 10

    for n in create_n(N):

        n_dec = int(n, 2) # converts binary to integer

        for link in ['x', 'y', 'z']:

            for i in range(N): # loop over the combinations 12, 23 and 31
                j = i + 1
                if j == N:
                    j = 0

                # calculating l
                new_i = (max_bin_len - 1) - i  # need to preprocess i, j and k because the most left site in |01 ... 1>
                new_j = (max_bin_len - 1) - j  # is the most right digit in its binary representation
                l = n_dec + (1 - 2*int(n[new_i])) * 2 ** i + (1 - 2 * int(n[new_j])) * 2 ** j # no -1 in power because indexing is zero based

                # inserting matrix elements
                if link == 'x':
                    H[l, n_dec] += -J[0, i, j] / 4
                elif link == 'y':
                    if n[i] == n[j]: # check for correct sign in y link
                        H[l, n_dec] += J[1, i, j] / 4
                    else:
                        H[l, n_dec] += -J[1, i, j] / 4
                else: # z link
                    if n[i] == n[j]: # check for sign
                        H[n_dec, n_dec] += -J[2, i, j] * h / 4
                    else:
                        H[n_dec, n_dec] += J[2, i, j] * h / 4

    return H


# set up J's for b)
J = 1
N = 3
J_array = np.zeros((3, 3, 3))

#J_b as Ising model
J_b = J_array.copy()
J_b[2, :, :] = J

# J_c as isotropic Heisenberg model
J_c = J_array.copy()
J_c[:, :, :] = J

# J_d as in exercise 1 c)
J_d = J_array.copy()
J_d[0, 0, 1] = J
J_d[1, 1, 2] = J
J_d[2, 2, 0] = J

#print(calc_H(J_c, 3))
N = 3
max_bin_len = len(bin(2 ** N - 1)[2:])
n = '100'#create_n(N)[3]
n_dec = int(n, 2)
i = 0
j = 1
new_i = (max_bin_len - 1) - i  # need to preprocess i, j and k because the most left site in |01 ... 1>
new_j = (max_bin_len - 1) - j
print(n)
print(n_dec + (1 - 2*int(n[i])) * 2 ** i + (1 - 2 * int(n[j])) * 2 ** j)
