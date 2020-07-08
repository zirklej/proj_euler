'''Project Euler #4:  Largest Palidrome Product'''

palindrome_list=[]

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if len(word)==1:
        return True
    elif len(word)==2:
        return first(word)==last(word)
    elif len(word)>2:
        if first(word)==last(word):
            return is_palindrome(middle(word))
        else:
            return False

#generate a product, then call is_palindrome
a=999
b=999

for i in range(0,900):
    for j in range(0,900):
        product=(a-i)*(b-j)
        product=str(product)
        if is_palindrome(product)==True:
            palindrome_list.append(int(product))

max_palindrome=max(palindrome_list)
#print(palindrome_list)
print(max_palindrome)
