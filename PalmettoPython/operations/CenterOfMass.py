"""
Project: Palmetto

Description: This script contains the functionality to compute the center of mass and crop
operations

Created on 13 Oct 2014

@author:  Jason Forte
@contact: <dev@dustio.com>
"""

import numpy

from structure.Operation import Operation


class CenterOfMass(Operation):
    '''
    CenterOfMass
    
    Gets an image of a certain window dimension
    
    options:
    
    window (x,y)    -    x and y for the image you want from the center
    '''
    
    NAME = 'Center of Mass & Cropping'
    def __init__(self, input_image=numpy.ndarray, options=dict):
        Operation.__init__(self, input_image=input_image, options=options)
    
    
    def execute(self):
        '''
        Find the center of mass and crop the image around it
        
        If the center is not close enough to the center then None is returned
        '''
        cent = self.CoM()
        if cent == None:
            self.x, self.y = [0, 0]
            return self.input_image
        
        self.x, self.y = cent
        
        # self.printDot()
        
        return self.CropWindow(self.x, self.y, self.options['window'])
    
    def printDot(self):
        try:
            self.input_image[self.x + 1, self.y] = 255
            self.input_image[self.x - 1, self.y] = 255
            self.input_image[self.x, self.y + 1] = 255
            self.input_image[self.x, self.y - 1] = 255
        except IndexError:
            pass
    
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
                xr += self.input_image[i, j] * i
                yr += self.input_image[i, j] * j
                mass += self.input_image[i, j]
        
        if mass == 0.0:
            return None
        x_m = xr / mass
        y_m = yr / mass
        
        return int(x_m), int(y_m)
    
    def CropWindow(self, x, y, window=(64, 64)):
        # ensure that two half windows is not bigger than the given window dimension
        # even if an odd value is given
        
        borderY = int(numpy.ceil(window[0] / 2.0 - window[0] % 2))
        borderX = int(numpy.ceil(window[1] / 2.0 - window[1] % 2))
        
        dim = numpy.shape(self.input_image)
        
        # print ((borderX, borderY, dim))
        
        top_x = x + borderX
        top_y = y + borderY
        bottom_x = x - borderX
        bottom_y = y - borderY
        
#         print((x, y))
        
#         print((bottom_x, top_x, bottom_y, top_y))
        
        if x < borderX:
            bottom_x = 0
            top_x = borderX * 2
         
        if y < borderY:
            bottom_y = 0
            top_y = borderY * 2
         
        if x > dim[0] - borderX:
            bottom_x = dim[0] - borderX * 2
            top_x = dim[0]
         
        if y > dim[1] - borderY:
            bottom_y = dim[1] - borderY * 2
            top_y = dim[1]
#         print('Converted -> '),
#         print((bottom_x, top_x, bottom_y, top_y))
        
        return self.input_image[bottom_x:top_x, bottom_y:top_y]
    
if __name__ == '__main__':
    
    import cv2
    import structure.Base
    
    sample_image = structure.Base.sample_dir + 'sample.png'
    
    img1 = cv2.imread(sample_image, 0)    
    
    op = CenterOfMass(img1, options={'window': (420, 380)})

    result = op.execute()
    
    cv2.imshow('Resulting Image', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
