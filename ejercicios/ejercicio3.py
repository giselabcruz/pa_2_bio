from Bio.Seq import Seq

print("_____Ejercicio 3_____")

mrna = Seq("AUGUAUGCUUAA")
protein = mrna.translate()

print("ARNm:", mrna)
print("Proteína:", protein)
