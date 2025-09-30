from ejercicios import (
    ejercicio1
)

def main():
    var = "GATTACA"
    comp = ejercicio1.complement(var)
    print(f"La complementaria de {var} es: {comp}")

if __name__ == "__main__":
    main()

# Ejercicio 1. Replicación del ADN
# Objetivo: comprender el mecanismo semiconservativo y las enzimas implicadas.
# Instrucciones:
# 1. Considera la siguiente secuencia de ADN: 5’ – ATG CCG TTA GCT – 3’ / 3’ – TAC GGC AAT CGA – 5’.
# 2. Realiza una ronda de replicación:
#    o Identifica las nuevas hebras que se formarán.
#    o Indica cuál sería la función de las enzimas helicasa, primasa, ADN polimerasa y ligasa en este proceso.
# 3. Reflexiona: ¿qué ocurriría si la ADN polimerasa cometiera un error en una base y no se corrigiera?
#
# Extensión con Biopython:
# Escribe un pequeño script que, dada una cadena de ADN, genere automáticamente su hebra
# complementaria, y comprueba si tu resultado coincide con lo que obtuviste manualmente.

# Ejercicio 2. Transcripción del ADN a ARN
#
# 1) Secuencia dada:
#    Hebra codificante (5’→3’): ATG CCT GAA TGC
#    Hebra molde (3’→5’):       TAC GGA CTT ACG
#
# 2) La cadena molde es la que se lee en dirección 3’→5’:
#    3’ – TAC GGA CTT ACG – 5’
#
# 3) Transcrito de ARN (complementario a la molde, en dirección 5’→3’):
#    5’ – AUG CCU GAA UGC – 3’
#
# 4) Región promotora: secuencia previa al inicio de transcripción
#    donde se une la ARN polimerasa (ejemplo en eucariotas: caja TATA).
#
#    Región codificante: fragmento del ADN que se transcribe y traduce,
#    en este caso el que origina el ARNm anterior.
#
# Extensión con Biopython:
# Crea un script que lea un archivo FASTA con ADN y produzca la secuencia de ARNm.
# Experimenta cambiando la orientación de la hebra y observa qué ocurre.
#
# print("_____Ejercicio 2_____")
#
# gene = "mocked_gene.fna"
# record = next(SeqIO.parse(gene, "fasta"))
# read_seq = record.seq
# mrna = read_seq.transcribe()
# mrna_reverse = read_seq.reverse_complement().transcribe()
#
# print("Secuencia ADN completa:")
# print(read_seq, "\n")
#
# print("ARNm (codificante):")
# print(mrna, "\n")
#
# print("ARNm (complementaria inversa como codificante):")
# print(mrna_reverse)
#
# # Ejercicio 3. Traducción del ARNm a proteína
# # Objetivo: aplicar el código genético y reflexionar sobre mutaciones.
# #
# # 1. Transcrito: 5’ – AUG UAU GCU UAA – 3’
# #    Codón de inicio: AUG (Metionina)
# #    Codón de paro:   UAA (Stop)
# #    Traducción: AUG → Metionina (M), UAU → Tirosina (Y), GCU → Alanina (A)
# #    Cadena resultante: Met – Tyr – Ala
# #
# # 2. Si AUG muta a GUG → puede iniciar pero menos eficiente; si no se reconoce, no se traduce proteína.
# # 3. Si desaparece el STOP → la traducción continúa hasta otro STOP → proteína más larga y probablemente no funcional.
# #
# # Extensión con Biopython:
# # Traducir automáticamente con Bio.Seq.
#
# print("_____Ejercicio 3_____")
#
# mrna = Seq("AUGUAUGCUUAA")
# protein = mrna.translate()
#
# print("ARNm:", mrna)
# print("Proteína:", protein)
#
# # Ejercicio 4. Splicing alternativo
# # Objetivo: comprender cómo un mismo gen puede generar varias proteínas.
# # Instrucciones:
# # 1. Gen con 5 exones: Exón 1 – Exón 2 – Exón 3 – Exón 4 – Exón 5.
# # 2. Ejemplo de combinaciones: 1-2-4-5 o 1-3-5.
# # 3. Diferencias: distintas combinaciones → distintas proteínas (longitud/estructura).
# # 4. Reflexión: este mecanismo aumenta la diversidad proteica sin necesidad de más genes.
#
# print("_____Ejercicio 4_____")
#
# # Ejercicio 5. Introducción a las proteínas
# # Objetivo: relacionar secuencia, estructura y función.
# # Instrucciones:
# # 1. Secuencia ejemplo: Met – Ile – Ser – Gly – Val – Lys – His.
# # 2. Extremo N: Metionina, Extremo C: Histidina.
# # 3. Reflexión: el orden de aminoácidos determina la estructura final;
# #    una mutación hidrofóbico→hidrofílico en región interna puede desestabilizar el plegamiento.
#
# print("_____Ejercicio 5_____")
#
# # Ejercicio 6. Actividad integradora: del ADN a la proteína
# # Objetivo: recorrer el dogma central completo.
# # Pasos: replicación, transcripción, traducción.
# # Reflexión: la traducción es el punto más vulnerable (un error puede alterar toda la proteína).
# #
# # Extensión con Biopython: pipeline sencillo.
#
# print("_____Ejercicio 6_____")
#
# fasta = "mocked_gene.fna"
# asume_codificante = True  # False si la secuencia es hebra molde
#
# record = next(SeqIO.parse(fasta, "fasta"))
# dna = record.seq.upper()
#
# hija_A = dna.reverse_complement()
# hija_B = dna
#
# if asume_codificante:
#     mrna = dna.transcribe()
# else:
#     mrna = dna.reverse_complement().transcribe()
#
# s = str(mrna)
# start = s.find("AUG")
# if start == -1:
#     protein = Seq(s).translate(to_stop=True)
# else:
#     protein = Seq(s[start:]).translate(to_stop=True)
#
# print("ADN (5'->3')        :", dna)
# print("Hija A (5'->3')     :", hija_A)
# print("Hija B (5'->3')     :", hija_B)
# print("ARNm (5'->3')       :", mrna)
# print("Proteína (aa)       :", protein if protein else "(vacía)")