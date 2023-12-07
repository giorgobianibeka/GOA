# Fake Binary

# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

def fake_bin(x):
    bin=""
    for i in x:
        if int(i) < 5:
            bin+="0"
        elif int(i) >= 5:
            bin+="1"
    return bin