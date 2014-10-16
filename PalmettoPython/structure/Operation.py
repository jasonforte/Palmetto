#!/usr/bin/env python
"""
Project: Palmetto

Description: Implementation of Operation Class

Created on 30 Sep 2014

@author:  Jason Forte
@contact: <dev@dustio.com>
"""

import numpy

class Operation(object):
    """
    Operation(ndarray input_image, dict options)

    input_image    -    Input image used as the image source
    options        -    Dictionary of options {'threshold': 0.4}

    Requires:    numpy
    
    Description: This class forms the basis of other operation subclasses. 
    """   
    # Brief Operation Name & Description
    NAME = "Unnamed"
    DESC = "No Description"
    
    def __init__(self, input_image=numpy.ndarray, options=dict):
        '''
        Accepts the input image and the operation options        
        '''
        self.input_image = input_image
        self.options = options
    
    def execute(self):
        '''
        execute() -> unimplemented
        '''
        return self.input_image

""" if statement to initiate from terminal """
if __name__ == '__main__':
    pass

        