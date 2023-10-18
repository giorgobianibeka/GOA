tickets=25
people=[12,34,21,6,19,42,25,22,10,29,47,36,77]
total_amount=0
for i in people:
    if i >=16:
        total_amount+=25
print(total_amount)