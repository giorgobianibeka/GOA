#Convert number to reversed array of digits

# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

def digitize(n):
    my_arr=[]
    for i in str(n):
        my_arr.append(int(i))
    my_arr.reverse()
    return my_arr