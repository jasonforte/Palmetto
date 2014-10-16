
import matplotlib.pyplot
import numpy


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
    hist, bins = numpy.histogram(img.flatten(), 256, [0, 256])
    matplotlib.pyplot.hist(img.flatten(), 256, [0, 256], color='r')
    matplotlib.pyplot.xlim([0, 256])
    
    matplotlib.pyplot.title('Histogram of Image')
    matplotlib.pyplot.show()
    return hist, bins

def getNeighbourhood(input_image, x, y, grid):
        '''
        getNeighbourhood(img, x, y, grid) -> subset of image
        
        Get the neighbours based on location x,y for the subset width grid
        even values will be expanded to the next odd value
        '''
        border = int(numpy.ceil((grid - 1) / 2.0))
        return input_image[y - border:y + border + 1, x - border:x + border + 1]
