cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef clip(double[:] a, double min, double max, double[:] out):
    if min>max:
        raise ValueError("min must be <= max")
    if a.shape[0] != out.shape[0]:
        raise ValueError("input and output arrays must be the same size")
    for i in range(a.shape[0]):
        if a[i]< min:
            out[i] = min
        elif a[i] > max:
            out[i] = max
        else:
            out[i] = a[i]


@cython.boundscheck(False)
@cython.wraparound(False)
cpdef clip2(double[:] a, double min, double max,double[:] out):
    if min>max:
        raise ValueError("min must be <= max")
    if a.shape[0] != out.shape[0]:
        raise ValueError("input and output arrays must be the same size")
    for i in range(a.shape[0]):
        out[i] = (a[i] if a[i] < max else max) if a[i] >min else min

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef clip_nogil(double[:] a, double min, double max,double[:] out):
    if min>max:
        raise ValueError("min must be <= max")
    if a.shape[0] != out.shape[0]:
        raise ValueError("input and output arrays must be the same size")
    with nogil:
        for i in range(a.shape[0]):
            out[i] = (a[i] if a[i] < max else max) if a[i] >min else min