# Find the smallest integer in the array

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