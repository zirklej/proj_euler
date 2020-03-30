'''Project Euler #2:  Even Fibonacci Numbers'''

import numpy as np
import time

start=time.time()

# only need to store 3 fibonacci numbers at a time
fib=np.zeros(3)

# initialize first two fibonacci numbers
fib[0]=1
fib[1]=2

# the sum of even fibonacci numbers
sum=2 

def fibo(sum):  
    # generate Fibonacci numbers and sum the even ones
    fib[2]=fib[0]+fib[1]
    
    if fib[2]<4000000:
        
        if int(fib[2])%2==0:
            sum+=fib[2]
            
            print(sum) # last number printed is the total sum
        
        fib[0]=fib[1]
        fib[1]=fib[2]
        
        fibo(sum)
    

fibo(sum)

end=time.time()
print(end-start)


