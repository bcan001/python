# For a long time, the main disadvantage of interpreted languages like Python was the lack of speed when dealing with large volumes of data and complex mathematical operations. The Python NumPy (Numerical Python) library in particular takes the wind out of the sails of this allegation. It loads its data efficiently into memory and integrates C code, which compiles at run time.
import numpy

import scipy
import matplotlib
import pandas


# print numpy.array([1, 2, 3]) + numpy.array([1, 2, 3])
print
print "------"
print numpy.array([1, 2, 3])[2] * numpy.array([1, 2, 3])


print "-------------------"
# series objects
# s = pandas.Series([1, 2, 3])



