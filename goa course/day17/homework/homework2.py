# Remove String Spaces

# Write a function that removes the spaces from the string, then return the resultant string.

def no_space(x):
    my_str=""
    for i in x:
        if i!=" ":
            my_str+=i
    return my_str