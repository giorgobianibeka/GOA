# Count of positives / sum of negatives

# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

# If the input is an empty array or is null, return an empty array.

def count_positives_sum_negatives(arr):
    if len(arr)==0:
        return arr
    count_sum_positives=0
    count_sum_negatives=0
    for i in arr:
        if i > 0:
            count_sum_positives += 1
        else: 
            count_sum_negatives+=i
    return [count_sum_positives,count_sum_negatives]