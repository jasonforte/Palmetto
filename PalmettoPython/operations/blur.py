"""
Project: Palmetto

Description: Adds the following operations

Blur            -    computes a blog averaging filter
GaussianBlur    -    applys a Gaussian filter to the image
MedianFilter    -    applys a median filter to the image

Created on 8 Oct 2014

Updated __updated__

@author:  Jason Forte
@contact: <dev@dustio.com>
"""
import cv2
import numpy

from structure.Operation import Operation

class Blur(Operation):
    '''
    Blur(input_image, options={'ksize': (15,15)}) -> numpy.ndarray
    
    options:
        ksize    -    dimensions of the block for filetering
    
    
    '''
    
    NAME = 'Normalised Block Filter'
    def __init__(self, input_image=numpy.ndarray, options=dict):
        Operation.__init__(self, input_image=input_image, options=options)
        if not self.options.has_key('ksize'):
            self.options['ksize'] = (15, 15)
    
    def execute(self):
        return cv2.blur(self.input_image, self.options['ksize'])


class MedianFilter(Operation):
    '''
    MedianFilter(input_image, options={'ksize': (15,15)}) -> numpy.ndarray
    
    options:
        ksize    -    dimensions of the block for filtering
    
    
    '''
    
    NAME = 'Median Filter'
    def __init__(self, input_image=numpy.ndarray, options=dict):
        Operation.__init__(self, input_image=input_image, options=options)
        if not self.options.has_key('ksize'):
            self.options['ksize'] = (15, 15)
    
    def execute(self):
        return cv2.medianBlur(self.input_image, self.options['ksize'])



class GaussBlur(Operation):
    '''
    GaussianBlur(input_image, options={'window':(x,y), 's_x':3, 's_y': 3})
    
    Applys a gaussian filter with window and sigma values for x and y as s_x and s_y
    respectively
    '''
    NAME = "Gaussian Filter"
    def __init__(self, input_image=numpy.ndarray, options=dict):
        Operation.__init__(self, input_image=input_image, options=options)
        
        if not self.options.has_key('window'):
            self.options['window'] = (15, 15)
        if not self.options.has_key('s_x'):
            self.options['s_x'] = 3
        if not self.options.has_key('s_y'):
            self.options['s_y'] = 3
    
    def execute(self):
        return cv2.GaussianBlur(self.input_image, self.options['window'], self.options['s_x'], self.options['s_y'])
    

if __name__ == '__main__':
    
    import structure.Base
    
    sample_image = structure.Base.sample_dir + 'sample.png'
    
    img = cv2.imread(sample_image, 0)

    op = GaussBlur(img, options={})
    
    # op = Blur(img, options={})
    
    # op = MedianFilter(img, options={'ksize':9})
    
    result = op.execute()
    cv2.imshow('Blur Original', img)
    cv2.imshow('Blur Result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
