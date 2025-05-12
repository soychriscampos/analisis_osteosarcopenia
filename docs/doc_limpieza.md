# Documentación Técnica de Limpieza de Datos.

**Notebook:** `notebooks/data_cleaning.ipynb`
**Archivo fuente:** `../data/raw/tabla osteosarcopenia escui.xlsx`
**Archivo generado:** `../data/cleaned/df_limpio.csv`

## 1. Introducción.

Este notebook realiza la limpieza de datos del estudio sobre osteosarcopenia realizado por el Dr. Arturo Rizo Topete en pacientes del municipio de Escuinapa, Sinaloa. 

El archivo original fue entregado en formato `.xlsx` sin tratamiento previo y contiene aproximadamente 75 columnas con variables clínicas, antropométricas y funcionales.


## 2. Librerías utilizadas.
````
import pandas as pd
import numpy as np
````

### 3. Carga de datos.
Las dos primeras filas del archivo original contenían encabezados decorativos o sin estructura útil, por lo que fueron omitidas durante la carga del archivo.
````
path = "../data/raw/tabla osteosarcopenia escui.xlsx"
df = pd.read_excel(path, skiprows=2)
````
**Variable creada** `df` - contiene los datos clínicos, funcionales y antropométricos.

### 4. Limpieza de nombres de columnas.
Se estandarizaron los nombres de los atributos:
* Eliminación de espacios en blanco.
* Sustitución de espacios por guiones bajos `_`
* Eliminación de puntos.
* Conversión a minúsculas.

````
df.columns = (
    df.columns
    .str.strip()
    .str.replace(" ", "_")
    .str.replace(".", "")
    .str.lower()
)
````

### 5. Eliminación y renombramiento de columnas.
Se eliminaron columnas irrelevantes por estar vacías, duplicadas o no aportar al análisis.
````
df = df.drop(columns=[
    '#', 'nombre', 'rango_de_edad', 'lugar', '3_ms', 'resultado2', 'sarcopenia1',
    'grosor', 'sarcopenia2', 'medicamento_3', 'medicamento_4'])
````

Se renombraron columnas para mejorar su legilibidad:
````
df = df.rename(columns={
    'imc1': 'clas_imc',
    'resultado': 'grasa_resultado',
    'masa_muscular_absoluta,_kg': 'masa_muscular_absoluta',
    'imme:_kg/m2': 'imme',
    'resultado1': 'imme_resultado',
    'puntaje_sarc_-f': 'sarc_f_puntaje',
    'resultado_de_sarc-f': 'sarc_f_resultado',
    'tiempo_de_ejercico': 'tiempo_de_ejercicio',
    'probabilida_de_fractura_por_fragilidad': 'probabilidad_de_fractura_por_fragilidad',
    'probabilida_de_fractura_de_cadera': 'probabilidad_de_fractura_de_cadera'
})
````

### 6. Limpieza de valores y corrección de datos.
* Se conservaron únicamente las primeras 53 filas que contienen datos válidos de pacientes.
````
df = df.iloc[:53, :]
````
* Se corrigeron errores de captura numérica en la columna `columna`, donde valores iniciados con `.` debían ser negativos. Mediante la función `corregir_puntos_erroneos`.

* Se transformaron algunas en metros a centímetros mediante la función `corregir_altura`.
Se reemplazaron valores textuales como "Incapaz" con `NaN` para preservar tipo numérico.
* Se limpiaron errores ortográficos y tipográficos en varias columnas.

**Funciones personalizadas aplicadas:**
* `corregir_puntos_erroneos()`
* `corregir_altura()`

Correcciones específicas:
````
df['columna'] = df['columna'].apply(corregir_puntos_erroneos)
df['prueba_de_la_silla'] = df['prueba_de_la_silla'].replace('Incapaz', np.nan)
df['altura_en_cm'] = df['altura_en_cm'].apply(corregir_altura)
df['altura_mencionada'] = df['altura_mencionada'].apply(corregir_altura)
df['clasificacion_de_estado_fisico'] = df['clasificacion_de_estado_fisico'].apply(lambda x: x.split(' ', 1)[-1] if isinstance(x, str) else x)
df['tiempo_de_ejercicio'] = df['tiempo_de_ejercicio'].replace({
    '61 -120 mins': '61 - 120 mins',
    '121 -180mins': '121 - 180 mins'
})
df['nivel_de_sarcopenia'] = df['nivel_de_sarcopenia'].replace({
    'Sarcopenoa Leve': 'sarcopenia leve'
})
df['medicamento_1'] = df['medicamento_1'].replace({
    'hipnoticos o ancioliticos': 'hipnoticos o ansioliticos'
})
df['medicamento_2'] = df['medicamento_2'].replace({
    'hipnoticos o ancioliticos': 'hipnoticos o ansioliticos'
})
````

**Limpieza general de texto:**
````
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.strip().str.lower()
````

## 7. Creación de categorías ordenadas.
Se definió un diccionario con el orden jerárquico para variables categóricas.
````
categorias_ordenadas = {
    'clas_imc': ['adecuado', 'sobrepeso', 'obesidad 1', 'obesidad 2', 'obesidad 3'],
    'grasa_resultado': ['normal', 'bueno', 'alta', 'peligrosamente alta'],
    'imme_resultado': ['normal', 'sarcopenia grado 1', 'sarcopenia grado 2'],
    'estratificacion_de_riesgo': ['baja', 'moderada', 'alta', 'muy alta'],
    'clasificacion_de_estado_fisico' : ['bajo', 'intermedio', 'alto'],
    'fuerza': ['ninguna', 'poca', 'mucha'],
    'caminata': ['ninguna', 'poca', 'mucha'],
    'levantarse': ['ninguna', 'poca', 'mucha'],
    'subir_escaleras': ['ninguna', 'poca', 'mucha'],
    'caidas': ['ninguna', '1 - 3 caidas', '4 o mas caidas'],
    'tiempo_de_ejercicio': ['no', '30 - 60 mins', '61 - 120 mins', '121 - 180 mins','mas de 180 mins'],
    'nivel_de_sarcopenia': ['sin sarcopenia', 'sarcopenia leve', 'sarcopenia moderada', 'sarcopenia severa']
}

for col, orden in categorias_ordenadas.items():
    if col in df.columns:
        df[col] = pd.Categorical(df[col], categories=orden, ordered=True)
````
Esto permite preservar el significado clínico de las categorías en análisis posteriores.

## 8. Exportación de dataset limpio.
El DataFrame final fue exportado a un archivo `.csv` para su análisis epxloratorio.
````
df.to_csv('../data/cleaned/df_limpio.csv', index=False)
````

## Resumen:
El proceso de limpieza incluyó:
* Carga de datos excluyendo encabezados decorativos.
* limpieza y estandarización de nombres de columnas.
* Corrección de valores erróneos y estandarización textual.
* Eliminación de columnas innecesarias.
* Renombramiento para mayor claridad.
* Creación de variables categóricas ordenadas.

No se crearon nuevas variables analíticas en esta etapa. El archivo `df_limpio.csv` representa la versión depurada y lista para el análisis exploratorio.

