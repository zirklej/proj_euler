'''Project Euler #13:  Large Summ'''

fin=open('euler13.txt')
run_sum=0

for i in range(0,100):
    num=fin.readline()
    num=num.strip()
    print(num)
    num=int(num)
    run_sum=run_sum+num

print(run_sum)
run_sum=str(run_sum)
print(run_sum[0:10])
