'''
Created on 23 Sep 2014
A module to compute the contrast limited adaptive histogram enhancement method
@author: jason
'''
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import time



def histogram_example(img="013-hand-dorsum-v-880.png"):
    """ Get the image """
    img = cv2.imread(img, 0);
    
    """ Create a histogram of the flattened image """
    hist,bins = np.histogram(img.flatten(), 256,[0,256])
    
    """ Calculate the Cumulateive Distribution Function """
    cdf = hist.cumsum()
    
    """ Normalise the CDF """
    cdf_normalised = cdf * hist.max() / cdf.max()
    
    """ Plot the Resulting Graph """
    plt.plot(cdf_normalised, color='b')
    plt.hist(img.flatten(), 256, [0,256], color = 'r')
    plt.xlim([0,256])
    plt.legend(('cdf', 'histogram'), loc='upper left')
    plt.title('Histogram & CDF of Vein Image')
    plt.show()
    
    """ Create a mask where the cdf = 0 """
    cdf_m = np.ma.masked_equal(cdf, 0)
    
    """ Perform Contrast Spreading """
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max()-cdf_m.min())
    
    """ Return array with masked data set to 0 """
    cdf = np.ma.filled(cdf_m, 0)
    
    """ cdf acts as a lookup table that maps the input image to a new output image """
    img2 = cdf[img]
    
    """ Write the output of the process to a file """
    cv2.imwrite('result.png', img2)
    
    """ Create a histogram of the flattened image """
    hist2,bins2 = np.histogram(img.flatten(), 256,[0,256])
    
    """ Calculate the Cumulateive Distribution Function """
    cdf2 = hist2.cumsum()
    
    """ Normalise the CDF """
    cdf2_normalised = cdf2 * hist2.max() / cdf2.max()
    
    """ Plot the Adapted image graphs """
    plt.figure(2)
    plt.plot(cdf2_normalised, color='b')
    plt.hist(img2.flatten(), 256, [0,256], color = 'r')
    plt.xlim([0,256])
    plt.legend(('cdf', 'histogram'), loc='upper left')
    plt.title('Adjusted Histogram & CDF of Vein Image')
    plt.show()

def histogram_equalisation(img='013-hand-dorsum-v-880',output='result'):
    """ Load image """
    img = cv2.imread(img + ".png",0)
    
    """ Perform Histogram Equilisation """
    equ = cv2.equalizeHist(img)
    
    """ Combine Results Side by Side """
    #res = np.hstack((img,equ))
    
    cv2.imwrite(output + ".png", equ)
    
def perform_clahe(img='013-hand-dorsum-v-880',output='result',clip=2.0):
    """ Load image """
    img = cv2.imread(img + ".png",0)
    
    cv2.imwrite(output + "_orig.png", img)
    
    #img = cv2.GaussianBlur(img, ksize=(15,15), sigmaX=0.4)
    """ Create CLAHE object """
    clahe = cv2.createCLAHE(clipLimit=clip, tileGridSize=(8,8))
    
    """ Apply to the image """
    cl1 = clahe.apply(img)
    
    cv2.imwrite(output + ".png", cl1)

def apply_threshold():
    pass
      

""" Call the main method if initiated individually """
if __name__ == '__main__':
    start_time = time.time()
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, '../../tests/samples/ahe')
    
    img = cv2.imread(filename + ".png",0)
    
    """ Perform Histogram Equilisation """
    equ = cv2.equalizeHist(img)
    
    """ Combine Results Side by Side """
    #res = np.hstack((img,equ))
    
    cv2.imwrite(filename + "ahe_result.png", equ)
    
    #histogram_example()
    histogram_equalisation(img= filename + "ahe", output= filename + "ahe_result")
    #histogram_equalisation("Tests//clahe_1", "Tests//ahe_1_res")
    #perform_clahe('Tests//clahe_1', output='Tests//clahe_3_res', clip=10.0)
    perform_time = time.time() - start_time
    print("Execution Time: %0.3f seconds" % perform_time)



