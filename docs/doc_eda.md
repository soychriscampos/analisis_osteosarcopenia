# Documentación Técnica de Análisis Exploratorio de Datos.

**Notebook:** `notebooks/eda.ipynb`
**Archivo fuente:** `../data/cleaned/df_limpio.csv`
**Archivo generado:** `../data/cleaned/df_eda.csv`

## 1. Introducción.
Este notebook contiene el análisis exploratorio de datos del estudio sobre osteosarcopenia. Parte del archivo previamente limpiado (`df_limpio.csv`) y tiene como objetivo preparar, explorar y derivar variables necesarias para abordar los objetivos específicos del estudio.

## 2. Librerías utilizadas.
````
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
````

## 3. Carga de datos.
Se carga el archivo limpio generado en la etapa de  data cleaning:
````
df = pd.read_csv("../data/cleaned/df_limpio.csv")
````
**Variable creada:** `df` - contiene 53 observaciones con las columnas ya depuradas y estandarizadas.

## 4. Creación de nueva variable: osteosarcopenia.
Se creó una nueva variable llamada `osteosarcopenia` bajo el siguiente criterio:
* Paciente con diagnóstico de sarcopenia distinto de "sin sarcopenia", y
* Clasificación de densidad mineral igual a "osteopenia" u "osteoporosis".

````
cond_sarcopenia = df['nivel_de_sarcopenia'] != 'sin sarcopenia'
cond_osteopenia = df['clasificacion_de_densidad_mineral'].isin(['osteopenia', 'osteoporosis'])

df['osteosarcopenia'] = cond_sarcopenia & cond_osteopenia
````
**Variable creada:** `osteosarcopenia` - indica presencia de osteosarcopenia de acuerdo con criterio combinado.

## 5. Corrección y creación de variables para análisis categórico.
Se ajustaron o derivaron variables necesarias para análisis posteriores. Cada transformación se documenta a continuación:

### 5.1 Variable: `clasificacion_sppb`
Clasificación funcional basada en puntaje de SPPB:
````
def clasificar_sppb(valor):
    if valor >= 10:
        return 'mínima'
    elif valor >= 7:
        return 'leve'
    elif valor >= 5:
        return 'moderada'
    else:
        return 'grave'

df['clasificacion_sppb'] = df['sppb'].apply(clasificar_sppb)
````
**Variable creada:** `clasificacion_sppb` - clasifica a pacientes según su nivel de funcionalidad física basada en SPPB.

## Creación de variables binarias de uso de medicamentos.
Se unificaron las columnas medicamento_1 y medicamento_2 para generar variables binarias de uso de ciertos tipos de medicamentos.
````
df['medicamentos_combinados'] = df[['medicamento_1', 'medicamento_2']].values.tolist()

df['usa_antidiabeticos'] = df['medicamentos_combinados'].apply(
    lambda x: 'antidiabeticos' in x if isinstance(x, list) else False
)
df['usa_antihipertensivos'] = df['medicamentos_combinados'].apply(
    lambda x: 'antihipertensivos' in x if isinstance(x, list) else False
)

df['usa_ansioliticos'] = df['medicamentos_combinados'].apply(
    lambda x: 'hipnoticos o ansioliticos' in x if isinstance(x, list) else False
)
````

**Variables creadas:**
* `usa_antidiabeticos`
* `usa_antihipertensivos`
* `usa_ansioliticos`

Cada una indica si el paciente usa ese tipo de medicamento (valor booleano).

## 7. Exportación del DataFrame transformado.
El DataFrame final, con las variables derivadas necesarias para abordar los objetivos analíticos, fue exportado para su uso posterior.
````
df_eda.to_csv("../data/cleaned/df_eda.csv", index=False)
````

## Resumen:
El análisis exploratorio generó variables clave necesarias para abordar los objetivos específicos del estudio.
* `osteosarcopenia` - condición combinada sarcopenia + alteración ósea.
* `clasificacion_sppb` - niveles funcionaes derivados de SPPB
* `usa_antidiabeticos`, `usa_antihipertensivos`, `usa_ansioliticos` - variables binarias para explorar asociación con medicación.

Estas transformaciones se realizaron sin modificar las variables originales y respetando la estructura del archivo limpio.

El archivo `df_eda.csv` contiene el dataset final para visualización, análisis y modelado posterior.

