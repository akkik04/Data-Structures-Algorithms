# TRANSCRIBE TO MRNA EDABIT SOLUTION:

# creating a function to solve the problem.
def dna_to_rna(dna):

    # returning the DNA strand with modifications to make it an RNA strand.
    return(dna.replace("A", "U")
        .replace("T", "A")
        .replace("G", "C")
        .replace("C", "G"))