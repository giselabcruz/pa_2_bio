from Bio import SeqIO

fasta = "data/mocked_gene.fna"

def transcribe_gene(fasta_path: str = fasta):
    """Lee un FASTA y devuelve ADN, ARNm y ARNm inverso."""
    record = next(SeqIO.parse(fasta_path, "fasta"))
    dna = record.seq
    mrna = dna.transcribe()
    mrna_reverse = dna.reverse_complement().transcribe()
    return dna, mrna, mrna_reverse

def main():
    dna, mrna, mrna_reverse = transcribe_gene(fasta)

    print("Secuencia ADN completa:")
    print(dna, "\n")

    print("ARNm (codificante):")
    print(mrna, "\n")

    print("ARNm (complementaria inversa como codificante):")
    print(mrna_reverse)

if __name__ == "__main__":
    main()