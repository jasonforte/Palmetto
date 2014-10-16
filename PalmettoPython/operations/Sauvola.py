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

import structure.Base

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
    # Decribe the Operation
    NAME = 'Sauvola Operation'
    
    def __init__(self, input_image=numpy.ndarray, options=dict):
        '''
        Sauvola(input_image, options) -> ndarray
        
        options:
        widow  (x,y) -    window of the kernel
        k            -    multiplaction factor for the Sauvola method
        '''
        Operation.__init__(self, input_image=input_image, options=options)
        
        self.operation_name = 'Sauvola Method'
        
        # Check existence of values
        if not self.options.has_key('window'):
            options['window'] = (15, 15)
        if not self.options.has_key('k'):
            options['k'] = 0.03
        
        # save the image to a know location
        self.dirname = structure.Base.sample_dir
                
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
        prog_location = structure.Base.base_dir + 'operations/./Sauvola'
        
        # tries to call the Sauvola program which outputs to result.png
        try:
            # supress the standard error
            subprocess.check_output([prog_location, 's', '-x ' + str(self.options['window'][0]),
                                      '-y ' + str(self.options['window'][0]),
                                       '-k ' + str(self.options['k']),
                                        self.dirname + 'source.png',
                                         self.dirname + 'result.png'], stderr=False)
            # read the image output
            output = cv2.imread(self.dirname + 'result.png', 0)
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
    Example of the use of the Sauvola method to enhance an image.
    '''
    # select the sample image to transform
    sample_file = structure.Base.sample_dir + 'sample.png'
    
    img = cv2.imread(sample_file, 0)

    op = Sauvola(img, options={'window':(69, 13), 'k':0.01})

    print(op)
    
    # output the image in a window
    cv2.imshow("Sauvola Output", op.execute())
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
