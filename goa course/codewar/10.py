# Remove First and Last Character

# It's pretty straightforward. Your goal is to create a function that removes the first and last 
# characters of a string. You're given one parameter, the original string. You don't 
# have to worry with strings with less than two characters.

def remove_char(s):
    new_s=""
    i=1
    while i <len(s)-1:
        new_s+=s[i]
        i+=1
    return new_s