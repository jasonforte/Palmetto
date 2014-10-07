"""
Project: Palmetto

Description: Perform Upscale and Downscale using the open cv library

Created on 7 Oct 2014

@author:  Jason Forte
@contact: <dev@dustio.com>
"""
import cv2
from structure.Operation import Operation

class Downscale(Operation):
    '''
    Downscale(input_image) -> numpy.ndarray
    
    Description
    Uses the opencv pyramid function to downsample the image
    '''
    def __init__(self, input_image, options=None):      
        # call to superclass
        super(Downscale, self).__init__(input_image, options)
        
    def execute(self):
        return cv2.pyrDown(self.input_image)

class Upscale(Operation):
    '''
    Upscale(input_image) -> numpy.ndarray
    
    Description
    Uses the opencv pyramid function to upsample the image
    '''
    def __init__(self, input_image, options=None):      
        # call to superclass
        super(Upscale, self).__init__(input_image, options)
        
    def execute(self):
        return cv2.pyrUp(self.input_image)


if __name__ == '__main__':
    
    import os
    
    # setup directory
    base = os.path.dirname(__file__)
    dirname = os.path.join(base, '../tests/samples/clahe/')
    
    img1 = cv2.imread(dirname + "clahe3_res.png", 0)
    
    op = Downscale(img1)   
    img1 = op.execute()
    op = Upscale(img1)
    final = op.execute()
    
    cv2.imshow('Resulting Image', final)
    cv2.waitKey(0)
    cv2.destroyAllWindows()