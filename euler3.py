'''Project Euler #3:  Largest Prime Factor'''
import math
factors=[]

d=2
n=600851475143
while d<=int(math.sqrt(600851475143)):
    if n%d==0:
        factors.append(d)
        n=n/d
        d=d+1
    elif n%d!=0:
        d=d+1
#print(factors)

print('The largest prime factor of 600851475143 is:', end=' ')
print(max(factors))
