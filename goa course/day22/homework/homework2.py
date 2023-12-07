# Reversed sequence

# method 1
def reverse_seq(n):
    my_arr=[]
    for i in range(1,n+1):
        my_arr.append(i)
    return my_arr[::-1]

# method 2
def reverse_seq(n):
    arr=[]
    i=n
    while i>0:
        arr.append(i)
        i-=1
    return arr