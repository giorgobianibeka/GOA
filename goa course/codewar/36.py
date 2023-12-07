# Calculate average

# Write a function which calculates the average of the numbers in a given list.

# Note: Empty arrays should return 0.


def find_average(numbers):
    my_list=0
    if numbers==[]:
        return 0
    for i in numbers:
        my_list+=i
    return my_list/len(numbers)