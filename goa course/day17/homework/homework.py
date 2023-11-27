# Grasshopper - Summation

# Write a program that finds the summation of every number from 1 to num. 
# The number will always be a positive integer greater than 0.

#   method 1
def summation(num):
    my_sum=0
    for item in range(num+1):
        my_sum+=item
    return my_sum
    

#   method 2
def summation(num):
    my_sum=0
    i=0
    while i < num+1:
        my_sum+=i
        i+=1
    return my_sum