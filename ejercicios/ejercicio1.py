from Bio.Seq import Seq

def header(title: str) -> None:
    print(f"\n{'_'*5} {title} {'_'*5}")

def complement(seq: str) -> Seq:
    return Seq(seq).complement()

def main():
    var = "GATTACA"
    comp = complement(var)
    print(f"La complementaria de {var} es: {comp}")

if __name__ == "__main__":
    main()
