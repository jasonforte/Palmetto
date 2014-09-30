"""
Project: Palmetto

Implemented with reference to matlab code by Prof. John Greene Department of Electrical Engineering UCT

Description: Contrast Limited Adaptive Histogram Enhancement Implementation with opencv

Created on 30 Sep 2014

@author:  Jason Forte
@contact: <dev@dustio.com>
"""
import numpy
import numpy.random
import logging

logging.basicConfig(filename='..//program.log', format='%(asctime)s %(message)s', level=logging.DEBUG)


def fminbga(func, init=[], maxgen=1):
    """ 
        fminbga(costfunction, generations)    --> best vector
        
        Inputs:
        func        -    reference to a cost function to optimise. func must have an ndarray input
        init        -    initial vector for where to start the search
        generations -    max number of generations before killing the search
        
        Description:
        Runs the Breeder Genetic Algorithm (BGA) on a given cost function
    """
    
    pop = 200
    nvars = len(init)
    
    # Define the threshold for selection of a new generation
    thresh = round(pop*15.0/100)
    
    best_result = []
    
    delta = 0.1
    
    # create a matrix of random variable as the initial trial solutions
    T = numpy.random.rand(nvars, pop)
    
    # add init as the seed point
    T[:,0] = init
    
    #print(T[0,:])    # print column 1
    
    for gen in range(0,maxgen):
        f = numpy.zeros((pop, 1))
        
        # evaluate the function for entire population
        for j in range(0,pop):
            f[j,:] = - func(T[:,j])
            #print (str(j) + " = " + str(f[j,:]))
        
        f = numpy.transpose(f)
        print(numpy.shape(f))
        #print(f[0, 0:100])
        #print(f[0, 101::])
        
        flow = numpy.mean(f[0, 1:100])
        fhigh = numpy.mean(f[0, 101::])
        print("Low Mean = %0.3f; High Mean = %0.3f" % (flow, fhigh))
        
        if flow > fhigh:
            delta *= 0.95
        else:
            delta *= 1.05
        
        """ Sort the f vector in decending order and apply the changes to the T vector
            This gives the best solution at S[:,0] """
        S = T[:, numpy.argsort(-f[0,:])]
        
        # save best result and accompanying cost function result
        best_result.append([S[:,0], func(S[:,0])])
        
        # now the best results are chosen for the next generation
        pool = S[:,0:thresh]
        
        # the best result is added to the first position
        T[:,0] = S[:,0]
        
        for i in range(0, pop):
            # construct an thresh length array of random integer values between 0 and thresh
            R = numpy.random.permutation(thresh)
            
            # generate a random number to compare
            rand = numpy.random.rand()
            
            if rand < 0.15:
                
        
        print(best_result)

        
    
    

def cost(arr):
    return (arr[0] - 0)**2 + (arr[1] - 0)**2 + (arr[2] - 0)**2

if __name__ == '__main__':
    fminbga(cost, numpy.array([1,1,1]))