import time
import array
import numpy as np
from pyrsistent import s
from timeit import default_timer as timer

import cythonfn_type_annotations

def main(STREAM_ARRAY_TYPE, STREAM_ARRAY_SIZE):
    a = array.array(STREAM_ARRAY_TYPE, [1.0] * STREAM_ARRAY_SIZE)
    b = array.array(STREAM_ARRAY_TYPE, [2.0] * STREAM_ARRAY_SIZE)
    c = array.array(STREAM_ARRAY_TYPE, [0.0] * STREAM_ARRAY_SIZE)
    scalar = 2.0
    times = [0.0] * 4
    times[0] = timer()
    cythonfn_type_annotations.cython_copy(a, c)
    times[0] = timer() - times[0]

    times[1] = timer()
    cythonfn_type_annotations.cython_scale(b, c, scalar)
    times[1] = timer() - times[1]

    times[2] = timer()
    cythonfn_type_annotations.cython_add(a, b, c)
    times[2] = timer() - times[2]

    times[3] = timer()
    cythonfn_type_annotations.cython_triad(a, b, c, scalar)
    times[3] = timer() - times[3]

    print("Python list: ", times)
    return times



if __name__ == "__main__":
    import matplotlib.pyplot as plt
    labels = ["copy", "scale", "sum", "triad"]
    bandwith_copy_python_list = []
    bandwith_scale_python_list = []
    bandwith_sum_python_list = []
    bandwith_triad_python_list = []
    bandwith_copy_array = []
    bandwith_scale_array = []
    bandwith_sum_array = []
    bandwith_triad_array = []
    bandwith_copy_numpy = []
    bandwith_scale_numpy = []
    bandwith_sum_numpy = []
    bandwith_triad_numpy = []
    STREAM_ARRAY_SIZE = 10000
    STREAM_ARRAY_TYPE = 'd'

    while STREAM_ARRAY_SIZE < 100000000:
        times = main(STREAM_ARRAY_TYPE, STREAM_ARRAY_SIZE)
    # 
        c = STREAM_ARRAY_SIZE
        # calculate MB/s for each operation
        import cython
        import sys
        print(times)
        for i in range(len(times)):
            times[i] = (2 * sys.getsizeof(cython.p_double) * STREAM_ARRAY_SIZE / 2**20) / times[i]
        # plot
        for index, t in enumerate(times):
            if index == 0:
                bandwith_copy_python_list.append(t)
            elif index == 1:
                bandwith_scale_python_list.append(t)
            elif index == 2:
                bandwith_sum_python_list.append(t)
            elif index == 3:
                bandwith_triad_python_list.append(t)
            
            
            
            
        print("STREAM_ARRAY_SIZE: ", STREAM_ARRAY_SIZE)
        STREAM_ARRAY_SIZE *= 10
        
    # plot by different implementations
    plt.plot(bandwith_copy_python_list, label="copy cython")
    plt.plot(bandwith_scale_python_list, label="scale cython")
    plt.plot(bandwith_sum_python_list, label="sum cython")
    plt.plot(bandwith_triad_python_list, label="triad cython")
    
    plt.xlabel("STREAM_ARRAY_SIZE, 10^8")
    plt.ylabel("Bandwith (MB/s)")
    plt.title("Bandwith Cython")
    plt.legend()
    plt.savefig("cython_stream_benchmark.png")


