"""
Project: Palmetto

Description: Optimisation of the CLAHE variables for the best output

Created on 6 Oct 2014

@author:  Jason Forte
@contact: <dev@dustio.com>
"""

import cv2
import numpy
import os
import scipy.spatial.distance

import functions.fminbga
import operations.clahe
import structure.Base


vein = []
other = []


sample_image = structure.Base.sample_dir + 'example.png'


# setup directory

img1 = cv2.imread(sample_image, 0)
img1 = cv2.blur(img1, (9, 9))


def difference(img1, img2):
    return scipy.spatial.distance.pdist([img1.flatten(), img2.flatten()], 'cosine')


def actualValues(arr):
    clip = arr[0] * 8000;
    # print (arr),
    # print (" >> "),
    # scale x and y, the matrix dimensions from 1 to 20
    x = int(numpy.floor(arr[1] * 30) + 1)
    y = int(numpy.floor(arr[2] * 30) + 1)
    
    k1 = int(numpy.floor(arr[3] * 30) + 1)
    k2 = int(numpy.floor(arr[4] * 30) + 1)
    
    if x <= 0:
        x = 1
    if y <= 0:
        y = 1
    if k1 <= 0:
        k1 = 1
    if k2 <= 0:
        k2 = 1
            
    print("Clip: %0.6f \t Arr (%1.0f,%1.0f) Blur (%1.0f,%1.0f)" % (clip, x, y, k1, k2))

def hammingCost(arr):
    ''' arr is the threshold value'''
    
    clip = arr[0] * 10000;
    # print (arr),
    # print (" >> "),
    # scale x and y, the matrix dimensions from 1 to 20
    x = int(numpy.floor(arr[1] * 30) + 1)
    y = int(numpy.floor(arr[2] * 30) + 1)
    
    k1 = int(numpy.floor(arr[3] * 30) + 1)
    k2 = int(numpy.floor(arr[4] * 30) + 1)
    
    if x <= 0:
        x = 1
    if y <= 0:
        y = 1
    if k1 <= 0:
        k1 = 1
    if k2 <= 0:
        k2 = 1
    # op = AdaptiveThreshold(img1, options={'C':x, 'grid':y})
    
    img2 = cv2.blur(img1, ksize=(k1, k1))
    
    op = operations.clahe.ContrastLimitedAHE(img2, options={'clip':clip, 'grid': (x, y)})
    
    out = op.execute()
    
    vein_total = numpy.float128(0.0)
    other_total = numpy.float128(0.0)
    
    for i in vein:
        vein_total = vein_total + (out[i] - 0) ** 2
    
    for i in other:
        other_total = other_total + (out[i] - 255) ** 2
    
    J = vein_total + other_total
    
    return J

    
    
def get_sample_points():
    '''
    Gather points that lie on veins or on otherwise
    '''
    # setup directory
    base = os.path.dirname(__file__)
    dirname = os.path.join(base, '../tests/samples/clahe/')
    
    sam_image = cv2.imread(dirname + "clahe3_sample.png")
    
    dim = numpy.shape(img1)
    
    vein = []
    other = []
    
    for i in range(0, dim[0]):
        for j in range(0, dim[1]):
            if (sam_image[i, j] == yellow).all():
                vein.append((i, j))
            if (sam_image[i, j] == red).all():
                other.append((i, j))
    
    return vein, other
    

if __name__ == '__main__':
    
    
    sample_image = structure.Base.sample_dir + 'example.png'
    
    yellow = [0, 255, 255]
    red = [0, 0, 255]
    
    vein, other = get_sample_points()
    
    print('Sample Points Captured...')
    
    img1 = cv2.imread(sample_image, 0)
        
    # print(hammingCost([0.5, 2, 2]))
    # img2 = cv2.imread(dirname + "clahe9_opt_ideal.png", 0)
    
    # 0.77924757,  0.21278735,  0.22703163
    # Generation 5 Mutation Rate 0.081  Current Best 298634989.00000  >>  [ 0.39776096  1.00695604  0.35260915  0.46077316  0.13693767]
    # Generation 9 Mutation Rate 0.099  Current Best 297918299.00000  >>  [ 0.51756102  1.46934224  0.34191395  0.46032458  0.16499233]
    # 0.63496855,  1.05389801,  0.36302749,  0.3852121,   0.13553139   =  298907411.00000
    # Generation 9 Mutation Rate 0.121  Current Best 297411673.00000  >>  [ 0.79357104  1.82521635  0.35354824  0.5206348   0.14233059]
    # Generation 9 Mutation Rate 0.099  Current Best 296965414.00000  >>  [ 0.2677742   2.04354938  0.3576068   0.52488928  0.14639264]
    
    
    # best, loss = functions.fminbga.fminbga(hammingCost, numpy.array([ 0.2677742,   2.04354938,  0.3576068,   0.52488928,  0.14639264]), 10)
    best, loss = functions.fminbga.fminbga(hammingCost, numpy.random.rand(5), 20)
    # best = scipy.optimize.fmin(func=hammingCost, x0=[0.5, 0.5, 0.5, 0.5, 0.5])
    
    # cv2.imshow('Resulting Image', img1)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    # best = numpy.array([0.2677742,   2.04354938,  0.3576068,   0.52488928,  0.14639264])
    
    print("Result")
    
    print(hammingCost(numpy.array([0, 0, 0, 0, 0])))
    
    
    print(best),
    print(" >> "),
    print(actualValues(best))

    
