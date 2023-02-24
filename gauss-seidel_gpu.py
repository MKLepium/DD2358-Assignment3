import copy
import numpy as np
import torch

def gauss_seidel_gpu(f):
    # convert 2D list to PyTorch tensor
    f_tensor = torch.tensor(f)

    # move tensor to GPU
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    f_tensor = f_tensor.to(device)

    # apply Gauss-Seidel algorithm
    for _ in range(100):
        f_tensor[1:-1, 1:-1] = 0.25 * (torch.roll(f_tensor, shifts=1, dims=0)[1:-1, 1:-1] +
                                       torch.roll(f_tensor, shifts=-1, dims=0)[1:-1, 1:-1] +
                                       torch.roll(f_tensor, shifts=1, dims=1)[1:-1, 1:-1] +
                                       torch.roll(f_tensor, shifts=-1, dims=1)[1:-1, 1:-1])

    # move tensor back to CPU and convert to 2D list
    newf = f_tensor.cpu().detach().numpy().tolist()

    return newf

# import cupy as cp
# def gauss_seidel_cupy(f):
#     newf = cp.array(f)
    
#     for _ in range(100):
#         newf[1:-1, 1:-1] = 0.25 * (cp.roll(newf, -1, axis=0)[1:-1, 1:-1] +
#                                     cp.roll(newf, 1, axis=0)[1:-1, 1:-1] +
#                                     cp.roll(newf, -1, axis=1)[1:-1, 1:-1] +
#                                     cp.roll(newf, 1, axis=1)[1:-1, 1:-1])
    
#     return newf.get()

import numpy as np
import array
import time
def main():
    array_size = 10
    x = np.zeros((array_size,array_size))
    time_per_size = []
    while array_size <= 25:
        
        x = np.zeros((array_size,array_size))
        times = [0.0] * 3
        times[0] = time.time()
        for i in range(1000):    
            x = gauss_seidel_gpu(x)
        times[0] = time.time() - times[0]

        time_per_size.append(times)
        print(times)
        print(array_size)
        array_size *= 2
    print(time_per_size)

    # plot the results
    import matplotlib.pyplot as plt

    # plot time per size for each method

    #plt.plot([10, 20, 40, 80, 160], [time_per_size[i][0] for i in range(len(time_per_size))], label='GPU')
    #plt.xlabel('Size of array')
    #plt.ylabel('Time (s)')
    #plt.title('Time per size for each method')
    #plt.legend()
    # plt.savefig('time_per_size_gaus_cupy.png')

    import h5py
    with h5py.File("mytestfile.hdf5", "w") as f:
        # Create a new dataset and write the newgrid array to it
        dset = f.create_dataset('newgrid', data=x, dtype='d')

if __name__ == "__main__":
    main()
