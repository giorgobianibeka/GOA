# Find Maximum and Minimum Values of a List

# Your task is to make two functions ( max and min, or maximum and minimum, etc., depending on the language ) that receive a list of integers as input, and return the largest and lowest number in that list, respectively.

def minimum(arr):
    min_arr=arr[0]
    for item in arr:
        if item<min_arr:
            min_arr=item
    return min_arr
def maximum(arr):
    max_arr=arr[0]
    for item in arr:
        if item>max_arr:
            max_arr=item
    return max_arr