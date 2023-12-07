# Abbreviate a Two Word Name

# Write a function to convert a name into initials. 
# This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.

def abbrev_name(name):
    my_arr=name.split()
    return my_arr[0][0].capitalize() +"."+my_arr[1][0].capitalize()