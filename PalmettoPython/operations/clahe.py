"""
Project: Palmetto

Description: Contrast Limited Adaptive Histogram Enhancement Implementation with opencv

Created on 30 Sep 2014

@author:  Jason Forte
@contact: <dev@dustio.com>
"""
import os
import structure.Operation
import cv2
import logging
import functions

class ContrastLimitedAHE(structure.Operation):
    '''
    ContrastLimitedAHE(ndarray input_image, dict options)
    
    Inputs:
    input_image    -    image to transform
    options        -    options for the enhancement
    
    options = {'clip': 2.0, 'grid':(15,15)}
    
    Requires:    os, logging, cv2, structure.Operation
    
    Description:
    Performs Contract Limited Adaptive Histogram Enhancement
    
    '''

    def __init__(self, input_image, options=None):      
        # call to superclass
        super(ContrastLimitedAHE, self).__init__(input_image, options)
        
        # Check the options variable has the required options and replace if not
        if not self.options.has_key('clip'):
            self.options['clip'] = 2.0
        if not self.options.has_key('grid'):
            self.options['grid'] = (15,15)

    
    def execute(self):
        """ execute() --> ndarray """
        
        # Create CLAHE object with the clip and tileGridSize implemented from the options
        try:
            clahe = cv2.createCLAHE(clipLimit=self.options['clip'], tileGridSize=self.options['grid'])
            #clahe = cv2.createCLAHE(clipLimit=2000.0, tileGridSize=(8,8))
        except Exception as err:
            logging.warn("Couldn't create CLAHE with " + str(self.options) + "\n" + str(err))
            return None
        
        """ Apply to the image """
        return clahe.apply(self.input_image)
    

if __name__ == '__main__':
    # setup directory
    base = os.path.dirname(__file__)
    dirname = os.path.join(base, '../tests/samples/clahe/')
    
    img = cv2.imread(dirname + 'clahe.png', 0)
    
    # Create a histogram of the initial image
    functions.createHistogram(img)
    
    op = ContrastLimitedAHE(img, options={'clip':2000.0,'grid':(8,8)})
    
    # Create histogram of the resulting image
    functions.createHistogram(op)
    
    cv2.imshow('Output of CLAHE', op.execute())
    cv2.waitKey(0)
    cv2.destroyAllWindows()

