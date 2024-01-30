import numpy

speed = [77, 78, 85, 86, 86, 86, 87, 87, 94, 98, 99, 103]

Mean=numpy.mean(speed)
Median=numpy.median(speed)
print(Mode)

from scipy import stats
Mode=stats.mode(speed)
print(Mode)