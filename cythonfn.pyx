
import time
import array
import numpy as np

def stream_python_list(STREAM_ARRAY_TYPE, STREAM_ARRAY_SIZE):
    a = [1.0] * STREAM_ARRAY_SIZE
    b = [2.0] * STREAM_ARRAY_SIZE
    c = [0.0] * STREAM_ARRAY_SIZE
    scalar = 2.0

    times = [0.0] * 4

    # copy
    times[0] = time.time()
    for j in range(STREAM_ARRAY_SIZE):
        c[j] = a[j]
    times[0] = time.time() - times[0]

    # scale
    times[1] = time.time()
    for j in range(STREAM_ARRAY_SIZE):
        b[j] = scalar*c[j]
    times[1] = time.time() - times[1]

    # sum
    times[2] = time.time()
    for j in range(STREAM_ARRAY_SIZE):
        c[j] = a[j]+b[j]
    times[2] = time.time() - times[2]

    # triad
    times[3] = time.time()
    for j in range(STREAM_ARRAY_SIZE):
        a[j] = b[j]+scalar*c[j]
    times[3] = time.time() - times[3]

    return times

def stream_array(STREAM_ARRAY_TYPE, STREAM_ARRAY_SIZE):
    a = array.array(STREAM_ARRAY_TYPE, [1.0] * STREAM_ARRAY_SIZE)
    b = array.array(STREAM_ARRAY_TYPE, [2.0] * STREAM_ARRAY_SIZE)
    c = array.array(STREAM_ARRAY_TYPE, [0.0] * STREAM_ARRAY_SIZE)
    scalar = 2.0

    times = [0.0] * 4

    # copy
    times[0] = time.time()
    for j in range(STREAM_ARRAY_SIZE):
        c[j] = a[j]
    times[0] = time.time() - times[0]

    # scale
    times[1] = time.time()
    for j in range(STREAM_ARRAY_SIZE):
        b[j] = scalar*c[j]
    times[1] = time.time() - times[1]

    # sum
    times[2] = time.time()
    for j in range(STREAM_ARRAY_SIZE):
        c[j] = a[j]+b[j]
    times[2] = time.time() - times[2]

    # triad
    times[3] = time.time()
    for j in range(STREAM_ARRAY_SIZE):
        a[j] = b[j]+scalar*c[j]
    times[3] = time.time() - times[3]

    return times

def stream_numpy(STREAM_ARRAY_TYPE, STREAM_ARRAY_SIZE):
    a = np.ones(STREAM_ARRAY_SIZE, dtype=STREAM_ARRAY_TYPE)
    b = np.ones(STREAM_ARRAY_SIZE, dtype=STREAM_ARRAY_TYPE) * 2
    c = np.zeros(STREAM_ARRAY_SIZE, dtype=STREAM_ARRAY_TYPE)
    scalar = 2.0

    times = [0.0] * 4

    # copy
    times[0] = time.time()
    c = a.copy()
    times[0] = time.time() - times[0]

    # scale
    times[1] = time.time()
    b = scalar * c
    times[1] = time.time() - times[1]

    # sum
    times[2] = time.time()
    c = a + b
    times[2] = time.time() - times[2]

    # triad
    times[3] = time.time()
    a = b + scalar * c
    times[3] = time.time() - times[3]

    return times

def main(STREAM_ARRAY_TYPE, STREAM_ARRAY_SIZE):
    times_python_list = stream_python_list(STREAM_ARRAY_TYPE, STREAM_ARRAY_SIZE)
    times_array = stream_array(STREAM_ARRAY_TYPE, STREAM_ARRAY_SIZE)
    times_numpy = stream_numpy(STREAM_ARRAY_TYPE, STREAM_ARRAY_SIZE)

    print("Python list: ", times_python_list)
    print("Array: ", times_array)
    print("Numpy: ", times_numpy)
    return (times_python_list, times_array, times_numpy)