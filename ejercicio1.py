from Bio import SeqIO
from Bio.Seq import Seq

print("_____Ejercicio 1_____")

def complement(seq):
    seq = Seq(seq)
    complementaria = Seq.complement(seq)
    return complementaria

print(f'Complementaria: {complement("GATTACA")}')
