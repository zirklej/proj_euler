# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 10:51:33 2018

@author: joelz

project euler 12:  find the first triangular number to have over 500 divisors

the n-th triangle number is the sum of the first n positive integers.

the n-th triangle number is n(n+1)/2.  note that n and n+1 are coprime, 
hence we can count their divisors instead of generating a triangle number
and trying to count its divisors.

"""

from numpy import *

def divisors(i):
    upper_check=int(floor(i/2))  # only check divisors up to i/2
    div_i=array([])  # array to hold divisors
    for j in range(1,upper_check+1):
        if i%j==0:
            div_i=append(div_i,j)
    div_i=append(div_i,i)  # count i as a divisor of itself
    return div_i

div_num=0
i=1
               
div_i=divisors(i)
while div_num<=500:
    if (i+1)%2==0:
        div_i1=divisors((i+1)/2)
    else:
        div_i1=divisors(i+1)
    temp=div_i1
    div_num=len(div_i)*len(div_i1)-1
    div_i=temp
    i+=1
    
print(div_num,i*(i-1)/2)