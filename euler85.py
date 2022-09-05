"""
Euler 85:  counting rectangles

find the area of the rectangle that contains the number of rectangles
closest to 2 million

number of i x j rectangles = (n-i+1)(m-j+1)
where main rectangle is n x m (n rows, m columns)
and 1<=i<=n, 1<=j<=m

limits on size are 1<=n<=2000 and 1<=m<=2000
"""

import numpy as np

# specify number of rows
n=np.arange(1,2001,1)

# specify number of columns
m=np.arange(1,2001,1)

# keep number of sub-rectangles closest to 2,000,000
gate=float('inf')

# array to hold all sub-rectangle counts
subrect_arr=np.zeros(2000*2000)
counter=0
area_arr=np.zeros(2000*2000)

# calculate number of sub-rectangles for each configuration
for i in n:
    print(i)
    for j in m:
        subrect=0.25*(j**2+j)*(i**2+i)
        subrect_arr[counter]=subrect
        area_arr[counter]=i*j
        counter+=1

print(np.amin(abs(2000000-subrect_arr)))
print(np.argmin(abs(2000000-subrect_arr)))
idx=np.argmin(abs(2000000-subrect_arr))
print(subrect_arr[idx])
print(area_arr[idx])

