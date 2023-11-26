# 1 String repeat

# Write a function that accepts an integer n and a string s as parameters,
# and returns a string of s repeated exactly n times.

def repeat_str(repeat, string):
    return string*repeat

# 2 Remove First and Last Character

# It's pretty straightforward. Your goal is to create a function that removes the first and last 
# characters of a string. You're given one parameter, the original string. You don't 
# have to worry with strings with less than two characters.

# method 1
def remove_char(s):
    new_s=""
    i=1
    while i <len(s)-1:
        new_s+=s[i]
        i+=1
    return new_s

# method 2
def remove_char(s):
    return s[1:-1]

# 3Find the smallest integer in the array

# Given an array of integers your solution should find the smallest integer.

#   method 1
def find_smallest_int(arr):
    min=arr[0]
    for item in arr:
        if min> item:
            min=item
    return min

#   method 2
def find_smallest_int(arr):
    return min(arr)