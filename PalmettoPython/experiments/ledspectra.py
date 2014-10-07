'''
Created on 17 Sep 2014

@author: jason
'''
import matplotlib.pyplot
import numpy
import matplotlib.mlab
from matplotlib import pyplot

def createspecrum(mean, sigma):
    X = numpy.linspace(760, 1100, 100)
    Y = matplotlib.mlab.normpdf(X, mean, sigma);
    top = numpy.max(Y)
    return X, Y/top


def main():
    A1 = createspecrum(850, numpy.sqrt(500))
    A2 = createspecrum(880, numpy.sqrt(500))
    A3 = createspecrum(940, numpy.sqrt(480))
    A4 = A1[1] + A2[1] + A3[1]
    A4 = A4/numpy.max(A4)
    matplotlib.pyplot.subplot(2, 1, 1)
    matplotlib.pyplot.plot(A1[0], A1[1]),
    matplotlib.pyplot.plot(A2[0], A2[1]),
    matplotlib.pyplot.plot(A3[0], A3[1])
    matplotlib.pyplot.title('Individual Spectra Approximations for IR LEDs')
    
    matplotlib.pyplot.subplot(2, 1, 2)
    matplotlib.pyplot.plot(A3[0], A4, 'k')
    matplotlib.pyplot.title('Normalised Spectra Distribution of All LED Wavelengths')
    
    pyplot.show()

if __name__ == '__main__':
    main()