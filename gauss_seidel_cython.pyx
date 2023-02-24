import copy
import numpy as np

def gauss_seidel_numpy(f):
    newf = copy.deepcopy(f)
    
    for i in range(1,newf.shape[0]-1):
        for j in range(1,newf.shape[1]-1):
            newf[i,j] = 0.25 * (newf[i,j+1] + newf[i,j-1] +
                                   newf[i+1,j] + newf[i-1,j])
    return newf

def gauss_seidel_list(f):
    newf = copy.deepcopy(f)
    
    for i in range(1,len(newf)-1):
        for j in range(1,len(newf[1])-1):
            newf[i][j] = 0.25 * (newf[i][j+1] + newf[i][j-1] +
                                   newf[i+1][j] + newf[i-1][j])
    
    return newf

import math
import array
def gauss_seidel_array(f):
    newf = copy.deepcopy(f)
    size = int(math.sqrt(len(f)))
    # apply Gauss-Seidel algorithm
    # print(newf)
    for i in range(1, size-1):
        for j in range(1, size-1):
            # calculate the new value for the current point
            new_val = 0.25 * (newf[i*size + j+1] + newf[i*size + j-1] +
                              newf[(i+1)*size + j] + newf[(i-1)*size + j])


            newf[i*size + j] = new_val


    return newf