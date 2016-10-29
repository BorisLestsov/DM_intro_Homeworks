import numpy as np


def f1(x):
    if x > 0:
        return x
    else:
        return 0.01 * x

def f2(x, sigma):
    return max(0.0, x + np.random.normal(0.0, sigma))

f1_v = np.vectorize(f1)
f2_v = np.vectorize(f2)

a = np.array([-1.0, -2.0, 1.0, 2.0])
np.set_printoptions(formatter={'float': '{: 0.4f}'.format})

print f1_v(a)
print f2_v(a, 2)