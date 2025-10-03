

# Ejercicio 1. Replicación del ADN
**Objetivo:** comprender el mecanismo semiconservativo y las enzimas implicadas.  

## 1. Secuencia inicial
```
5’ – ATG CCG TTA GCT – 3’
3’ – TAC GGC AAT CGA – 5’
```

## 2. Ronda de replicación
**Nuevas hebras:**
```
TAC GGC AAT CGA
ATG CCG TTA GCT
```

### Función de las enzimas
- **Helicasa:** desenrolla la doble hélice y rompe los puentes de hidrógeno.  
- **Primasa:** sintetiza fragmentos cortos de ARN (cebadores).  
- **ADN polimerasa:** incorpora nucleótidos complementarios en dirección 5’→3’.  
- **Ligasa:** une los fragmentos de Okazaki en la hebra retardada.  

## 3. Reflexiona
**¿Qué ocurre si la ADN polimerasa comete un error y no se corrige?**  

Se genera una **mutación**:  
- **Silenciosa:** sin efecto en la proteína.  
- **Cambio de sentido:** altera un aminoácido.  
- **Sin sentido:** introduce un codón de paro prematuro.  

Si ocurre en una región no codificante, puede no tener consecuencias.  

> **Extensión con Biopython:** Escribe un script que, dada una cadena de ADN, genere automáticamente su hebra complementaria y compárala con tu resultado manual.

---

# Ejercicio 2. Transcripción del ADN a ARN
**Objetivo:** traducir correctamente la información de la cadena molde.  

## 1. Secuencia de ADN
```
5’ – ATG CCT GAA TGC – 3’
3’ – TAC GGA CTT ACG – 5’
```

## 2. Identificar la cadena molde
La cadena molde es:
```
3’ – TAC GGA CTT ACG – 5’
```
La superior (5’→3’) es la codificante.  

## 3. Transcrito de ARN
```
5’ – AUG CCU GAA UGC – 3’
```

## 4. Promotora vs Codificante
- **Promotora:** sitio de unión de ARN polimerasa y factores de transcripción, no se transcribe.  
- **Codificante:** región que se transcribe y luego se traduce.  

> **Extensión con Biopython:** Crea un script que lea un FASTA con ADN y genere el ARNm correspondiente.

---

# Ejercicio 3. Traducción del ARNm a proteína
**Objetivo:** aplicar el código genético y reflexionar sobre mutaciones.  

## 1. Transcrito de ARN
```
5’ – AUG UAU GCU UAA – 3’
```

## 2. Codón de inicio y de paro
- **Inicio:** `AUG` → Metionina (Met)  
- **Paro:** `UAA`  

## 3. Traducción
```
AUG – UAU – GCU – UAA
```

- AUG → Metionina (Met)  
- UAU → Tirosina (Tyr)  
- GCU → Alanina (Ala)  
- UAA → Stop  

**Proteína sintetizada:**  
```
Met – Tyr – Ala
```

## 4. Reflexiona
- Si `AUG` muta a `GUG`, puede iniciar con Valina (Val).  
- Si desaparece `UAA`, la proteína será más larga → posible pérdida de función.  

> **Extensión con Biopython:** Usa `Bio.Seq` para traducir automáticamente el ARNm y compáralo con tu traducción manual.

---

# Ejercicio 4. Splicing alternativo
**Objetivo:** comprender cómo un mismo gen puede generar varias proteínas.  

## 1. Exones
```
1 – 2 – 3 – 4 – 5
```

## 2. Ejemplos de isoformas
- 1 – 2 – 4 – 5  
- 1 – 3 – 5  

## 3. Diferencias proteicas
- Longitud distinta.  
- Presencia o ausencia de dominios funcionales.  
- Posible cambio en localización celular.  

## 4. Reflexiona
El splicing alternativo permite que de un solo gen se obtengan varias isoformas, aumentando la diversidad proteica.  

> **Extensión con Biopython/Ensembl:** Busca en Ensembl un gen humano con isoformas (ej. *FGFR2*) y compara transcritos.

---

# Ejercicio 5. Introducción a las proteínas
**Objetivo:** relacionar secuencia, estructura y función.  

## 1. Secuencia
```
Met – Ile – Ser – Gly – Val – Lys – His
```

## 2. Extremos
- **N-terminal:** Metionina (Met).  
- **C-terminal:** Histidina (His).  

## 3. Reflexiona
- El orden de aminoácidos define la estructura primaria y, por tanto, la estructura final.  
- Sustituir un aminoácido hidrofóbico por uno hidrofílico en el núcleo:  
  - Desestabiliza la proteína.  
  - Puede alterar plegamiento y función.  

> **Extensión con Bioinformática:** Busca en el **PDB** la estructura de una proteína y analiza el efecto de una mutación puntual.

---

# Ejercicio 6. Actividad integradora
**Objetivo:** recorrer el dogma central completo.  

## 1. ADN de partida
```
5’ – ATG GCT TTA GGA CCT – 3’
3’ – TAC CGA AAT CCT GGA – 5’
```

## 2. Replicación
```
ATG GCT TTA GGA CCT
TAC CGA AAT CCT GGA
```

## 3. Transcripción
```
5’ – AUG GCU UUA GGA CCU – 3’
```

## 4. Traducción
```
AUG – GCU – UUA – GGA – CCU
```

**Proteína:**  
```
Met – Ala – Leu – Gly – Pro
```

## 5. Reflexiona
La **transcripción** es el paso más vulnerable porque:  
- Hay menos mecanismos de corrección.  
- Los errores pasan a la proteína.  

## 6. Extensión
Un pipeline en Python con Biopython debería hacer:  
1. Replicación  
2. Transcripción  
3. Traducción  

---

# Referencias
[1] Gisela Belmonte Cruz (2025). *Repositorio de ejercicios en Python usando Biopython*.  
Disponible en: [https://github.com/giselabcruz/pa_2_bio](https://github.com/giselabcruz/pa_2_bio)
