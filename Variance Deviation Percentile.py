import numpy

speed = [77, 78, 85, 86, 86, 86, 87, 87, 94, 98, 99, 103]

std=numpy.std(speed)
print(std)

var=numpy.var(speed)
print(var)

percentile=numpy.percentile(speed,50)
print(percentile)