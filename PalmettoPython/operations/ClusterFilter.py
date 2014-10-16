'''
Created on 13 May 2014

@author: jason
'''

import numpy

import structure.Operation


class Cluster(structure.Operation):
    '''
    classdocs
    '''
    
    NAME = 'Cluster Segment'
    seeds = []
    bin = []
    threshold = 0.02;
    colors = [None, None, None]
    def __init__(self, input_image=numpy.ndarray, options={'seeds':[0, 50, 90], 'colors':[]}):
        '''
        Constructor
        '''
        self.colors = options['colors']
        self.seeds = options['seeds']
        self.image = input_image
    def execute(self):
        '''
        Applies all necessary steps
        '''
        self.modimage = self.image
        old_seed = []
        
        # create old seed to match length on new seed
        for _ in range(0, len(self.seeds)):
            old_seed.append(0)
            self.bin.append([])
        
        # using iteration until the seed movement is below the threshold
        while(self.seedChange(old_seed, self.seeds) > self.threshold):
            self.clearBins()
            for y in range(0, self.shape(self.image)[0]):
                for x in range(0, self.shape(self.image)[1]):
                    self.addToBin(y, x, self.image[y][x])
            old_seed = self.seeds        
            self.seeds = self.getCentroids()  
        self.assignColors()                  
        return self.modimage
        
    def closestPoint(self, value):
        '''
        Find the closes seed by the least of the distances between the values and the all seed points
        '''
        distances = []  # calculate the distance to each seed point
        
        for seedIndex in range(0, len(self.seeds)):
            distances.append(abs(value - self.seeds[seedIndex]))  # append each absolute distance
        
        sort = sorted(distances)[0]
        closestIndex = 0
        
        for seedIndex in range(0, len(self.seeds)):
            if(abs(value - self.seeds[seedIndex]) == sort):
                closestIndex = seedIndex
                break
        
        return closestIndex  # return the closest seedIndex
    
    def addToBin(self, x, y, value):
        '''
        Find the closest seed point and assign the pixel value at (x,y) to the corresponding bin
        '''        
        closest = self.closestPoint(value)  # calculate the distance of the closest seed point
        self.bin[closest].append([x, y, value])
        
    def clearBins(self):
        for i in range(0, len(self.bin)):
            self.bin[i] = []
    
    def getCentroids(self):
        '''
        Each bin can be used to calculate a new seed point
        
        This function can handle any number of bins
        
        The new seed point is the average pixel value for a bin of
        Pixels. I.e if there are 3 bins then there will be a new seed
        point from each bin
        '''
        newCentroids = []
        # iterate through each bin and find the average pixel value
        # this becomes the new seed point
        for binIndex in range(0, len(self.bin)):
            cent = self.getBinCentroid(self.bin[binIndex])  # get the centroid of each bin
            if(cent == None):
                newCentroids.append(self.seeds[binIndex])  # assign same seed if bin length is 0
            else:
                newCentroids.append(cent)  # assign new seed as average
                
        return newCentroids  # return new centroids
    
    def getBinCentroid(self, binItem):
        '''
        Finds the centroid value for a bin of image pixels
        '''
        l = len(binItem)  # get the number of items in the bin
        centroid = 0
        if(l == 0):  # if there are no elements in the bin assign seed value as centroid
            centroid = None
        else:
            total = 0       
            for i in binItem:
                total += i[2]  # get the total of all the pixel values in the bin
            centroid = total / l  # get the average value of the values
        return centroid  # Return centroid or None if bin is length 0
        
    
    def assignColors(self):
        '''
        Assign the value in the seeds to their related bin points
        '''
        self.sortColors()
        for i in range(0, len(self.bin)):
            self.assignBinColor(self.bin[i], self.colors[i])
    
    def setColors(self, colors=[]):
        self.colors = colors
        self.sortColors()
    
    def getColors(self):
        return self.colors
    
    def sortColors(self):
        if (len(self.colors) == 0):
            self.colors = self.seeds
            return
        else:
            tempColors = []
            for i in range(0, len(self.colors)):
                if(self.colors[i] == None):
                    tempColors.append(self.seeds[i])
                else:
                    tempColors.append(self.colors[i])
            self.colors = tempColors
    
    def assignBinColor(self, binItem, color):
        if(len(binItem) == 0): return
        for i in binItem:
            self.modimage[i[0]][i[1]] = color
    
    def seedChange(self, old_seed, new_seed):
        '''
        Calculate the change in seed value
        '''
        total = 0
        for seedIndex in range(0, len(self.seeds)):
            total += abs(old_seed[seedIndex] - new_seed[seedIndex])  # difference between coordinates to find the vector change
        return total
    
    def setThreshold(self, threshold):
        '''
        Setter for threshold
        '''
        self.threshold = threshold 
    
    def shape(self, array):
        return numpy.shape(array)

if __name__ == '__main__':
    
    import cv2
    import structure.Base
    
    sample_image = structure.Base.sample_dir + 'sample.png'
    
    img1 = cv2.imread(sample_image, 0)
    
    op = Cluster(img1, options={'seeds':[10, 50, 90], 'colors':[0, 120, 255]})
    
    cv2.imshow('Resulting Image', op.execute())
    cv2.waitKey(0)
    cv2.destroyAllWindows()
