'''Project Euler #9:  Special Pythagorean Triplet'''

a=1
finish=False

def check(a):
    for i in range(a,999-a):
        b=i
        c=1000-a-b
        print(a,b,c)
        if (a**2+b**2==c**2):
            print(a*b*c)
            return True
        elif i==998-a:
            return False
        else:
            pass

while finish==False:
    finish=check(a)
    a=a+1




