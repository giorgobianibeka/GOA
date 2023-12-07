# DNA to RNA Conversion

def dna_to_rna(dna):
    my_dna=""
    for element in dna:
        if element == "T":
            my_dna+="U"
        else:
            my_dna+=element
    return my_dna