# Multiply

def multiply(a, b):
    return a*b

# Even or Odd
def even_or_odd(number):
    if number%2==0:
        return "Even"
    return "Odd"

# Convert a Number to a String!
def number_to_string(num):
    return str(num)

# Opposite number
def opposite(number):
    return number*-1


# Reversed Strings
def solution(string):
    my_str=""
    i=len(string)

    while i > 0:
        my_str+=string[i-1]
        i-=1
    return my_str
print(solution("giorgobiani"))

# Return Negative
def make_negative( number ):
    if number>0:
        return number*-1
    return number

# Convert boolean values to strings 'Yes' or 'No'.
def bool_to_word(boolean):
    if boolean==True:
        return "Yes"
    return "No"

# Sum of positive
def positive_sum(arr):
    my_arr=0
    for element in arr:
        if element>0:
            my_arr+=element
    return my_arr
