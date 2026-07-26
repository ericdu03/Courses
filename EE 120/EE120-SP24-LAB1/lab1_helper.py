"""DO NOT CHANGE THIS FILE"""

import numpy as np
import time

def get_speedup(f, g, num_trials=10):
    """
    Report the average speedup time over NUM_TRIALS attempts for convolving 
    two randomly generated length 500 signals using "f", a Python function
    to perform convolution, versus a naive numpyless implementation.
    """
    signal1 = np.random.randn(500)
    signal2 = np.random.randn(500)
    
    your_avg_time, default_avg_time = 0, 0
    for trial in range(num_trials):
        # Time your numpy-based convolution function
        t_start = time.time()
        f(signal1, signal2)
        t_end = time.time()
        your_avg_time += t_end - t_start

        # Time numpy-free convolution
        t_start = time.time()
        g(signal1, signal2)
        t_end = time.time()
        default_avg_time += t_end - t_start
    
    your_avg_time, default_avg_time = your_avg_time / num_trials, default_avg_time / num_trials
    print("Without NumPy: {} sec".format(round(default_avg_time, 4)))
    print("With NumPy:    {} sec".format(round(your_avg_time, 4)))
    print("NumPy gives a {}x speedup".format(round(default_avg_time / your_avg_time, 4)))