"""
Project: Palmetto

Adapted from matlab code produced by Prof. John Greene in the Department of Electrical Engineering at the
University of Cape Town.

Description: Implementation of the breeder genetic algorithm. This hill-climbing algorithm takes a random sample of points in 
the solution space of a cost function (here it is restricted to the range 0 to 1). The cost function is evaluated
for each sample point and the results are sorted. The top results are then used to generate new points which replace
the bad results. The effect is that after enough generations the cost function is minimised. This method may not always
find the global minimum but may find a good enough local minimum after a number of re-runs of the function.

Created on 30 Sep 2014

@author:  Jason Forte
@contact: <dev@dustio.com>
"""
import numpy

def fminbga(func, init=[], maxgen=20):
    """ 
        fminbga(func, init, maxgen=20)    --> best_vector, loss
        
        Inputs:
        func        -    reference to a cost function to optimise. func must have an ndarray input
        init        -    initial vector for where to start the search
        maxgen      -    max number of generations before killing the search
        
        Returns:
        best vector - vector of inputs that minimises the cost function
        loss        - the value of the cost function produced from the given best vector
        
        Requires: numpy
        
        Description:
        Runs the Breeder Genetic Algorithm (BGA) on a given cost function. The input cost function must
        map the input variable from the range 0 to 1. This is because this implementation of the BGA only
        finds solutions in the space where the input variable are in the range 0 to 1.
        
        Example:
        # input cost function
        def cost(arr):
            return (arr[0] - 0.333)**2 + (arr[1] - 0.666)**2 + (arr[2] - 0.111)**2
        # call BGA to minimise the cost function with maximum of 40 generations
        best,loss = fminbga(cost, numpy.array([1,1,1]), 40)
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
        
        flow = numpy.mean(f[0, 1:100])
        fhigh = numpy.mean(f[0, 101::])
        
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
        
        for i in range(1, pop):
            # construct an thresh length array of random integer values between 0 and thresh
            R = numpy.random.permutation(int(thresh))
            
            # generate a random number to compare
            rand = numpy.random.rand()
            
            if rand < 0.15:
                # Discrete recombination
                mask = (numpy.random.rand(1,nvars) > 0.5)
                T[:,i] = mask * pool[:,R[0]] + (1 - mask) * pool[:,R[1]]
            else:
                # volume recombination
                rr = -0.25 + 1.5 * numpy.random.rand(1,nvars)
                T[:,i] = rr * pool[:,R[0]] + (1 - rr) * pool[:,R[1]]
            
            # mutate the higher or lower part of the population at a higher or lower rate
            r1 = numpy.floor(nvars * numpy.random.rand())
            if i < 101:
                T[r1,i] += delta * (numpy.random.randn()/1.1)
            else:
                T[r1,i] += delta * (1.1 * numpy.random.randn())
        
        # calculate the value of the cost function for the best input vector    
        loss = func(S[:,0])
        # print the incremental results   
        print("Generation " + str(gen)),
        print("Mutation Rate %0.3f " % delta),
        print("Current Best %0.5f" % loss),
        print(" >> "),
        print(S[:,0])
    
    # return the best vector & cost function
    return S[:,0],loss

''' The following code is used as an example whereby the cost function is minimised 
    It was found that the BGA performs well and finds the minimum after only a few generations
    the final cost function evaluates to 1.60432661654e-07 in
'''

if __name__ == '__main__':
    def cost(arr):
        return (arr[0] - 0.333)**2 + (arr[1] - 0.666)**2 + (arr[2] - 0.111)**2
    import time
    pre = time.time()
    best,loss = fminbga(cost, numpy.array([1,1,1]), 40)
    period = time.time() - pre
    print("Execution Time: %0.4f seconds" % (time.time() - pre))
    print(best)
    print(loss)