from Bio.Seq import Seq

def replicar_dna(secuencia_adn):
    print("--- Iniciando Replicación ---")
    hebra_complementaria = secuencia_adn.reverse_complement()
    print(f"Hebra complementaria generada: {hebra_complementaria}")
    print("--- Fin de Replicación ---\n")
    return hebra_complementaria

def transcribir_a_arn(secuencia_adn):
    print("--- Iniciando Transcripción ---")
    transcrito_arn = secuencia_adn.transcribe()
    print(f"ARNm transcrito: {transcrito_arn}")
    print("--- Fin de Transcripción ---\n")
    return transcrito_arn

def traducir_a_proteina(secuencia_arn):
    print("--- Iniciando Traducción ---")
    proteina = secuencia_arn.translate(table="Standard", to_stop=False)  # incluye STOP '*'
    print(f"Secuencia de proteína generada: {proteina}")
    print("--- Fin de Traducción ---\n")
    return proteina

def main():
    dna_original = Seq("ATGGCTTTAGGACCT")
    print(f"Hebra de ADN original: {dna_original}\n")

    hebra_complementaria = replicar_dna(dna_original)
    transcrito_arn = transcribir_a_arn(dna_original)
    proteina_generada = traducir_a_proteina(transcrito_arn)

    print("Pipeline completado.")

if __name__ == "__main__":
    main()