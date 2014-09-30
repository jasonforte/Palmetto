"""
Project: Palmetto

Description: Test for Adaptive Histogram Enhancement in OpenCV

Created on 30 Sep 2014

@author:  Jason Forte
@contact: <dev@dustio.com>
"""
import unittest
import cv2
import os
import numpy
import operations.ahe

class TestAhe(unittest.TestCase):

    def setUp(self):
        # setup directory
        base = os.path.dirname(__file__)
        dirname = os.path.join(base, 'samples/ahe/')
        
        # load the base image
        self.img = cv2.imread(dirname + 'ahe.png', 0)
        
        # load the target image
        self.target = cv2.imread(dirname + 'ahe_result.png', 0)
    
    def testExecute(self):       
        self.assertEqual(numpy.array_equal(self.target, self.img), False, "Sample Images are the same. Cannot do Comparison") 
        
        # create an operation and store the result
        op = operations.ahe.AdaptiveHistogram(self.img)
        res = op.execute()
        # compare the result to the target
        
        self.assertEqual(numpy.array_equal(self.target, res), True, "Incorrect Output: AHE") 


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testExecute']
    unittest.main()