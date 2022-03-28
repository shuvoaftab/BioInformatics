
from Bio import Seq

dna = input()


def ReverseComplement(dna):
    reverse_dna = Seq.reverse_complement(dna)
    return reverse_dna


reverse_dna = ReverseComplement(dna)
print(reverse_dna)
