from Bio import SeqIO
import sys

def gc_content(seq):
    """
    Calcula el porcentaje de bases G y C en una secuencia de ADN/ARN.
    """
    s = str(seq).upper()
    if len(s) == 0:
        return 0.0
    return 100 * (s.count("G") + s.count("C")) / len(s)

def identidad(seq1, seq2):
    """
    Qué porcentaje de posiciones tienen exactamente la misma base entre secuencias.
    """
    n = min(len(seq1), len(seq2))
    if n == 0:
        return 0.0
    iguales = sum(1 for a, b in zip(seq1[:n], seq2[:n]) if a == b)
    return 100 * iguales / n

def cargar_transcrito(path):
    """
    Carga el primer transcrito de un archivo FASTA.
    """
    try:
        return next(SeqIO.parse(path, "fasta")).seq
    except StopIteration:
        sys.exit(f"[ERROR] El archivo {path} no contiene secuencias.")
    except FileNotFoundError:
        sys.exit(f"[ERROR] No se encontró el archivo {path}.")

def main():
    file = "data/gen_FGFR2.fna"
    file1 = "data/ensembl-206.fna"
    file2 = "data/ensembl-235.fna"

    seq = cargar_transcrito(file) #En este caso, no se trata de un transcrito, pero la uso ya que mhace la misma función
    seq1 = cargar_transcrito(file1)
    seq2 = cargar_transcrito(file2)

    print(f"Gen FGFR2: {file}")
    print(f"  Longitud = {len(seq)} nucleotidos | %GC = {gc_content(seq):.2f}")
    print(f"Transcrito 1: {file1}")
    print(f"  Longitud = {len(seq1)} nucleotidos | %GC = {gc_content(seq1):.2f}")
    print(f"Transcrito 2: {file2}")
    print(f"  Longitud = {len(seq2)} nucleotidos | %GC = {gc_content(seq2):.2f}")
    print("----------------------------------")
    print(f"Identidad nucleotídica entre transcritos: {identidad(seq1, seq2):.2f} %")

if __name__ == "__main__":
    main()