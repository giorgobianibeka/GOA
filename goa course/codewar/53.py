# Convert a string to an array

def string_to_array(s):
    if len(s)<1:
        return [""]
    return s.split()