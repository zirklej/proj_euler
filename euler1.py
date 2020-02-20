'''Project Euler #1:  Multiples of 3 and 5'''

#find the sum of the multiples of 3 from 1 to 999

num3=int(1000/3) #number of multiples of 3 less than 1000
sum3=3*(num3*(num3+1))/2 #sum of multiples of 3 using Gaussian formula

#find the sum of the multiples of 5 from 1 to 1000

num5=int(1000/5) #number of multiples of 5 less than 1000
sum5=5*(num5*(num5+1))/2 #sum of multiples of 5 using Gaussian formula

#find the sum of the multiples of lcm(3,5)=15

num15=int(1000/15) #number of multiples of lcm less than 1000
sum15=15*(num15*(num15+1))/2 #sum of multiples of lcm using Gaussian formula

total_sum=int(sum3+sum5-sum15-1000) #have to exclude 1000

print(total_sum)


