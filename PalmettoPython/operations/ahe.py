"""
Project: Palmetto

Description: Implementation of Adaptive Histogram Enhancement in OpenCV

Created on 30 Sep 2014

@author:  Jason Forte
@contact: <dev@dustio.com>
"""

import numpy
import cv2
import structure.Operation

class AdaptiveHistogram(structure.Operation):
    '''   
    AdaptiveHistogram(ndarray input_image, dict options)
    
    input_image    -    input image for processing
    options        -    options for the algorithm
    
    Requires:    numpy, cv2, structure.Operation
    
    Description: Performs the Adaptive Histogram Equalisation Algorithm 
    '''
    def __init__(self, input_image=numpy.ndarray, options=dict):
        """ Initiate the Operation Function """
        super(AdaptiveHistogram, self).__init__(input_image, options)
    
    def execute(self):
        """ 
            Execute the Algorithm 
            Overrides Operation.execute
            
            Returns:
            ndarray output_image    -    final output of the operation
        """
        output_image = cv2.equalizeHist(self.input_image)
        return output_image
   
