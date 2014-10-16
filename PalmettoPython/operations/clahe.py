"""
Project: Palmetto

Description: Contrast Limited Adaptive Histogram Enhancement Implementation with opencv

Created on 30 Sep 2014

@author:  Jason Forte
@contact: <dev@dustio.com>
"""
import cv2

import structure.Operation


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
    
    NAME = 'Contrast Limited Adaptive Histogram Enhancement'

    def __init__(self, input_image, options=None):      
        # call to superclass
        super(ContrastLimitedAHE, self).__init__(input_image, options)
        
        # Check the options variable has the required options and replace if not
        if not self.options.has_key('clip'):
            self.options['clip'] = 2.0
        if not self.options.has_key('grid'):
            self.options['grid'] = (15, 15)

    
    def execute(self):
        """ execute() --> ndarray """
        
        # Create CLAHE object with the clip and tileGridSize implemented from the options
        try:
            clahe = cv2.createCLAHE(clipLimit=self.options['clip'], tileGridSize=self.options['grid'])
            # clahe = cv2.createCLAHE(clipLimit=2000.0, tileGridSize=(8,8))
        except Exception:
            return None
        
        """ Apply to the image """
        return clahe.apply(self.input_image)
    

if __name__ == '__main__':
    
    import structure.Base
    
    
    sample_image = structure.Base.sample_dir + 'sample.png'
    
    img = cv2.imread(sample_image, 0)

    op = ContrastLimitedAHE(img, options={'clip':12.45, 'grid':(12, 8)})
    
    import functions
    
    result = op.execute()
    
    # display resulting histogram
    functions.createHistogram(result)
    
    cv2.imshow('Output of CLAHE', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

