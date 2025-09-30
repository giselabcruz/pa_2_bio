from Bio import SeqIO

print("_____Ejercicio 2_____")

gene = "mocked_gene.fna"
record = next(SeqIO.parse(gene, "fasta"))
read_seq = record.seq
mrna = read_seq.transcribe()
mrna_reverse = read_seq.reverse_complement().transcribe()

print("Secuencia ADN completa:")
print(read_seq, "\n")

print("ARNm (codificante):")
print(mrna, "\n")

print("ARNm (complementaria inversa como codificante):")
print(mrna_reverse)