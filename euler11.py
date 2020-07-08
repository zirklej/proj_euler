'''Project Euler #11:  Largest Product in a Grid'''

fin=open('euler11.txt', newline=None)
array=[]
delimiter=' '

for i in range(20):
    stor=fin.readline()
    array.append(stor.split(delimiter))
    array[i][19]=array[i][19].strip() #remove trailing '\n' 

def  vert(array):
    max_vert=1
    for i in range(17):
        for j in range(20):
            prod=int(array[i][j])*int(array[i+1][j])*int(array[i+2][j])*int(array[i+3][j])
            if prod>max_vert:
                #print(i,j)
                max_vert=prod
    return max_vert

def horiz(array):
    max_horiz=1
    for i in range(20):
        for j in range(17):
            prod=int(array[i][j])*int(array[i][j+1])*int(array[i][j+2])*int(array[i][j+3])
            if prod>max_horiz:
                max_horiz=prod
    return max_horiz

def diag_r(array):  #diagonals like: \
    max_diag=1
    for i in range(17):
        for j in range(17):
            prod=int(array[i][j])*int(array[i+1][j+1])*int(array[i+2][j+2])*int(array[i+3][j+3])
            if prod>max_diag:
                max_diag=prod
    return max_diag

def diag_l(array):  #diagonals like:  /
    max_diag=1
    for i in range(17):
        for j in range(3,20):
            prod=int(array[i][j])*int(array[i+1][j-1])*int(array[i+2][j-2])*int(array[i+3][j-3])
            if prod>max_diag:
                max_diag=prod
    return max_diag
print(max(vert(array),horiz(array),diag_r(array),diag_l(array)))
