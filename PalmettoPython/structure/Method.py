'''
Method.py

Project: Palmetto

Description: This class extends the functionality of list to provide a
storage mechanism for a group of operations. Operations get appended to the
Method to form a operation chain. This method can the be applied to an image
by calling the applyTo() function.

An example is found below

Created on 12 Oct 2014

@author: Jason Forte
@contact: <dev@dustio.com>
'''

import structure.Base

class Method(list):
    '''
    Method(name)
    
    This class contains a list of operations that can be run on an image.
    The applyTo function systematically applies operations to an image and
    returns the final result.
    
    Requires: structure.Base, structure.Operation
    '''
    def __init__(self, name='Unnamed', *args, **kwargs):
        '''
        Override to parent __init__ method
        '''
        list.__init__(self, *args, **kwargs)
        # list element to store the operation options for each section
        self.options = []
        
        # if name is provided then store it
        self.name = name
    
    def append(self, function, options=dict):
        '''
        append(self, function, options=dict)
        
        Description:
        Append an operation to this method
        Store the opeartion and the options for that opperation
        '''
        list.append(self, function)
        self.options.append(options)
    
    def applyTo(self, input_image):
        '''
        Apply the operations to the image.
        
        Description:
        Because all operations are children of structure.Operation they all
        have the execute operation which returns the result of an operation.
        These methods are used to call each operation in the list. 
        '''
        # loop through the operations in the list and apply them to the image
       
        for sequence in range(0, len(self)):
            # declare the opearation object as a function with the input image and the options
            # as the parameters
            op = self[sequence](input_image, options=self.options[sequence])
            
            # store the image result for the next operation
            result_image = op.execute()
        
        return result_image
    
    def __str__(self, *args, **kwargs):
        '''
        Overrides the __str__ method to provide useful print information for this
        method. This function calls to the Operation.NAME constant. 
        '''
        # initail output
        output = 'Operation Stack - ' + self.name + '\n'
        
        for i in range(len(self)):
            output += ' - ' + str(self[i].NAME) + ' --> ' + str(self.options[i]) + '\n' 
        
        return output

if __name__ == '__main__':
    '''
    Example of the usage of this class to hold operation chains.
    
    This example adds two operations (GrayNorm, Sauvola) to a method called
    'Option 1'. The operations are then run in succession using the applyTo
    operation
    '''
    import cv2
    import operations.Sauvola
    import operations.graynorm
    
    # select the sample image to transform
    sample_file = structure.Base.sample_dir + 'sauvola/clahe8.png'
    
    # read in the image
    img = cv2.imread(sample_file, 0)
    
    if img == None:
        exit('Cannot Find Image at ' + sample_file)
    
    # add operations to this method
    m1 = Method('Option 1')
    
    m1.append(operations.graynorm.GrayNorm, options={'top':255, 'bottom':0})
    m1.append(operations.Sauvola.Sauvola, options={'window':(69, 13), 'k':0.01})
    
    # show the results of printing the operation stack
    print(m1)
    
    # show output of the process
    cv2.imshow('Output of CLAHE', m1.applyTo(img))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
