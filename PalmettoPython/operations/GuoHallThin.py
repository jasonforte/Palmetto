"""
Sauvola.py

Project: Palmetto

Description: Implements the GuoHall Thinning Algorithm via a compiled program GuoHallThin

Created on 11 Oct 2014

@author:  Jason Forte
@contact: <dev@dustio.com>
"""
import cv2
import numpy
import subprocess

import structure.Base

from structure.Operation import Operation


class GuoHallThinning(Operation):
    '''
    GuoHallThinning Operation
    
    '''
    # Decribe the Operation
    NAME = 'GuoHall Thinning Operation'
    
    def __init__(self, input_image=numpy.ndarray, options=dict):
        '''
        Sauvola(input_image, options) -> ndarray
        
        options:
        widow  (x,y) -    window of the kernel
        k            -    multiplaction factor for the Sauvola method
        '''
        Operation.__init__(self, input_image=input_image, options=options)
        
        self.operation_name = 'GuoHall Thinning Method'
        
        # save the image to a know location
                
        cv2.imwrite(structure.Base.sample_dir + 'source.png', input_image)   
        
    
    def execute(self):
        '''
        This script uses subprocess to compute the thinned version of an image
        
        '''
        prog_location = structure.Base.base_dir + 'operations/./GuoHallThin'
        
        # tries to call the Thinning program which outputs to result.png
        try:
            # supress the standard error
            subprocess.check_output([prog_location, structure.Base.sample_dir + 'source.png',
                                         structure.Base.sample_dir + 'result.png'], stderr=False)
            # read the image output
            output = cv2.imread(structure.Base.sample_dir + 'result.png', 0)
        except subprocess.CalledProcessError:
            print('Error using Sauvola Method')
        
        return output
    
    def __str__(self):
        '''
        Returns string when printing the operation
        '''
        return self.NAME + ' --> ' + self.options.__str__()        


if __name__ == '__main__':
    '''
    Example of the use of the Thining method to enhance an image.
    '''
    
    # select the sample image to transform
    sample_file = structure.Base.sample_dir + 'guohall.png'
    
    img = cv2.imread(sample_file, 0)
    
    op = GuoHallThinning(img, options={})
    
    result = op.execute()
    
    # output the image in a window
    cv2.imshow("Original", img)
    cv2.imshow("GuoHall Thinnning Output", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
