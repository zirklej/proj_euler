'''Project Euler #6:  Sum Square Difference'''

sum_square=0

for i in range(1,101):
    sum_square=sum_square+i**2

square_sum=((100*101)/2)**2 #sum of first 100 integers using Gaussian formula

difference=square_sum-sum_square

print(difference)
