from Bio import SeqIO

def transcribe_gene(fasta_path: str = "mocked_gene.fna"):
    """Lee un FASTA y devuelve ADN, ARNm y ARNm inverso."""
    record = next(SeqIO.parse(fasta_path, "fasta"))
    dna = record.seq
    mrna = dna.transcribe()
    mrna_reverse = dna.reverse_complement().transcribe()
    return dna, mrna, mrna_reverse

def main():
    print("_____Ejercicio 2_____")
    fasta = "data/mocked_gene.fna"
    dna, mrna, mrna_reverse = transcribe_gene(fasta)

    print("Secuencia ADN completa:")
    print(dna, "\n")

    print("ARNm (codificante):")
    print(mrna, "\n")

    print("ARNm (complementaria inversa como codificante):")
    print(mrna_reverse)

if __name__ == "__main__":
    main()