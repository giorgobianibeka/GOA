# Reversed Strings

# Complete the solution so that it reverses the string passed into it.

#   method 1
def solution(string):
    return string[::-1]

# method 2
def solution(string):
    str = ""
    for i in range(len(string)):
        str += string[-i -1]
        i -= 1 
    return str

# method 3
def solution(string):
    my_str = ""
    i = len(string)
    
    while i > 0:
        my_str += string [i-1]
        i -= 1
    return my_str