"""
Project: Palmetto

Description: Optimisation of the CLAHE variables for the best output

Created on 6 Oct 2014

@author:  Jason Forte
@contact: <dev@dustio.com>
"""

import cv2
import os
import functions.fminbga
import scipy.spatial.distance
import operations.clahe
import numpy

def difference(img1, img2):
    return scipy.spatial.distance.pdist([img1.flatten(), img2.flatten()], 'euclidean')

def actualValues(arr):
    clip = arr[0] * 5000;
    #print (arr),
    #print (" >> "),
    # scale x and y, the matrix dimensions from 1 to 20
    x = int(numpy.floor(arr[1] * 20) + 1)
    y = int(numpy.floor(arr[2] * 20) + 1)
    
    if x <= 0:
        x = 1
    if y <= 0:
        y = 1
    
    print("Clip: %0.6f \t Arr (%1.0f,%1.0f)" % (clip,x,y))

def hammingCost(arr):
    ''' arr is in the form of [clip, x, y] '''
    #scale clip between 0 and 5000
    clip = arr[0] * 5000;
    #print (arr),
    #print (" >> "),
    # scale x and y, the matrix dimensions from 1 to 20
    x = int(numpy.floor(arr[1] * 20) + 1)
    y = int(numpy.floor(arr[2] * 20) + 1)
    
    if x <= 0:
        x = 1
    if y <= 0:
        y = 1
    
    #print ([clip, x, y]),
    
    # get the clahe resulting image
    op = operations.clahe.ContrastLimitedAHE(img1, options={'clip':clip,'grid':(x,y)}) 
    
    J = difference(op.execute(), img2)
    
    #print(J)
    
    # return the hamming distance between the result and the ideal version
    return J
    

if __name__ == '__main__':
    # setup directory
    base = os.path.dirname(__file__)
    dirname = os.path.join(base, '../tests/samples/clahe/')
    
    img1 = cv2.imread(dirname + "clahe9.png", 0)
    
    img2 = cv2.imread(dirname + "clahe9_ideal.png", 0)
    
    best,loss = functions.fminbga.fminbga(hammingCost, numpy.array([0.00105956,  0.53489601,  0.3836524]), 10)
    
    print(best),
    print(" >> "),        
    print(actualValues(best))

    