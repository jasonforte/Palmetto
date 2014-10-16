#!/usr/bin/env python
"""
Project: Palmetto

Description: Computes the Binary Inverse of the given image

Created on 15 Oct 2014

@author:  Jason Forte
@contact: <dev@dustio.com>
"""
import cv2
import numpy

import structure.Base
from structure.Operation import Operation


class Invert(Operation):
    '''
    Invert the color scheme of the image
    
    0       ->   255
    255     ->   0
    '''
    
    NAME = "Binary Invert"
    def __init__(self, input_image=numpy.ndarray, options=dict):
        Operation.__init__(self, input_image=input_image, options=options)
    
    def execute(self):
        return numpy.max(self.input_image) - self.input_image



if __name__ == '__main__':
    # select the sample image to transform
    
    sample_file = structure.Base.sample_dir + 'sample.png'
    
    img = cv2.imread(sample_file, 0)
    
    op = Invert(img, options={})
    
    cv2.imshow('Output of Invert', op.execute())
    cv2.waitKey(0)
    cv2.destroyAllWindows()