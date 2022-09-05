'''Project Euler #7:  10001st Prime'''

list_num=0
prime_list=[]
n=3

def div_checker(n,k):
    i=2
    while i<=k:
        if n%i==0:  #if n is evenly divisible, it is not prime so we exit 
            return False
        else:
            i=i+1
    if i==k+1:
        return True
    

while list_num!=10000: #excluding 2, so we look for the 10000th prime
    k=int(n/2) #only need to check if n is divisible by integers up to n/2
    prime=div_checker(n,k)
    if prime==True:
        prime_list.append(n)
        list_num=list_num+1
        n=n+1
    else:
        n=n+1

print(prime_list[9999]) #list starts at item 0
    
