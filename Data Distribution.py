
import numpy
import matplotlib.pyplot as plt

bigData=numpy.random.uniform(0,5,250)
bigData=numpy.random.normal(5.0,1.0,1000)
print(bigData)

'''
plt.hist(bigData,5)
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

'''