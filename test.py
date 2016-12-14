#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *
from scipy import *
from scipy import linalg
import string
import sys
print test

def evalf(x):
    f=x[0]**2+exp(x[0])+x[1]**4+x[1]**2-2*x[0]*x[1]+3
    return f

def evalg(x):
    g=array([2*x[0]+exp(x[0])-2*x[1],4*x[1]**3+2*x[1]-2*x[0]])
    return g

def evalh(x):
    H=array([[2+exp(x[0]),-2],[-2,12*x[1]**2+2]])
    return H

def main():
   ### args=sys.argv[1:]
   ### problem=string.atoi(args[0])
   ### method=string.atoi(args[1])
   ### if problem==1:

        x=array([-0.5, -0.5])
        f=evalf(x)
        g=evalg(x)
        H=evalh(x)

        print 'f =', f, '\ng =', g,  '\nH= \n', H

        xi=1e-4
        rho=0.5
        k=0
        epsilon=2e-6
        count=0

        while count < 5:
            z=sqrt(evalg(x)[0]**2+evalg(x)[1]**2)
            if(z<=epsilon):
                break

            t=1
            count2=0
            while evalf(x-t*evalg(x))>=evalf(x)+xi*t*inner(-evalg(x),evalg(x)) and count2 <5:
                print evalg(x)
                t=rho*t
                print 't=',t
                count2+=1
            print t
            x=x-t*evalg(x)
            print 'g=',evalg(x)
            print 'x=', x
            count += 1
            print 'f =', evalf(x)

        ###while f(x+t)<=f(x)+epsilon*t*(-1)*norm(evalg(x))**2:
           ### t=(-1)*norm(evalg(x))**2*t**2/2(f(x+t)-f(x)+norm(evalg(x))**2*t)




if __name__=='__main__':
    main()
