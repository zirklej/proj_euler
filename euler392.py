# -*- coding: utf-8 -*-
"""
Created on Tue Aug 06 19:34:48 2019

@author: joelz

Project Euler 392:
    
    https://projecteuler.net/problem=392
    
    solution:
    
    write equation for the area of the rectangles in terms of the x_i,
    then take all the first partial derivatives and equate to zero.  use a nonlinear
    solver to find the solution.  initial guess for solver can be equidistant 
    points.
    
"""

import numpy as np
import scipy.optimize
from matplotlib import pyplot as plt
import time

start=time.time()

# number of x points
n=200

def partials(x):
    # array to hold all first partial derivatives
    func=np.zeros(n)
    
    func[0]=np.sqrt(1-x[0]**2)-(x[0]*x[1])-1+2*(x[0]**2)
    
    for i in range(1,n-1):
        func[i]=np.sqrt(1-x[i]**2)*np.sqrt(1-x[i-1]**2)-(x[i]*x[i+1])-1+2*(x[i]**2)
        
    func[n-1]=np.sqrt(1-x[n-1]**2)*np.sqrt(1-x[n-2]**2)-x[n-1]-1+2*(x[n-1]**2)
    
    return func

# equidistant points for initial guess
x0=np.linspace(0.,1,n+2)
x0=x0[1:-1]

# nonlinear solver
xval=scipy.optimize.newton_krylov(partials,x0,x_tol=1e-14)

end=time.time()

def area(x):
    # calculate area of all rectangles in first quadrant
    a=x[0]
    
    for i in range(1,n):
        a+=(x[i]-x[i-1])*np.sqrt(1-x[i-1]**2)
        
    a+=(1-x[n-1])*np.sqrt(1-x[n-1]**2)
    
    return a
    
print(4*area(xval))
print(end-start)
