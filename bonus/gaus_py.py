import numpy as np
import time
import gauss_seidel
def main():
    array_size = 10
    x = np.zeros((array_size,array_size))
    times = []
    array_sizes = []
    while array_size <= 180:
        
        x = np.zeros((array_size,array_size))
        start = time.time()
        for i in range(1000):  
            gauss_seidel.gauss_seidel(x)
        end = time.time()


        # print(arr)
        times.append(end - start)
        array_sizes.append(array_size)
        print(times)
        print(array_size)
        array_size *= 2
    print(times)

    # plot the results
    import matplotlib.pyplot as plt

    # plot time per size for each method

    plt.plot([10,20, 40, 80, 160], times, label="imported c")
    plt.xlabel('Size of array')
    plt.ylabel('Time (s)')
    plt.title('Time per size')
    plt.legend()
    plt.savefig('time_per_size_gaus.png')


if __name__ == "__main__":
    main()
