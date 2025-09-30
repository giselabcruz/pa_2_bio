from Bio.Seq import Seq

def complement(seq: str) -> Seq:
    return Seq(seq).complement()

def main():
    var = "GATTACA"
    comp = complement(var)
    print(f"La complementaria de {var} es: {comp}")

if __name__ == "__main__":
    main()
