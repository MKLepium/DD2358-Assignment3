import numpy as np
import array
import time

import gauss_seidel_cython
def main():
    array_size = 10
    x = np.zeros((array_size,array_size))
    time_per_size = []
    while array_size <= 200:
        
        x = np.zeros((array_size,array_size))
        times = [0.0] * 3
        times[0] = time.time()
        for i in range(1000):    
            x = gauss_seidel_cython.gauss_seidel_numpy(x)
        times[0] = time.time() - times[0]

        
        x = [[0.0 for i in range(array_size)] for j in range(array_size)]
        times[1] = time.time()
        for i in range(1000):
            x = gauss_seidel_cython.gauss_seidel_list(x)
        times[1] = time.time() - times[1]



        arr = array.array('d', [0.0 for i in range(array_size*array_size)])


        times[2] = time.time()
        for i in range(1000):
            arr = gauss_seidel_cython.gauss_seidel_array(arr)
        times[2] = time.time() - times[2]
        # print(arr)
        time_per_size.append(times)
        print(times)
        print(array_size)
        array_size *= 2
    print(time_per_size)

    # plot the results
    import matplotlib.pyplot as plt

    # plot time per size for each method

    plt.plot([10,20, 40, 80, 160], [time_per_size[0][0],time_per_size[1][0],time_per_size[2][0],time_per_size[3][0], time_per_size[4][0]], label="numpy")
    plt.plot([10,20, 40, 80, 160], [time_per_size[0][1],time_per_size[1][1],time_per_size[2][1],time_per_size[3][1], time_per_size[4][1]], label="list")
    plt.plot([10,20, 40, 80, 160], [time_per_size[0][2],time_per_size[1][2],time_per_size[2][2],time_per_size[3][2], time_per_size[4][2]], label="array")
    plt.xlabel('Size of array')
    plt.ylabel('Time (s)')
    plt.title('Time per size for each method')
    plt.legend()
    plt.savefig('time_per_size_gaus_cythonize_without_types.png')


if __name__ == "__main__":
    main()
