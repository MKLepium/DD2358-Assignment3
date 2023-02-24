
import time
import array
import numpy as np
import cython
cimport numpy as np
from cpython cimport array

from cython.parallel cimport prange


@cython.boundscheck(False)
def cython_copy(double[:] a, double[:] c):
    cdef int stream_array_size = a.shape[0]
    cdef int i
    for i in prange(stream_array_size, nogil=True):
        c[i] = a[i]

@cython.boundscheck(False)
def cython_scale(double[:] b, double[:] c, double scalar):
    cdef int stream_array_size = b.shape[0]
    cdef int i
    for i in prange(stream_array_size, nogil=True):
        b[i] = scalar*c[i]

@cython.boundscheck(False)
def cython_add(double[:] a, double[:] b, double[:] c):
    cdef int stream_array_size = a.shape[0]
    cdef int i
    for i in prange(stream_array_size, nogil=True):
        c[i] = a[i]+b[i]

@cython.boundscheck(False)
def cython_triad(double[:] a, double[:] b, double[:] c, double scalar):
    cdef int stream_array_size = a.shape[0]
    cdef int i
    for i in prange(stream_array_size, nogil=True):
        a[i] = b[i]+scalar*c[i]