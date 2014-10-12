"""
Sauvola.py

Project: Palmetto

Description: Implementation of the Sauvola thresholding method. This class forms a wrapper to an external
Sauvola program. This class uses subprocess to access the functionality.

Reference:
Christian Wolf , Jean-Michel Jolion and Francoise Chassaing. Text Localization, 
Enhancement and Binarization in Multimedia Documents Proceedings of the International Conference 
on Pattern Recognition (ICPR), volume 4, pages 1037-1040,
IEEE Computer Society. August 11th-15th, 2002, Quebec City, Canada. 4 pages.

Created on 11 Oct 2014

@author:  Jason Forte
@contact: <dev@dustio.com>
"""
import cv2
import numpy     
import os
import subprocess
from structure.Operation import Operation

class Sauvola(Operation):
    ''' 
    Description:  
    Performs the sauvola threshold enhancement algorithm. This operation is 
    actually a wrapper class for the Sauvola program
    
    With Reference to: 
    
    @InProceedings{WolfICPR2002V,
      Author         = {C. Wolf and J.-M. Jolion and F. Chassaing},
      Title          = {Text {L}ocalization, {E}nhancement and {B}inarization in {M}ultimedia {D}ocuments},
      BookTitle      = {Proceedings of the {I}nternational {C}onference on {P}attern {R}ecognition},
      Volume         = {2},
      Pages          = {1037-1040},
      year           = 2002,
    }
    
    Requires: cv2, os, numpy, subprocess structure.Operation
    
    '''
    
    def __init__(self, input_image=numpy.ndarray, options=dict):
        '''
        Sauvola(input_image, options) -> ndarray
        
        options:
        widow  (x,y) -    window of the kernel
        k            -    multiplaction factor for the Sauvola method
        '''
        Operation.__init__(self, input_image=input_image, options=options)
        
        # Check existence of values
        if not self.options.has_key('window'):
            options['window'] = (15, 15)
        if not self.options.has_key('k'):
            options['k'] = 0.03
        
        # save the image to a know location
        self.base = os.path.dirname(__file__)
        self.dirname = os.path.join(self.base, '../tests/samples/sauvola/')
                
        cv2.imwrite(self.dirname + 'source.png', input_image)   
        
        self.k = options['k']
        
    
    def execute(self):
        '''
        The Sauvola Method for Enhancement hs not been implemented in 
        opencv. A module was found that performs the operation in C++
        this result is much faster than an implementation in python.
        
        Execute uses subprocess to call the program with the input
        image as the argument. The output image is presented in a
        an output file which is read and then returned
        
        '''
        
        # tries to call the Sauvola program which outputs to result.png
        try:
            # supress the standard error
            subprocess.check_output(['./Sauvola', 's', '-x ' + str(self.options['window'][0]),
                                      '-y ' + str(self.options['window'][0]),
                                       '-k ' + str(self.options['k']),
                                        self.dirname + 'source.png',
                                         self.dirname + 'result.png'], stderr=False)
            # read the image output
            output = cv2.imread(self.dirname + 'result.png', 0)
        except subprocess.CalledProcessError as err:
            print('Error using Sauvola Method:\n' + str(err.message))
        
        return output       


if __name__ == '__main__':
    '''
    Example of the use of the Sauvola method to enhance an image.
    '''
    base = os.path.dirname(__file__)
    dirname = os.path.join(base, '../tests/samples/sauvola/')
    
    img = cv2.imread(dirname + 'sample.png', 0)
    
    op = Sauvola(cv2.GaussianBlur(img, (5, 5), 3), options={'window':(69, 13), 'k':0.01})
    
    # output the image in a window
    cv2.imshow("Sauvola Output", op.execute())
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
