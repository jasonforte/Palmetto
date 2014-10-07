"""
Project: Palmetto

Description: Convert an image using grayscale normalisation

Created on 7 Oct 2014

@author:  Jason Forte
@contact: <dev@dustio.com>
"""
import cv2
from structure.Operation import Operation

class GrayNorm(Operation):
    '''
    GrayNorm(input_image, options)    ->     result_image
    
    input_image    -    image to be converted
    otions         -    operation options
    
    options={'bottom':0,'top':255}    normalise the gray-scale values between bottom and top
    
    Requires: cv2, structure.Operation
    
    Description:
    This normalisation process finds the minimmum and maximum grayscale value and
    computes each output pixel y = (x - min) * 255 / (max - min)    
    
    '''
    def __init__(self, input_image, options):      
        # call to superclass
        super(GrayNorm, self).__init__(input_image, options)
        
        # Check the options variable has the required options and replace if not
        if not self.options.has_key('top'):
            self.options['top'] = 255
        if not self.options.has_key('bottom'):
            self.options['bottom'] = 0
        
    def execute(self):
        # call the opencv method to perform the min max normalisation
        return cv2.normalize(self.input_image, self.options['bottom'], self.options['top'], norm_type=cv2.NORM_MINMAX)


if __name__ == '__main__':
    # import the os functionality
    import os
    
    # setup route to sample image
    base = os.path.dirname(__file__)
    dirname = os.path.join(base, '../tests/samples/clahe/')
    
    # read in image
    img1 = cv2.imread(dirname + "clahe3.png", 0)
    
    # create operation object for grayscale normalisation
    op = GrayNorm(img1, options={'bottom':0,'top':255})
    
    # retrieve result
    result = op.execute()
    
    # Show output    
    cv2.imshow('Resulting Image', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()