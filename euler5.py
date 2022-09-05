'''Project Euler #5:  Smallest Multiple'''

d=40
fin=False

def div_checker(d,i):
    if i==20 and d%20==0:
        print(d)
        return True
    elif d%i!=0:
        return False
    elif d%i==0:
        return div_checker(d,i+1)

while fin==False:
    fin=div_checker(d,3)
    d=d+10 #number has to end in a 0 because it is divisible by both 2 and 5
        
