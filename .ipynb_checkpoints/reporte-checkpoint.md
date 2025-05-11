# Preliminar / Borrador

# Informe Exploratorio: Osteosarcopenia | Análisis a 53 Pacientes de Escuinapa, Sinaloa.
---

**Estudio:** Dr. Arturo Rizo Topete.  
**Análisis:** Christian Campos

## Objetivo 1: Identificar pacientes con osteosarcopenia.

**Definición:** pacientes con diagnóstico de sarcopenia junto con osteoporosis u osteopenia.

**Criterios usados:**
- _Nivel de sarcopenia_ distinto de _sin sarcopenia_.
- _Clasificación de densidad mineral_ igual a _osteopenia_ u _osteoporosis_.

**Resultados:**
- Pacientes con osteosarcopenia: **26**
- Pacintes sin osteosarcopenia: **27**

### Visualización.

#### 1. Conteo de pacientes.
![Barplot conteo](/outputs/osteosarcopenia_pacientes.png)

**Interpretación:**
Se observa que 26 de los 53 pacientes presentan tanto sarcopenia como osteopenia u osteoporosis, lo que representa el 49% de la muestra. Este hallazgo sugiere que la coexistencia de ambas condiciones es común en la población evaluada, y puede justificar su análisis conjunto.

#### 2. Distribución por edad.
![Barplot conteo](/outputs/osteosarcopenia_edad.png)

**Interpretación:**
La mediana de edad es mayor en el grupo con osteosarcopenia (~68 años) en comparación con quienes no la presentan (~64 años). Aunque hay superposición, los valores centrales y extremos sugieren una posible asociación entre mayor edad y presencia de osteosarcopenia.

#### 3. Osteosarcopenia según nivel de sarcopenia.
![Barplot conteo](/outputs/osteosarcopenia_nivel.png)

**Interpretación:**
Los datos muestran que la mayoría de los pacientes con sarcopenia moderada presentan también osteosarcopenia. En contraste, los pacientes sin sarcopenia no tienen casos registrados de osteosarcopenia, lo cual apoya la definición lógica de esta variable derivada.

#### 4. Cruce con nivel de sarcopenia.
![Barplot conteo](/outputs/osteosarcopenia_nivel_vs_dmo.png)

**Interpretación:**
El cruce de variables indica que los pacientes con sarcopenia moderada son más frecuentes entre quienes tienen osteopenia. También se observan combinaciones de sarcopenia severa con osteoporosis. Estos patrones respaldan la consistencia interna del diagnóstico combinado (osteosarcopenia) y pueden servir como base para análisis posteriores.

**Conclusión de objetivo 1:**
A partir del cruce entre los niveles de sarcopenia y la clasificación de densidad mineral ósea, se identificaron 26 pacientes con criterios compatibles con osteosarcopenia. Esta condicón afecta prácticamente la mitad de la muestra analizada.  
Los patrones observados en las visualizaciones sugieren que la osteosarcopenia es más frecuente a mayor edad y con niveles más avanzados de sarcopenia. Además, la consistencia entre las variables usadas refuerza la validez del criterio adoptado para identificarla.

---
## Objetivo 2: Clasificación de pacientes con osteosarcopenia, osteoporosis u osteopenia.

**Definición:** Este objetivo busca clasificar a los pacientes según las tres condiciones clínicas identificadas en el estudio:

- Osteosarcopenia.
- Osteopenia.
- Osteoporosis.

> Las donciciones no son excluyentes. Un paciente puede tener más de una simultáneamente.

**Resultados:**
- Osteopenia: **35 pacientes**.
- Osteosarcopenia: **26 pacientes**.
- Osteoporosis: **18 pacientes**.

### Visualización
### Conteo de pacientes por condición clínica.
![Barplot conteo](/outputs/objetivo2_condiciones_clinicas.png)

**Interpreteación:**
Los datos muestran que la osteopenia es la condición más prevalente en la muestra, presente en 66% de los pacientes. La osteosarcopenia afecta aproximadamente a la mitad de los pacientes, mientras que la osteoporosis representa el 34%.  

Dado que las condiciones no son excluyentes, es posible que existan intersecciones entre estos grupos, por lo que este análisis permite entender la magnitud individual de cada condición, pero no su combinación exacta.

**Conclusión del objetivo 2:**
Este análisis permitió obtener un conteo individual de los pacientes que presentan osteopenia, osteopososis y osteosarcopenia. La osteopenia fue la condición más frecuente, seguida de la osteosarcopenia. Estos resultados no reflejan exclusividad entre categorías, pero permiten tener un panorama inicial sobre la prevalencia de cada condición en la muestra.