# Informe de Inferencial Estadística: Osteosarcopenia

**Responsable del estudio:** Dr. Arturo José Rizo Topete.
**Análisis estadístico:** Christian Campos Regalado.

---

## Introducción
Este documento complementa el análisis exploratorio previamente entregado, integrando pruebas de inferencia estadística sobre una muestra de 53 pacientes. El propósito es validar si los patrones observados entre variables clínicas, funcionales y antropométricas son estadísticamente significativos dentro de la muestra analizada.

Cada apartado corresponde a un objetivo específico del estudio original y aplica técnicas inferenciales acordes al tipo de variable y nivel de medición.

> *Nota: Las pruebas aquí utilizadas no buscan establecer causalidad clínica, sino únicamente identificar diferencias o asociaciones significativas desde el punto de vista estadístico.*

---

## Objetivo 1. Comparar la edad entre pacientes con y sin osteosarcopenia.

**Propósito:** Evaluar si la edad media difiere significativamente entre pacientes con y sin osteosarcopenia, como se sugirió visualmente en el análisis exploratorio.

### Metodología:
- Prueba de normalidad (Shapiro-Wilk).
- Prueba de homogeneidad de varianzas (Levene).
- Prueba t de Student para muestras independientes.
- Prueba de respaldo: Mann-Whitney U.

### Resultados
- Edad media (osteosarcopenia): 67.9 años  
- Edad media (sin osteosarcopenia): 65.0 años  
- t-test: p = 0.119  
- Mann-Whitney U: p = 0.101 

### Conclusión:
No se encontraron diferencias estadísticamente significativas en la edad media entre pacientes con y sin osteosarcopenia. Aunque existe una ligera tendencia hacia mayor edad en el grupo con la condición, esta no alcanza significancia estadística (p > 0.05).

La superposición de valores y el tamaño limitado de la muestra podrían influir en la ausencia de significancia.

---
## Objetivo 3. Asociación entre estado físico y osteosarcopenia.

**Propósito:** Determinar si existe una asociación estadísticamente significativa entre el nivel de estado físico de los pacientes (alto, intermedio, bajo) y la presencia de osteosarcopenia. En el análisis exploratorio se observó que los pacientes con peor estado físico tendían a presentar la condición.

### Metodología:
* Tabla de contingencia entre las variables _clasificación de estado físico_ y _osteosarcopenia_.
* Prueba de independendia: Chi-cuadrado de Pearson.
* Se evaluó si la distribución del estado físico es independiente de la presencia de osteosarcopenia.

### Resultados:
| Estado físico | Sin osteosarcopenia | Con osteosarcopenia |
| ------------- | ------------------- | ------------------- |
| Alto          | 18                  | 3                   |
| Intermedio    | 7                   | 11                  |
| Bajo          | 2                   | 12                  |

* Estadístico chi-cuadrado: 18.73.
* p-valor: 0.0001.
* Grados de libertad: 2.

### Conclusión:
Se encontró una asociación estadísticamente significativa entre el nivel de estado físico y la presencia de osteosarcopenia (p < 0.001).

Los pacientes con osteosarcopenia presentaron una proporción notablemente mayor de casos con estado físico bajo, mientras que aquellos con estado físico alto fueron más frecuentes en el grupo sin la condición. Estos hallazgos respaldan el patrón observado en el análisis exploratorio y sugieren que la funcionalidad física podría estar relacionada con la presencia de osteosarcopenia dentro de esta muestra.

---

## Objetivo 4. Evaluar diferencias en IMC y grasa corporal según osteosarcopenia.

**Propósito:** Evaluar si existen diferencias estadísticamente significativas en el porcentaje de grasa corporal y la clasificación del IMC entre pacientes con y sin osteosarcopenia. En el análisis exploratorio se observaron patrones que sugerían una mayor proporción de grasa y mayor clasificación de IMC en pacientes con la condición.

### Metodología:
Se analizaron dos variables:
1. **Porcentaje de grasa corporal:**
    - Prueba de normalidad: Shapiro-Wilk.
    - Comparación de medias: t de Student para muestras independientes.
    - Prueba no paramétrica de respaldo: Mann-Whitney U.
2. **Clasificación del IMC:**
    - Asociación mediante tabla de contingencia.
    - Prueba de independencia: Chi-cuadrado de Pearson.

### Resultados:
**Porcentaje de grasa corporal:**
- Shapiro-Wilk (osteosarcopenia): p = 0.112.
- Shapiro-Wilk (sin osteosarcopenia): p = 0.224.

_Se cumplió el suspuesto de normalidad para ambos grupos._

- t-test: p = 0.119.
- Mann-Whitney U: p = 0.101.

_No se encontraron diferencias estadísticamente significatvias en el porcentaje de grasa corportal entre los grupos._

**Clasificación del IMC**
| Clasificación IMC | Sin osteosarcopenia | Con osteosarcopenia |
| ----------------- | ------------------- | ------------------- |
| Adecuado          | 2                   | 2                   |
| Sobrepeso         | 14                  | 8                   |
| Obesidad 1        | 7                   | 7                   |
| Obesidad 2        | 3                   | 5                   |
| Obesidad 3        | 1                   | 4                   |

- Chi-cuadrado: 3.92.
- p-valor: 0.417.
- Grados de libertad: 4.

_No se encontró asociación estadísticamente significativa entre la clasificación del IMC y la presencia de osteosarcopenia._

### Conclusión:
Aunque el análisis exploratorio mostró una tendencia visual hacia mayor porcentaje de grasa corporal y clasificaciones más altas de IMC en pacientes con osteosarcopenia, las pruebas inferenciales no encontraron diferencias ni asociaciones estadísticamente significativas (p > 0.05).

Estos resultados sugieren que, en esta muestra, la composición corporal medida mediante estas variables no se comporta como un diferenciador concluyente de osteosarcopenia desde el punto de vista estadístico.

---

## Objetivo 6. Relación entre nivel de funcionalidad física (SPPB) y osteosarcopenia.

**Propósito:** Evaluar si existe una asociación estadísticamente significativa entre el nivel de funcionalidad física —clasificado mediante la prueba SPPB en cuatro categorías— y la presencia de osteosarcopenia. En el análisis exploratorio se observó que los niveles funcionales más bajos eran más frecuentes en pacientes con la condición.

### Metodología:
- Se utilizó la variable _sppb categoria_ con cuatro niveles: mínima, leve, moderada, y grave.
- Se comparó con la variable _osteosarcopenia_.
- Se construyó una tabla de contingencia.
- Se aplicó una prueba de independencia chi-cuadrado de Pearson para evaluar si la distribución de los niveles funcionales difiere según la presencia de la condición.

### Resultados:
| Nivel SPPB | Sin osteosarcopenia | Con osteosarcopenia |
| ---------- | ------------------- | ------------------- |
| Mínima     | 18                  | 3                   |
| Leve       | 6                   | 9                   |
| Moderada   | 2                   | 9                   |
| Grave      | 1                   | 5                   |

- Estadístico chi-cuadrado: 18.42.
- p-valor: 0.0004.
- Grados de libertad: 3.

### Conclusión:
Se encontró una asocación estadísticamente significativa entre el nivel de funcionalidad física (SPPB) y la presencia de osteosarcopenia (p < 0.001).

Los pacientes con osteosarcopenia mostraron una mayor proporción de casos con funcionalidad reducida (niveles moderado y grave), mientras que aquellos sin la condición se concentraron en los niveles de funcionalidad mínima. Esto respalda el patrón observado en el análisis exploratorio y sugiere que el desempeño físico modedido por la prueba SPPB está relacionado con la condición dentro de esta muestra clínica.

---

## Objetivo 7. Comparación de masa muscular según nivel de sarcopenia.

**Propósito:** Evaluar si existen diferencias estadísticamente significativas en la masa muscular absoluta entre los diferentes niveles de sarcopenia (sin, leve, moderada, severa). En el análisis exploratorio se observaron diferencias en las medianas entre grupos, aunque no se identificó un patrón progresivo claro.

### Metodología:
- Variable dependiente: _masa muscular absoluta_ (kg).
- Variable independiente: _nivel de sarcopenia_ (cuatro grupos).
- Se aplicó la prueba de normalidad Shapiro-Wilk por grupo.
- Al no cumplirse el supuesto de normalidad en todos los grupos, se utilizó la prueba no paramétrica de Kruskal-Wallis para comparar distribuciones entre los grupos independientes.

### Resultados.
**Prueba de normalidad (Shapiro-Wilk por grupo):**
- Sin sarcopenia: p = 0.001 no normal.
- Leve: p = 0.541 normal.
Moderada: p = 0.473 normal.
Severa: p = 0.786 normal.

_Al menos uno de los grupos no presenta distribución normal, por lo tanto se aplicó una prueba no paramétrica._

**Prueba Kruskal-Wallis:**
- Estadístico H: 11.07.
- p-valor: 0.011.

_El resultado indica que existen diferencias estadísticamente significativas en la masa muscular entre al menos dos de los niveles de sarcopenia (p < 0.05)._

### Conclusión:
Se encontraron diferencias estadísticamente significativas en la masa muscular absoluta entre los distintos niveles de sarcopenia (p = 0.011).

Estos resultados respaldan principalmente lo observado en el análisis exploratorio: si bien no se identificó una disminución progresiva clara en la masa muscular al avanzar en los niveles de sarcopenia, las diferencias entre grupos no son atribuibles al azar dentro de esta muestra.

Este hallazgo sugiere que la masa muscular está relacionada con el grado de sarcopenia en los pacientes, aunque su comportamiento no sigue un patrón completamente lineal.

---

## Objetivo 11. Comparación de escalas de funcionalidad (Katz y Lawton) según osteosarcopenia.

**Propósito:** Evaluar si existen diferencias estadísticamente significativas en los puntajes de las escalas funcionales Katz y Lawton entre pacientes con y sin osteosarcopenia. En el análisis exploratorio, la escala Lawton mostró mayor dispersión en el grupo con osteosarcopenia, mientras que la escala Katz evidenció un efecto techo, con la mayoría de los pacientes concentrados en el valor máximo.

### Metodología:
- Variables analizadas:
    - _Puntaje de Katz_ (0 a 6): mide actividades básicas de la vida diaria.
    - _Resultado de lawton_ (0 a 8): mide actividades instrumentales.
- Comparación entre dos grupos:
    - Pacientes con osteosarcopenia.
    - Pacientes sin osteosarcopenia.
- Prueba estadística: Mann-Whitney U, al tratarse de puntuaciones ordinales con posibles distribuciones no normales.

### Resultados:
**Katz:**
- Estadístico U: 296.0.
- p-valor: 0.078.

_No se encontró una diferencia estadísticamente significativa en el puntwaje de Katz entre ambos grupos (p > 0.05)._

**Lawton:**
- Estadístico U: 215.0.
- p-valor: 0.003.

_Se encontró una diferencia estadísticamente significativa en el puntaje de Lawton entre pacientes con y sin osteosarcopenia (p < 0.01>)._

### Conclusión:
El análisis inferencial confirmó que los pacientes con osteosarcopenia presentan una menor funcionalidad en actividades instrumentales según la escala de Lawton (p = 0.003). Este resultado coincide con lo observado visualmente en el EDA, donde el grupo con la condición mostró mayor dispersión y tendencia a menores puntajes.

En contraste, la escaa Katz no mostró diferencias estadísticamente significativas entre los grupos (p = 0.078), lo cual es consistente con el efecto techo observado en el análisis exploratorio.

Estos hallazgos sugieren que, dentro de esta muestra, la escala Lawton es más sensible que Katz para captar diferencias funcionales asociadas a la presencia de osteosarcopenia.

---
## Objetivo 12. Relación entre tiempo de ejercicio y presencia de sarcopenia u osteoporosis.

**Propósito:** Explorar si existe una asociación estadísticamente significativa entre el nivel de actividad física reportado (clasificado según tiempo semanal de ejercicio) y la presencia de sarcopenia u osteoporosis. En el análisis exploratorio se observaron tendencias visuales en ambos casos, con mayor prevalencia de condiciones musculoesqueléticas entre quienes reportaban no hacer ejercicio.

### Metodología:
- Variable ordinal _tiempo de ejercicio_.
- Condiciones analizadas por separado:
    - Sarcopenia (presencia).
    - Osteoporosis (presencia).
- Prueba estadística: Chi-cuadrado de independencia.
- Se construyeron dos tablas de contingencia y se evaluó la independencia entre las variables en cada caso.

### Resultados
**Ejercico vs Sarcopenia**
| Tiempo de ejercicio | Con sarcopenia |
| ------------------- | -------------- |
| No                  | 29             |
| 30–60 mins          | 4              |
| 61–120 mins         | 3              |
| 121–180 mins        | 9              |
| Más de 180 mins     | 8              |

- Chi-cuadrado: 0.00.
- p-valor: 1.000.
- Grados de libertad: 0.

_No se pudo calcular diferencia entre grupos, ya que todos los casos correspondieron al grupo con sarcopenia, impiediendo una comparación válida._

**Ejercicio vs Osteoporosis**
| Tiempo de ejercicio | Sin osteoporosis | Con osteoporosis |
| ------------------- | ---------------- | ---------------- |
| No                  | 18               | 11               |
| 30–60 mins          | 3                | 1                |
| 61–120 mins         | 3                | 0                |
| 121–180 mins        | 6                | 3                |
| Más de 180 mins     | 5                | 3                |

- Chi-cuadrado: 1.94.
- p-valor: 0.748.
- Grados de libertad: 4.

_No se encontró asociación estadísticamente significativa entre el nivel de ejercicio y la presencia de osteoporosis (p > 0.05)._

### Conclusión:
A pesar de que el análisis exploratorio sugirió posibles asociaciones entre menor nivel de ejercicio y mayor prevalencia de sarcopenia u osteoporosis, el análisis inferencial no encontró diferencias estadísticamente significativas.

En el caso de sarcopenia, los datos disponibles no permitieron realizar una comparación válida entre grupos. Para osteoporosis, aunque huno una mayor proporción de pacientes con la condición en la categoría "no ejercicio", esta diferencia no fue significativa (p = 0.748)

Estos resultados deben interpretarse con cautela y podrían estar influenciados por el tamaño reducido de la muestra o la distribución desigual de los casos en algunas categorías.

---

## Objetivo 13. Asociación entre uso de medicamentos y osteosarcopenia.

**Propósito:** Explorar si existe una asociación estadísticamente significativa entre el uso de tres tipos de medicamentos y la presencia de osteosarcopenia. Los grupos analizados fueron:

- Antidiabéticos.
- Antihipertensivos.
- Ansiolíticos o hipnóticos.

En el análisis exploratorio se observaron diferencias en la distribución del uso de estos medicamentos entre los grupos, especialmente en el caso de antidiabéticos y ansiolíticos.

### Metodología:
- Se construyó una tabla de contingencia para cada tipo de medicamentos y la variable _osteosarcopenia_.
- Se aplicó una prueba de independencia chi-cuadrado de Pearson para evaluar si el uso del medicamento está asociado con la condición.

### Resultados.
**Uso de antidiabéticos**
| Uso de antidiabéticos | Sin osteosarcopenia | Con osteosarcopenia |
| --------------------- | ------------------- | ------------------- |
| No                    | 21                  | 13                  |
| Sí                    | 6                   | 13                  |

- Chi-cuadrado: 3.32.
- p-valor: 0.069.
_No se encontró una asociación estadísticamente significativa al nivel convencional (p < 0.05), aunque se observó una tendencia que podría ser relevante clínicamente._

**Uso de antihipertensivos**
| Uso de antihipertensivos | Sin osteosarcopenia | Con osteosarcopenia |
| ------------------------ | ------------------- | ------------------- |
| No                       | 15                  | 16                  |
| Sí                       | 12                  | 10                  |

- Chi-cuadrado: 0.03.
- p-valor: 0.871.

_No se observó asociación significativa entre el uso de antihipertensivos y la presencia de osteosarcopenia._

**Uso de ansiolíticos**
| Uso de ansiolíticos | Sin osteosarcopenia | Con osteosarcopenia |
| ------------------- | ------------------- | ------------------- |
| No                  | 25                  | 23                  |
| Sí                  | 2                   | 3                   |

- Chi-cuadrado: 0.002.
- p-valor: 0.965.

_Tampoco se encontró asocación significativa entre el uso de ansiolíticos y la presencia de la condición._

### Conclusión:
Dentro de esta muestra, no se encontraron asociaciones estadísticamente significativas entre el uso de antidiabéticos, antihipertensivos o ansiolíticos y la presencia de osteosarcopenia.

El uso de antidiabéticos mostró una diferencia más marcada entre grupos, aunque el resultado no alcanzó significancia estadística (p = 0.069). Este patrón podría justificar un análisis más profundo con una muestra más amplia.

---

## Objetivo 14. Comparación del riesgo de fractura (FRAX) según presencia de osteosarcopenia.

**Propósito:** Evaluar si existen diferencias estadísticamente significativas en el riesgo estimado de fractura entre pacientes con y sin osteosarcopenia, utilizando los dos indicadores continuo proporcionados por el modelo FRAX:

- Probabilidad de fractura por fragilidad.
- Probabilidad de fractura de cadera.

En el análisis exploratorio, se observaron diferencias leves en la mediana, pero sin patrones concluyentes.

### Metodología:
- Variables continuas analizadas:
    - Probabilidad de fractura por fragilidad.
    - Probrabilidad de fractura de cadera.
- Grupos comparados:
    - Pacientes con osteosarcopenia.
    - Pacientes sin osteosarcopenia.
- Se evaluó la normalidad de ambas variables por grupo mediante la prueba de Shapiro-Wilk.
- Al no cumplirse el supuesto de normalidad en ninguno de los casos (p < 0.01), se aplicó la prueba no paramétrica de Mann-Whitney U como método principal.

### Resultados:
**Riesgo de fractura por fragilidad**
- Prueba de normalidad: p < 0.005 en ambos grupos, distribución no normal.
- t-test: p = 0.622.
- Mann-Whitney U: p = 0.682.

_No se encontraron diferencias estadísticamente significativas en la probabilidad de fractura por fragilidad entre los grupos (p > 0.05)._

**Riesgo de fractura de cadera**
- Prueba de normalidad: p < 0.001 en ambos grupos, distribución no normal.
- t-test: p = 0.817.
- Mann-Whitney U: p = 0.331.

_Tampoco se observaron diferencias estadísticamente significativas en la probabilidad de fractura de cadera (p > 0.05)._

### Conclusión:
Dentro de esta muestra, no se encontraron diferencias estadísticamente significativas en los valores del modelo FRAX entre pacientes con y sin osteosarcopenia, ni en la probabilidad de fractura por fragilidad ni en la de fractura de cadera.

Aunque en el análisis exploratorio se observaron tendencias leves, los resultados inferenciales no respaldan una relación concluyente entre la condición osteosarcopénica y un mayor riesgo de fractura según estos indicadores.

---

## Conclusión general.

El presente análisis de inferencia estadística contempla el estudio exploratorio de osteosarcopenia mediante la aplicación de pruebas estadísticas formales que permiten evaluar si las diferencias observadas entre grupos son atribuibles al azar o estadísticamente significativas dentro de la muestra analizada.

De los catorce objetivos abordados en el EDA, diex permitieron aplicar pruebas inferenciales. Los resultados más relevantes fueron los siguientes:

- Se encotnraron asociasiones estadísticamente significativas entre la osteosarcopenia y variables funcionales como el estado físico, el nivel de funcionalidad SPPB, y el puntaje Lawton, lo que respalda una relación entre esta condición y la pérdida de autonomía o capacidad funcional.
- También se identificaron diferencias significativas en la masa muscular absoluta según el nivel de sarcopenia, lo que sugiere un vínculo claro entre el diagnóstico clínico y las medidas antropométricas de masa muscular.
- Por el contrario,  no se encontraron diferencias significativas en variables como la edad, el riesgo de fractura (FRAX), el procentaje de grasa corporal, la clasificación del IMC, o el uso de medicamentos, a pesar de algunas tendencias observadas visualmente en el análisis exploratorio.
- En varios casos, la ausencia de significancia estadística puede estar influenciada por el tamaño reducido de la muestra, la concentración de valores (efectos techo) o la distribución no uniforme de las categorías.

Este análisis refuerza y delimita los hallazgos exploratorios, y proporciona evidencia técnica adicional para apoyar futuras decisiones clínicas o líneas de investigación. Las asociaciones identificadas deben interpretarse dentro del contexto clínico y metodológico del estudio, y no deben considerarse concluyentes sin un respaldo externo o una muestra más amplia.