# Invert values

# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

def invert(lst):
    my_list=[]
    if len(lst)==0:
        return []
    for i in lst:
        my_list.append(i*-1)
    return my_list