"""
Project: Palmetto

Description: Implementation of Adaptive Histogram Enhancement in OpenCV

Created on 30 Sep 2014

@author:  Jason Forte
@contact: <dev@dustio.com>
"""
import cv2
import numpy

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


if __name__ == '__main__':
    
    import functions
    import structure.Base
    
    image_file = structure.Base.sample_dir + 'sample.png'
    
    img = cv2.imread(image_file, 0)    
    
    op = AdaptiveHistogram(img)
    
    final = op.execute()
    functions.createHistogram(final)
    
    cv2.imshow('Initial Image', img)
    cv2.imshow('Result Image', final)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
   
