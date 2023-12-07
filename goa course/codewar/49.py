# Reversed Words

def reverse_words(s):
    x = s.split()
    x.reverse()
    final_str=""
    for element in x:
        final_str+=element + " "
    # return final_str[:-1]
    return final_str.strip()