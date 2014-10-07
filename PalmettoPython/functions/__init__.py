
import numpy
import matplotlib.pyplot

def createHistogram(img, figure=None):
    """
    createHistogram(ndarray img, int bins, matplotlib.figure.Figure figure) --> hist, bins
    
    Inputs:
    img         -    image to find histogram
    figure      -    where to place the figure
    
    Returns:
    hist        -    (tuple)  histogram element
    bins        -    (int)    number of bins used
    
    Requires:    numpy, matplotlib.pyplot
    
    Description:
    Displays a histogram of the image gray-scale values
    
    """
    if figure == None:
        matplotlib.pyplot.figure()
    
    """ Create a histogram of the flattened image """
    hist,bins = numpy.histogram(img.flatten(), 256,[0,256])
    matplotlib.pyplot.hist(img.flatten(), 256, [0,256], color = 'r')
    matplotlib.pyplot.xlim([0,256])
    
    matplotlib.pyplot.title('Histogram of Image')
    matplotlib.pyplot.show()
    return hist,bins
