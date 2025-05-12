# Informe Exploratorio: Osteosarcopenia - Análisis a 53 Pacientes de Escuinapa, Sinaloa, México.
**Responsable del Estudio:** Dr. Arturo Rizo Topete.  
**Análisis:** Christian Campos Regalado.

---
### Nota sobre estructura del informe.

El presente informe se desarrolla a partir de los veinte objetivos específicos originalmente propuestos por el Dr. Rizo, responsable del estudio. Sin embargo, para facilitar el análisis exploratorio de los datos, se optó por reorganizar dichos objetivos bajo un criterio temático y técnico que permitiera abordar con mayor claridad las relaciones entre variables, los métodos aplicados y la disponibilidad real de información.

Algunas observaciones clave sobre esta reorganización:
* Los objetivos se han agrupado o reordenado según su naturaleza, priorizando la coherencia analítica sobre el orden secuencial original.
* Algunos objetivos fueron fusionados, cuando se referían a mediciones o escalas que comparten enfoque o variables comunes.
* Se documentan explícitamente los casos en los que no fue posible realizar el análisis por falta de datos específicos.
* El contenido del informe refleja integralmente los objetivos propuestos, ya sea mediante análisis directo o justificación técnica de su exclusión.

Este enfoque garantiza que se pueda seguir el razonamiento estadístico y clínico sin necesidad de conocer la numeración original de los objetivos, manteniendo la trazabilidad y el rigor del estudio.

---

### Descripción de la muestra.
El presente análisis se realizó sobre una muestra de **53 pacientes**, con edades entre **55 y 80 años**, y una edad media de **66.5 años**.

Con respecto a la variable `sarcopenia`, el **51% de los pacientes fue clasificado como positivo para sarcopenia**, mientras que el **49% no presenta la condición**.

En la variable `clasificación de densidad mineral`, el **66% de los pacientes fue clasificado con osteopenia y el 34% con osteoporosis**. No se registran casos dentro del rango "normal" para esta variable en esta muestra.

### Propósito del análisis.
El presente informe tiene como propósito explorar y visualizar el comportamiento de distintas variables clínicas, funcionales y antropométricas registradas en una muestra de pacientes, con el fin de responder a los objetivos planteados en torno al estudio de la osteosarcopenia.

El análisis se centra en identificar patrones, distribuciones y posibles relaciones entre variables sin emitir juicios clínicos ni diagnósticos. Todas las visualizaciones y conclusiones están elaboradas exclusivamente a partir del conjunto de datos proporcionado y dentro del marco de un análisis exploratorio de datos.

---

## Objetivo 1: Identificar pacientes con osteosarcopenia.

**Definición:** pacientes con diagnóstico de sarcopenia junto con osteoporosis u osteopenia.

**Variables utilizadas:**
- _Nivel de sarcopenia_ distinto de _sin sarcopenia_.
- _Clasificación de densidad mineral_ igual a _osteopenia_ u _osteoporosis_.

**Resultados:**
- Pacientes con osteosarcopenia: **26**
- Pacientes sin osteosarcopenia: **27**

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

#### Conclusión de objetivo 1:
A partir del cruce entre los niveles de sarcopenia y la clasificación de densidad mineral ósea, se identificaron 26 pacientes con criterios compatibles con osteosarcopenia. Esta condición afecta prácticamente la mitad de la muestra analizada.  
  
Los patrones observados en las visualizaciones sugieren que la osteosarcopenia es más frecuente a mayor edad y con niveles más avanzados de sarcopenia. Además, la consistencia entre las variables usadas refuerza la validez del criterio adoptado para identificarla.

---
## Objetivo 2: Clasificación de pacientes con osteosarcopenia, osteoporosis u osteopenia.

**Definición:** Este objetivo busca clasificar a los pacientes según las tres condiciones clínicas identificadas en el estudio:

- Osteosarcopenia.
- Osteopenia.
- Osteoporosis.

> Las condiciones no son excluyentes. Un paciente puede tener más de una simultáneamente.

**Variables utilizadas:**
- _Clasificación de densidad mineral ósea_
- _Nivel de sarcopenia_

**Resultados:**
- Osteopenia: **35 pacientes**.
- Osteosarcopenia: **26 pacientes**.
- Osteoporosis: **18 pacientes**.

### Visualización
#### Conteo de pacientes por condición clínica.
![Barplot conteo](/outputs/objetivo2_condiciones_clinicas.png)

**Interpretación:**
Los datos muestran que la osteopenia es la condición más prevalente en la muestra, presente en 66% de los pacientes. La osteosarcopenia afecta aproximadamente a la mitad de los pacientes, mientras que la osteoporosis representa el 34%.  

Dado que las condiciones no son excluyentes, es posible que existan intersecciones entre estos grupos, por lo que este análisis permite entender la magnitud individual de cada condición, pero no su combinación exacta.

#### Conclusión del Objetivo 2:
Este análisis permitió obtener un conteo individual de los pacientes que presentan osteopenia, osteoporosis y osteosarcopenia. La osteopenia fue la condición más frecuente, seguida de la osteosarcopenia. Estos resultados no reflejan exclusividad entre categorías, pero permiten tener un panorama inicial sobre la prevalencia de cada condición en la muestra.

---

## Objetivo 3: Dar rehabilitación a los pacientes, de acorde a sus necesidades.

**Definición:** Este objetivo está orientado a una acción clínica. Desde el análisis de datos no es posible prescribir ni sugerir tratamientos, pero sí identificar patrones funcionales que orienten a posibles decisiones.

**Variables utilizadas:**
- _Clasificación de estado físico_: nivel de rendimiento físico (bajo, intermedio, alto).
- _Osteosarcopenia_: presencia o ausencia.

**Criterio de análisis:**
Se evaluó la distribución del estado físico en pacientes con y sin osteosarcopenia, con el objetivo de detectar posibles perfiles con mayor necesidad de intervención funcional.

### Visualización.

#### Estado físico según presencia de osteosarcopenia.
![estado vs osteosarcopenia](/outputs/objetivo3_estado_vs_osteosarcopenia.png)

**Interpretación:**
El gráfico muestra que los pacientes con estado físico bajo tienen una mayor proporción de casos con osteosarcopenia. En cambio aquellos con estado físico alto presentan predominantemente perfiles sin osteosarcopenia.

Este patrón sugiere que el nivel de rendimiento físico puede estar asociado con la presencia de esta condición combinada.

#### Conclusión Objetivo 3:
A partir de la variable _Clasificacion de estado físico_, se identificó que los pacientes con osteosarcopenia presentan con mayor frecuencia una capacidad funcional reducida. Este hallazgo puede ser útil para priorizar intervenciones de rehabilitación en función de la clasificación funcional del paciente.

---

## Objetivo 4: Evaluar la necesidad de tratamiento nutricional.

**Definición:** Este objetivo busca identificar si existen patrones en el estado nutricional que puedan orientar hacia una intervención alimentaria, especialmente en pacientes con osteosarcopenia.

**Variables utilizadas:**

- _Clasificación IMC_: adecuada, sobrepeso, obesidad 1, 2 y 3.
- _Porcentaje de grasa corporal_.
- _Osteosarcopenia_: presencia o ausencia.

**Criterio de análisis:**
Se examinaron las distribuciones de IMC y del porcentaje de grasa corporal en pacientes con y sin osteosarcopenia, con el fin de detectar perfiles de riesgo o indicios que sugieran la necesidad de intervención nutricional.

### Visualización.

#### 1. Clasificación IMC según presencia de osteosarcopenia.

![imv vs osteosarcopenia](/outputs/objetivo4_imc_vs_osteosarco.png)

**Interpretación:**
Se observa una mayor proporción de pacientes con osteosarcopenia en las categorías de obesidad 2 y obesidad 3, mientras que el grupo sin osteosarcopenia predomina en el sobrepeso. Esto podría sugerir una asociación entre niveles más elevados de IMC y mayor prevalencia de osteosarcopenia.

#### 2. Distribución del % de grasa corporal.

![imv vs osteosarcopenia](/outputs/objetivo4_grasa_vs_osteosarco.png)

**Interpretación:**
El gráfico muestra que los pacientes con osteosarcopenia presentan un porcentaje de grasa corporal más alto que aquellos sin esta condición. La mediana se encuentra desplazada hacia valores mayores, lo cual indica que al menos la mitad de estos pacientes tienen un porcentaje de grasa elevado. Además el rango intercuartílico (la distancia entre el primer y tercer cuartil) también es mayor, lo que sugiere más variabilidad y que un segmento amplio del grupo presenta niveles altos de adiposidad. Los valores atípicos o extremos refuerzan esta dispersión.

#### Conclusión Objetivo 4:
A través del análisis del IMC y del porcentaje de grasa corporal, se observan diferencias entre los pacientes con y sin osteosarcopenia. Los datos muestran una mayor concentración de casos con osteosarcopenia en las categorías más altas de IMC, así como una mayor mediana de grasa corporal en ese grupo. Estos hallazgos no establecen causalidad, pero aportan indicios de una posible relación entre composición corporal y presencia de osteosarcopenia.

---

## Objetivo 5: Comparar los diversos métodos de diagnóstico de sarcopenia.

**Definición:** Este objetivo busca observar cómo se comportan diferentes métodos diagnósticos de sarcopenia en la muestra. No se busca validar los métodos clínicamente, sino detectar consistencias, patrones o discrepancias entre ellos.

**Variables utilizadas:**
**Categóricas:**
- _Resultado de la escala SARC-F._
- _Resultado IMME._
- _Resultado de la fuerza de prensión._
- _Resultado de la velocidad de marcha._

**Numéricas:**
- _Circunferencia de la pantorilla._
- _Fuerza de prensión._
- _Velocidad de la marcha._

**Criterio de análisis:**
Se dividieron los métodos en dos grupos: variables categóricas (clasificación binaria del diagnóstico) y variables numéricas (medidas continuas asociadas). Esto permite abordar primero la presencia o ausencia de sarcopenia por método, y luego analizar cómo se comportan estas medidas según osteosarcopenia. Finalmente, se exploraron las correlaciones entre ellas.

### Visualización.
#### 1. Escala SARC-F.

![sarc-f](/outputs/objetivo5_sarc_f_resultado.png)

**Interpretación:**
35 pacientes presentan baja probabilidad de sarcopenia según SARC-F, mientras que 18 tienen alta probabilidad. Este instrumento, basado en la percepción del propio desempeño físico, identifica una proporción menor de posibles casos respecto a otros métodos.

#### 2. Circunferencia de miembro torácico.
![imme](/outputs/objetivo5_imme_resultado.png)

**Interpretación:**
La gran mayoría (44 pacientes) fue clasificada como "normal", mientras que 8 fueron detectados con sarcopenia grado 1 y sólo 1 con grado 2. Esto podría indicar que éste criterio es más convervador o que la muestra tiene características que lo afectan.

#### 3. Fuerza de prensión.
![resultado de fp](/outputs/objetivo5_resultado_de_fp.png)

**Interpretación:**
Hay distribución cercana entre pacientes con resultado _normal_ (30) y aquellos con resultado _sarcopenia_ (23). Esto indica que la fuerza de prensión muestra un equilibrio en la detección dentro de esta muestra.

#### 4. Velocidad.
![resultado_de_velocidad](/outputs/objetivo5_resultado_de_velocidad.png)

**Interpretación:**
Similar al patrón anterior, 31 pacientes fueron clasificados como _normal_, mientras que _22_ mostraron indicadores compatibles con sarcopenia. Esto sugiere que la velocidad también es un criterio que tiende a dividir la muestra de forma balanceada.

#### 5. Circunferencia de pantorrilla.
![circunferencia de pantorrilla](/outputs/objetivo5_circunferencia_de_la_pantorrilla.png)

**Interpretación:**
La distribución de la circunferencia de pantorrilla es similar entre grupos. No se observa una separación marcada entre los grupos. La mediana es ligeramente menor en quienes presentan osteosarcopenia, aunque con mayor dispersión, lo que sugiere que esta medida no diferencia de forma clara entre ambos perfiles.

#### 6. Fuerza de prensión (kg).
![fuerza de prensión](/outputs/objetivo5_fuerza_de_prension.png)

**Interpretación:**
Los pacientes con osteosarcopenia tienden a presentar una fuerza de prensión más baja. Las medianas entre ambos grupos están separadas, y el grupo con osteosarcopenia muestra también menor rango intercuartílico, indicando menor variabilidad.


#### 7. Velocidad de marcha (m/s).
![velocidad de la marcha](/outputs/objetivo5_velocidad_de_la_marcha.png)

**Interpretación:**
Los pacientes con osteosarcopenia tienden a tener velocidades de marcha más bajas. La mediana y el rango intercuartílico del grupo se sitúan en valores inferiores, lo que sugiere una menor capacidad para desplazarse con rapidez en este grupo. Esto se refuerza por la presencia de varios valores atípicos bajos en este grupo.


#### 8. Correlación entre medidas numéricas.
![correlación](/outputs/objetivo5_corr.png)

**Interpretación:**
Se exploró la relación entre variables numéricas involucradas en los diferentes métodos de diagnósticos de sarcopenia. En la matriz de correlación se observaron los siguientes hallazgos:
- Puntaje SARC-F mostró una correlación negativa moderada con la fuerza de prensión (-0.63) y con la velocidad de la marcha (-0.60). Esto indica que, a mayor puntaje, menores son los valores observados en estas dos pruebas físicas.
- La fuerza de prensión y la velocidad de la marcha también están moderadamente relacionados entre sí (0.40), lo que sugiere que los pacientes con mayor fuerza suelen tener también mayor velocidad al caminar.
- La circunferencia de la pantorrilla muestra relaciones débiles con las demás variables. Esto podría sugerir que esta medida refleja una característica diferente del perfil físico, posiblemente más relacionada con el tamaño del músculo que con su uso o desempeño en las pruebas.

#### Conclusión Objetivo 5:
El análisis comparativo de los métodos disponibles para detectar sarcopenia mostró resultados razonablemente consistentes. A través de los métodos categóricos (_SARC-F, IMME, fuerza de prensión, velocidad de la marcha_), se identificó un porcentaje importante de pacientes con resultados positivos en al menos uno de los enfoques. Cada método presenta distintos niveles de sensibilidad, lo que genera variaciones en la proporción de los pacientes detectados.

Por otro lado, los métodos numéricos (_circunferencia de la pantorrilla, fuerza de prensión y la velocidad de la marcha_) permitieron observar diferencias más claras entre quienes presentan osteosarcopenia y quienes no. En particular, los pacientes con osteosarcopenia tienden a tener menor fuerza de prensión, menor velocidad de marcha y una ligera tendencia a menor circunferencia de pantorrilla, aunque esta última con mayor dispersión.

Al explorar la relación entre estas variables numéricas se observó que el puntaje SARC-F se correlaciona negativamente con la fuerza de prensión y la velocidad de marcha, lo que indica que a mayor puntaje, los valores físicos tienden a ser menores. Fuerza y velocidad también mostraron una correlación positiva entre sí. En contraste, la circunferencia de la pantorrilla presentó asociaciones bajas con las demás variables, lo que sugiere que podría estar reflejando otro tipo de característica física dentro de esta muestra.

---

## Objetivo 6: Clasificar a los pacientes según niveles de funcionalidad mediante la prueba SPPB

**Definición** Este objetivo busca clasificar a los pacientes en cuatro niveles de funcionalidad física a parte de la prueba SPPB. Desde el análisis de datos, se busca identificar la distribución de los pacientes en estas categorías funcionales para ofrecer un panorama sobre su capacidad física general.

**Variables utilizadas:**
- _Puntaje total de la prueba SPPB_: resultado combinado de equilibrio, marcha y levantarse de la silla.
- _Osteosarcopenia:_ indicador si el paciente presenta sarcopenia más una alteración ósea (osteopenia u osteoporosis).

**Criterio de análisis:**
Se clasificó a los pacientes en cuatro categorías según su puntaje SPPB:
- Mínima (10 - 12 puntos).
- Leve (7 -9 puntos).
- Moderada (5 - 6 puntos).
- Grave (0 - 4 puntos).

Posteriormente, se analizó la distribución de estos niveles y su relación con la presencia de osteosarcopenia.

### Visualización
#### 1. Distribución de pacientes según niveles de funcionalidad.

![distribución sppb](/outputs/objetivo6_sppb_categorias.png)

**Interpretación:**
Se observa que la mayoría de los pacientes se ubican en los niveles mínima o leve de limitación funcional, mientras que una menor proporción presenta limitaciones moderadas o graves. Esto indica que, dentro de la muestra, hay una prevalencia mayor de desempeño físico conservado, aunque existe una fracción relevante con limitaciones más marcadas.


#### 2. Relación entre funcionalidad (SPPB) y osteosarcopenia.
![sppb vs osteosarcopenia](/outputs/objetivo6_sppb_vs_osteosarcopenia.png)

**Interpretación**
El gráfico muestra que la proporción de pacientes con osteosarcopenia aumenta a medida que disminuye el nivel de funcionalidad. En la categoría _mínima_, la mayoría no presenta osteosarcopenia, mientras que en las categorías _moderada_ y _grave_ predominan quienes sí la presentan. Este patrón sugiere una posible asociación entre menor desempeño físico y presencia de osteosarcopenia.

#### Tabla de resultados:
| Clasificación | Px. sin osteosarcopenia | Px. con osteosarcopenia | Total Px. |
|---------------|------------------------|-------------------------|----------|
| Mínima        | 18                     | 3                       | 21       |
| Leve          | 6                      | 9                       | 15       |
| Moderada      | 2                      | 9                       | 11       |
| Grave         | 1                      | 5                       | 6        |

La tabla permite observar que la proporción de pacientes con osteosarcopenia aumenta conforme disminuye el nivel de funcionalidad. Mientras que en el grupo _mínima_ la mayoría no presenta la condición, en los niveles _moderada_ y _grave_ los casos positivos superan con claridad a los negativos, lo cual reguerza el patrón ya observado en el gráfico anterior.

### Conclusión Objetivo 6.
A partir de la prueba SPPB, se clasificó a los pacientes según su nivel de funcionalidad física. Se identificó que las limitaciones más severas tienden a coincidir con la presencia de osteosarcopenia. Esta clasificación puede ser útil para priorizar la atención o seguimiento de pacientes con menor desempeño, especialmente si presentan esta condición combinada.

---

## Objetivo 7: Medir la cantidad de músculo total y relacionarla con la sarcopenia.

**Definición:** Este objetivo busca observar si existe una relación entre la masa muscular total y la presencia o el nivel de sarcopenia. El propósito es detectar si los pacientes con menor cantidad de músculo presentan con mayor frecuencia esta condición.

**Variables utilizadas:**
- _Masa muscular absoluta (kg)_: cantidad total estimada de músculo en el cuerpo.
- _Sarcopenia_: presencia o ausencia.
- _Nivel de sarcopenia_: sin, leve, moderada o severa.

**Criterio de análisis:**
Se compararon los valores de masa muscular total entre pacientes con y sin sarcopenia, así como entre los distintos niveles de esta condición. Se utilizaron gráficos de cajas para visualizar la distribución de valores y detectar patrones o diferencias.

### Visualización.

![masa muscular según sacropenia](/outputs/objetivo7_masa_vs_sarcopenia.png)

**Interpretación:**
Aunque hay superposición entre ambos grupos, se observa que los pacientes con sarcopenia tienden a tener menor masa muscular total. Las medianas son ligeramente más bajas y el rango inferior muestra mayor extensión hacia valores bajos.

![masa muscular según nivel de sarcopenia](/outputs/objetivo7_masa_vs_nivel.png)

**Interpretación:**
Aunque se esperaría una disminución progresiva en la masa muscular total conforme aumenta la severidad de la sarcopenia, los datos muestran una desviación en este patrón. En particular, el grupo con sarcopenia leve presenta la mediana más alta de masa muscular, incluso por encima del grupo de sin sarcopenia. A partir de ahí, los valores disminuyen en los grupos moderada y severa, siendo esta única categoría con una caída clara y sostenida.

Este comportamiento inesperado podría deberse a la forma en que se definieron los niveles de sarcopenia en la muestra o a la influencia de factores individuales como el peso corporal o la constitución física.

### Conclusión del Objetivo 7:
La masa muscular total muestra diferencias al compararse con la presencia y el nivel de sarcopenia, pero no sigue un patrón lineal progresivo. Si bien los pacientes con sarcopenia severa presentan la menor masa muscular, los grupos con niveles leves o moderados no muestran disminución continua. De hecho, el grupo con sarcopenia leve presenta valores más altos que el grupo sin sarcopenia. Este hallazgo sugiere que otros factores podrían estar influyendo en la clasificación o que existen variaciones individuales relevantes. Aún así, la caída en el grupo severo refuerza la relación entre baja masa muscular y mayor gravedad en esta condición.

---

## Objetivo 8: Comparar el % de músculo esquelético en miembros pélvicos por impedancia y compararla con la circunferencia de la pantorrilla.

Este objetivo no se abordó en el presente análisis, ya que el conjunto de datos no contiene una variable específica que represente el `porcentaje de músculo esquelético segmentado para miembros pélvicos`.

---

## Objetivo 9: Comparar la fuerza de agarre contra la fuerza del pellizco.

Este objetivo no se abordó, ya que el conjunto de datos no incluye una variable que represente directamente la `fuerza del pellizco`. Al no contar con esta medición específica, no fue posible establecer una comparación con la fuerza de agarre.

---

## Objetivo 10: Medir y graduar el grosor muscular de los músculos seleccionados para el estudio.

Este objetivo no se abordó en el presente análisis, dado que el conjunto de datos disponibles no incluye una variable que represente el `grosor muscular`.

---

## Objetivo 11: Comparar el grado de osteosarcopenia con la escala de Frail, SarQol, Katz y Lawton.

**Definición:** Este objetivo busca analizar si existen diferencias en el nivel de funcionalidad de los pacientes con y sin osteosarcopenia, utilizando escalas que evalúan actividades de la vida diaria. La intención es observar si la presencia de osteosarcopenia se relaciona con menores niveles de funcionalidad o autonomía.

**Variables utilizadas:**
- _Puntaje de katz_: desempeño en actividades básicas de la vida diaria (puntaje de 0 a 6).
- _Resultado de lawton_: desempeño en actividades instrumentales de la vida diaria (puntaje de 0 a 8).
- _Osteosarcopenia_: presencia o ausencia.

**Limitaciones del análisis:**
El análisis original incluía también Frail y SarQol; sin embargo, estas no se encuentran disponibles en el conjunto de datos actual. Por lo tanto, el análisis se limitó a las escalas Katz y Lawton.

**Criterio de análisis:**
Se compararon los puntajes de las escalas Katz y Lawton entre los pacientes con y sin osteosarcopenia. Debido a la naturaleza de los datos (valores agrupados y concentrados), se utilizaron gráficos de caja para visualizar posibles diferencias en la distribución. También se generaron tablas cruzadas para mostrar la frecuencia de cada puntaje en ambos grupos.

### Visualización.

#### 1. Puntaje de Katz según presencia de osteosarcopenia
![katz vs osteosarcopenia](/outputs/objetivo11_katz_vs_osteosarcopenia.png)

**Interpretación:**
La mayoría de los pacientes obtuvieron el puntaje máximo (6) en esta escala, lo que refleja un alto nivel de funcionalidad básica en ambos grupos. Esta falta de variabilidad limita la capacidad de la escala para detectar diferencias entre quienes presentan y no osteosarcopenia. En términos técnicos, se observa un _efecto techo_, lo cual indica que los datos están concentrados en el valor superior.

**Tabla de distribución de puntajes Katz:**
| Osteosarcopenia | 4.0 | 5.0 | 6.0 |
|------------------|-----|-----|-----|
| No               | 0   | 1   | 26  |
| Sí               | 1   | 4   | 21   |


#### 2. Puntaje de Lawton según presencia de osteosarcopenia.
![lawton vs osteosarcopenia](/outputs/objetivo11_lawton_vs_osteosarcopenia.png)

**Interpretación:**
A diferencia de la escala de Katz, el puntaje de Lawton presenta mayor dispersión, especialmente en el grupo con osteosarcopenia. Mientras que el grupo sin esta condición se concentra casi exclusivamente en el puntaje máximo (8), el grupo con osteosarcopenia se distribuye entre los valores 4 a 8. Este diferencia sugiere que Lawton podría ser más sensible para captar variaciones funcionales en pacientes con osteosarcopenia.

**Tabla de distribución de puntajes Lawton:**
| Osteosarcopenia | 4.0 | 5.0 | 6.0 | 7.0 | 8.0 |
|------------------|-----|-----|-----|-----|-----|
| No               | 0   | 0   | 2   | 1   | 24  |
| Sí               | 1   | 1   | 5   | 6   | 13  |

#### Conclusión Objetivo 11:
En esta muestra, la escala de Katz mostró un fuerte efecto techo, con la mayoría de los pacientes ubicados en el puntaje máximo, lo cual limita su utilidad para discriminar entre pacientes con y sin osteosarcopenia.

En contraste, la escala Lawton presentó una mayor dispersión en el grupo con osteosarcopenia, con puntajes que van desde 4 hasta 8, mientras que el grupo sin la condición se concentró mayoritariamente en el valor máximo. Esto sugiere que, dentro de este conjunto de datos, Lawton podría ofrecer una mayor sensibilidad para identificar variaciones funcionales asociadas a la osteosarcopenia.

La falta de datos de las escalas Frain y SarQol limitó el alcance completo del objetivo.

---

## Objetivo 12: Comparar la osteoporosis y sarcopenia con la cantidad de ejercicio de sus años pasados.

**Definición:** Este objetivo busca explorar si existe una relación entre la presencia de sarcopenia y/o osteoporosis y la cantidad de ejercicio que los pacientes realizaban en años anteriores. El propósito es detectar si un menor nivel de actividad física se asocia con estas condiciones.

**Variables utilizadas:**
- _Tiempo de ejercicio_: (no, 30 - 60 mins, 61 - 120 mins, 121 - 180 mins, mas de 180 mins)
- _Sarcopenia_: presencia o ausencia.
- _Clasificación de densidad mineral ósea_: incluye normal, osteopenia y osteoporosis.

**Criterio de análisis:**
Se ordenaron las categorías de ejercicio y se comparó su distribución entre los grupos con y sin sarcopenia, así como entre los grupos con y sin osteoporosis. 

### Visualización.

#### 1. Distribución del ejercicio según presencia de sarcopenia.

![ejercicio y sarcopenia](/outputs/objetivo12_ejercicio_vs_sarcopenia.png)

**Interpretación:**
La mayoría de los pacientes con sarcopenia se centran en la categoría _no_, lo que sugiere una mayor prevalencia de esta condición entre quienes reportaron no haber realizado ejercicio. En contraste, los pacientes sin sarcopenia muestran una distribución más amplia, con mayor representación en categorías de mayor duración de ejercicio.

#### 2. Distribución del ejercicio según presencia de osteoporosis.

![ejercicio y osteoporosis](/outputs/objetivo12_ejercicio_vs_osteoporosis.png)

**Interpretación:**
Aunque el grupo con osteoporosis también se concentra en la categoría _no_, existe cierta representación en las demás categorías. Los pacientes sin osteoporosis muestran una distribución más uniforme, con presencia moderada en todos los niveles de ejercicio. La diferencia no es tan marcada como en el caso de sarcopenia, pero se percibe una tendencia similar.

#### Conclusión Objetivo 12:
Los datos sugieren una posible asociación entre el bajo nivel de ejercicio en años anteriores y la presencia de sarcopenia, ya que la mayoría de los pacientes con esta condición reportaron no haber realizado ejercicio. En el caso de osteoporosis, aunque la tendencia es similar, la distribución entre las categorías es menos marcada. Estos hallazgos podrían reforzar la importancia del ejercicio como posible factor protector frente a condiciones músculo-esqueléticas.

---

## Objetivo 13: Observar si se presentan medicamentos que predispongan a esta patología.

**Definición:** Este objetivo busca explorar si existen patrones de uso de ciertos medicamentos en los pacientes con osteosarcopenia, con el fin de observar su posible distribución diferencial. No se pretende evaluar causalidad ni confirmar efectos clínicos, sino únicamente identificar si alguno de estos grupos farmacológicos aparece con mayor frecuencia en los pacientes con esta condición.

**Variables utilizadas:**
- _Medicamento 1_ y _Medicamento 2_: variables que registran el uso de alguno de los siguientes tipos de medicamentos:
    - Antidiabéticos.
    - Antihipertensivos.
    - Hipnóticos o ansiolíticos.
- _Osteosarcopenia_: presencia o ausencia.

**Criterio de análisis:**
Se unificaron las columnas medicamento 1 y medicamento 2 en una lista por paciente. Posteriormente, se crearon variables binarias que indican si cada paciente utiliza o no alguno de los tres tipos de medicamentos registrados.

### Visualización.

#### 1. Consumo de antidiabéticos según osteosarcopenia.
![antidiabéticos vs osteosarcopenia](/outputs/objetivo13_antidiabeticos_vs_osteosarcopenia.png)

**Interpretación:**
En el grupo con osteosarcopenia se observa una mayor proporción de pacientes que utilizan antidiabéticos en comparación con el grupo sin la condición. 

#### 2. Consumo de antihipertensivos según osteosarcopenia.
![antihipertensivos vs osteosarcopenia](/outputs/objetivo13_antihipertensivos_vs_osteosarcopenia.png)

**Interpretación:**
El uso de antihipertensivos está presente en ambos grupos de manera relativamente pareja. No se observa una diferencia clara en su frecuencia que permita suponer una asociación directa con la presencia de osteosarcopenia.

#### 3. Consumo de hipnóticos o ansiolíticos según osteosarcopenia.
![ansiolíticos vs osteosarcopenia](/outputs/objetivo13_ansioliticos_vs_osteosarcopenia.png)

**Interpretación:**
El consumo de hipnóticos o ansiolíticos es bajo en general, pero su frecuencia relativa es ligeramente mayo en el grupo con osteosarcopenia.

#### Conclusión Objetivo 13:
Los datos muestran que el uso de antidiabéticos es más frecuente en pacientes con osteosarcopenia, mientras que los antihipertensivos no presentan una diferencia notable entre grupos, El uso de ansiolíticos o hipnóticos es bajo, pero ligeramente mayor en pacientes con la condición. Estas observaciones deben interpretarse con cautela ya que el conjunto de datos no permite establecer causalidad.

---

### Objetivo 14: Estratificar el riesgo de fractura con el FRAX en los pacientes con osteosarcopenia.

**Definición:** Este objetivo busca observar si los pacientes con osteosarcopenia presentan una mayor riesgo de fractura, utilizando los indicadores derivados del modelo FRAX. Se consideran tanto las probabilidades continuas como la clasificación ordinal del riesgo, con el fin de identificar si esta condición está asociada a una mayor vulnerabilidad ósea.

**Variables utilizadas:**
- _Probabilidad de fractura por fragilidad._
- _Probabilidad de fractura de cadera_
- _Estratificación de riesgo_: baja, moderada, alta, muy alta.
- _Osteosarcopenia:_ presencia o ausencia.

**Criterio de análisis:**
Se compararon las probabilidades continuas de fractura (por fragilidad y de cadera) mediante gráficos de caja, y se visualizó la distribución de categorías de riesgo para evaluar si el grupo con osteosarcopenia presenta mayor concentración en niveles elevados.

### Visualización.

#### 1. FRAX: Probabilidad de fractura por fragilidad según osteosarcopenia.
![fragilidad vs osteosarcopenia](/outputs/objetivo14_frax_fragilidad_vs_osteosarcopenia.png)

**Interpretación:**
Aunque la mediana es ligeramente más alta en el grupo con osteosarcopenia, la diferencia es mínima y existe un solapamiento considerable entre ambos grupos. No se observa una separación clara en la probabilidad de fractura por fragilidad.

#### 2. FRAX: Probabilidad de fractura de cadera según osteosarcopenia.
![cadera vs osteosarcopenia](/outputs/objetivo14_frax_cadera_vs_osteosarcopenia.png)

**Interpretación:**
En el grupo con osteosarcopenia se observa una mediana elevada en la probabilidad de fractura de cadera, junto con un rango de valores más extendido hacia el riesgo alto. Aunque hay valores extremos en ambos grupos, esta diferencia sugiere una tendencia leve hacia mayor riesgo.

#### 3. Clasificación de riesgo de FRAX según osteosarcopenia.
![clasificacion de riesgo](/outputs/objetivo14_frax_clasificacion_vs_osteosarcopenia.png)

**Interpretación:**
La mayoría de los pacientes con y sin osteosarcopenia se encuentran en el nivel moderado de riesgo. Se observa una mayor presencia relativa del grupo con osteosarcopenia en la categoría alta, mientras que el grupo sin la condición muestra mayor representación en la categoría muy alta. No se aprecia una tendencia clara que relacione directamente la presencia de osteosarcopenia con una mayor estratificación de riesgo de FRAX.

#### Conclusión Objetivo 14:
En términos generales, los resultados no muestran diferencias marcadas en el riesgo de fractura entre pacientes con o sin osteosarcopenia. Si bien el grupo con osteosarcopenia presenta una mediana ligeramente más alta en la probabilidad de fractura de cadera y una mayor representación en la categoría alta del FRAX, estas diferencias no son consistentes ni concluyentes. Por lo tanto, no puede afirmarse que exista una mayor estratificación del riesgo en este grupo con base en los datos disponibles.

---

## Objetivo 15. Identificar a los pacientes que tienen problemas de equilibrio mediante la prueba de Get up and go.

El conjunto de datos no contiene ninguna variable relacionada con esta prueba específica, ni valores equivalentes que permitan inferir su resultado. Por lo tanto no fue posible desarrollar este objetivo dentro del análisis.

---

## Objetivo 16. Comparar los niveles de vitamina D con la densidad mineral ósea y los valores de sarcopenia.

El conjunto de datos no incluye ninguna medición bioquímica o clínica correspondiente a vitamina D. Dado que esta variable no se encuentra disponible, no fue posible realizar el análisis propuesto.

---

#### Comentario final.

Este análisis exploratorio se limitó a describir y visualizar los datos disponibles en la muestra proporcionada, con base en los objetivos establecidos. Las conclusiones aquí presentadas se derivan exclusivamente del comportamiento de las variables en el conjunto de datos y no deben interpretarse como juicios clínicos. Cualquier validación o interpretación médica deberá ser realizada por el doctor responsable del estudio.