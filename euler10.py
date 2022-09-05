'''Project Euler #10:  Summation of Primes'''

#this was a brute force method, estimated running time:  >5 hours
'''run_total=2 #we exclude the first prime 2, so we include it here
n=3

def div_checker(n,k):
    i=2
    while i<=k:
        if n%i==0:  #if n is evenly divisible, it is not prime so we exit 
            return 0
        else:
            i=i+1
    if i==k+1:
        return n

while n<2000000:
    k=int(n/2) #need only check if n is divisible by integers up to n/2
    x=div_checker(n,k)
    print(x)
    run_total=run_total+x
    n=n+2

print(run_total)'''

#sieve of erastothenes

numbers=list(range(2000000))
running_sum=0

#assign all multiples of 2 in list to False
for index,item in enumerate(numbers):
    if index==2:
        n=2
        while n*index<2000000:
            numbers[n*index]=False
            n=n+1
    else:
        pass
#Set zero-th and first items in list to False
numbers[0]=False
numbers[1]=False

#eliminates all numbers other than primes
for index,item in enumerate(numbers):
    if item==False:
        pass
    else:
        n=2
        running_sum=running_sum+item
        print(running_sum)
        while n*index<2000000:
            numbers[n*index]=False
            n=n+1

#print(numbers)
print(running_sum)
    
