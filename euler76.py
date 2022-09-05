"""

Euler 76:  Counting summations

How many different ways can one hundred be written as the sum of at least
two positive integers?

function that uses recursive formula to find number of partitions of
any given positive integer

"""

import numpy as np

def pentagonal_number(i):
    return int(i*(3*i-1)/2)

# find number of partitions of integer n
def partition(n):

    # first partition (i.e. number of partitions of 1 is 1)
    num_partitions=np.array([1])

    for j in range(1,n+1):
        num_partitions=np.append(num_partitions,0)
        for k in range(1,j+1):
            coeff=(-1)**(k+1)
            for t in [pentagonal_number(k),pentagonal_number(-k)]:
                if j-t>=0:
                    num_partitions[j]+=coeff*num_partitions[j-t]
    
    return num_partitions

# subtract 1 because in this problem we do not consider n to be a partition of n
print(partition(100)[-1]-1)
