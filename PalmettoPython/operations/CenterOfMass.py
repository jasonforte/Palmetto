"""
Project: 

Description:

Created on 13 Oct 2014

@author:  Jason Forte
@contact: <dev@dustio.com>
"""

from structure.Operation import Operation
import numpy

class CenterOfMass(Operation):
    '''
    CenterOfMass
    
    Gets an image of a certain window dimension
    
    options:
    
    window (x,y)    -    x and y for the image you want from the center
    '''
    def __init__(self, input_image=numpy.ndarray, options=dict):
        Operation.__init__(self, input_image=input_image, options=options)
    
    def execute(self):
        '''
        Find the center of mass and crop the image around it
        '''
        x,y = self.CoM()
        return self.CropWindow(x,y, self.options['window'])
    
    def CoM(self):
        
        # find the shape of the image
        sh = numpy.shape(self.input_image)
        
        xr = 0.0
        yr = 0.0
        
        mass = 0.0
        for i in range(0, sh[0], 16):
            for j in range(0, sh[1], 16):
                '''
                find the moment about the axes
                '''
                xr += self.input_image[i,j] * i
                yr += self.input_image[i,j] * j
                mass += self.input_image[i,j]
        
        x_m = xr/mass
        y_m = yr/mass
        
        return int(x_m), int(y_m)
    
    def CropWindow(self, x, y, window=(64,64)):
        # ensure that two half windows is not bigger than the given window dimentsion
        # even if an odd value is given
        borderY = int(numpy.ceil(window[0]/2.0 - window[0]%2))
        borderX = int(numpy.ceil(window[1]/2.0 - window[1]%2))
        
        return self.input_image[x-borderX:x+borderX, y-borderY: y+borderY]
 
    
if __name__ == '__main__':
    
    import os
    import cv2
    import time
    
    # setup directory
    base = os.path.dirname(__file__)
    dirname = os.path.join(base, '../tests/samples/clahe/')
    
    img1 = cv2.imread(dirname + "clahe7.png", 0)    
    
    op = CenterOfMass(img1, options={'window': (420, 380)})
    
    #op = AdaptiveThreshold(op.execute(), options={'C':0.1,'grid':21})
    
    start_time = time.time()
    
    result = op.execute()
    
    time_taken = time.time() - start_time
    
    print('Took %0.5f seconds' % time_taken)
    
    cv2.imshow('Resulting Image', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()