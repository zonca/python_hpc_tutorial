#!/usr/bin/env python3
import sys
import numpy as np

def inside_circle(total_count):

    x = np.random.uniform(size=total_count)
    y = np.random.uniform(size=total_count)

    radii_square = x**2 + y**2

    count = (radii_square<=1.0).sum()

    return count

def estimate_pi(n_samples):

    return (4.0 * inside_circle(n_samples) / n_samples)

if __name__=='__main__':

    n_samples = 10000
    if len(sys.argv) > 1:
        n_samples = int(sys.argv[1])

    my_pi = estimate_pi(n_samples)
    sizeof = np.dtype(np.float64).itemsize

    print("required memory {:.3f} MB".format(n_samples*sizeof*3/(1024*1024)))
    print("pi is {} from {} samples".format(my_pi,n_samples))
    print("error is {:.3e}".format(abs(my_pi - np.pi)))
