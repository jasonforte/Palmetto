#!/usr/bin/env python

"""
Created on 30 Sep 2014

Project: Palmetto

@author: Jason Forte
@contact: <dev@dustio.com>
"""

import numpy

class Operation(object):
    """
    Operation(ndarray input_image, dict options)
    
    This class forms the basis of other operation subclasses. 
    
    input_image    -    Input image used as the image source
    options        -    Dictionary of options {'threshold': 0.4}
    
    """   
    
    # Brief Operation Name & Description
    name = ""
    desctiption = ""
    
    def __init__(self, input_image=numpy.ndarray, options=dict):
        '''
        Accepts the input image and the operation options        
        '''
        self.input_image = input_image
        self.options = options
    
    def execute(self):
        '''
        Execute the operation within this class
        
        This needs to be implemented by subclasses
        '''
        pass

""" if statement to initiate from terminal """
if __name__ == '__main__':
    op = Operation

        