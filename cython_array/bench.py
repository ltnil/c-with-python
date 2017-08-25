# coding=utf8

import numpy
import sample
import timeit

a = numpy.random.uniform(-10,10,size=1000000)
c = numpy.zeros_like(a)

print('numpy takes:',
    timeit.timeit('numpy.clip(a,-5,5,c)', """
import numpy
import sample

a = numpy.random.uniform(-10,10,size=1000000)
c = numpy.zeros_like(a)
numpy.clip(a,-5,5,c)
""", number=1000))
print('cython clip takes:',
    timeit.timeit('numpy.clip(a,-5,5,c)', """
import numpy
import sample

a = numpy.random.uniform(-10,10,size=1000000)
c = numpy.zeros_like(a)
sample.clip(a,-5,5,c)
""", number=1000))
print('cython clip2 takes:',
    timeit.timeit('numpy.clip(a,-5,5,c)', """
import numpy
import sample

a = numpy.random.uniform(-10,10,size=1000000)
c = numpy.zeros_like(a)
sample.clip2(a,-5,5,c)
""", number=1000))
print('cython clip_nogil takes:',
    timeit.timeit('numpy.clip(a,-5,5,c)', """
import numpy
import sample

a = numpy.random.uniform(-10,10,size=1000000)
c = numpy.zeros_like(a)
sample.clip_nogil(a,-5,5,c)
""", number=1000))
# print(timeit.timeit('sample.clip(a,-5,5,c)', 'from __main__ import a,c,sample', number=1000))