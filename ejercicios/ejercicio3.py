from Bio.Seq import Seq

sec = "AUGUAUGCUUAA"

def translate_mrna(seq_str: str = sec):
    """
    Traduce un ARNm a proteína usando el código genético estándar.
    """
    mrna = Seq(seq_str)
    protein = mrna.translate()
    return mrna, protein

def main():
    mrna, protein = translate_mrna()
    print("ARNm:", mrna)
    print("Proteína:", protein)

if __name__ == "__main__":
    main()