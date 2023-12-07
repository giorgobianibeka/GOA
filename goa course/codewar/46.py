# Count the Monkeys!
 
# method 1
def monkey_count(n):
    return list(range(1,n+1))

# method 2
def monkey_count(n):
    my_arr=[]
    for i in range (1,n+1):
        my_arr.append(i)
    return my_arr

