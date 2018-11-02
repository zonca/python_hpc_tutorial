#!/usr/bin/env python3
import sys
import numpy as np
import dask.array as da
import dask

def inside_circle(total_count):

    x = da.random.uniform(size=total_count, chunks=total_count//12)
    y = da.random.uniform(size=total_count, chunks=total_count//12)

    radii_square = x**2 + y**2

    count = (radii_square<=1.0).sum()

    return count

def estimate_pi(n_samples):

    return (4.0 * inside_circle(n_samples) / n_samples)

if __name__=='__main__':
    n_samples = 10000
    if len(sys.argv) > 1:
        n_samples = int(sys.argv[1])

    my_pi = estimate_pi(n_samples).compute(num_workers=1)
    sizeof = np.dtype(np.float64).itemsize

    print("pi is {} from {} samples".format(my_pi,n_samples))
    print("error is {:.3e}".format(abs(my_pi - np.pi)))
