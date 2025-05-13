# Análisis Exploratorio de Datos en Estudio Clínico de Osteosarcopenia.

Este repositorio contiene el proceso de análisis exploratorio de datos (EDA) aplicado a una muestra clínica en el marco del estudio sobre osteosarcopenia liderado por el Dr. Arturo Rizo Topete. El trabajo fue realizado como colaboración técnica para la futura publicación científica del doctor, e incluye desde la limpieza estructurada de datos hasta la generación de visualizaciones e interpretaciones descriptivas.

---

## Contexto del estudio.

El estudio fue realizado con pacientes del municipio de Escuinapa, Sinaloa, y tiene como objetivo evaluar la coexistencia de sarcopenia y osteporosis u osteopenia, así como su relación con variables funcionales, clínicas y antropométricas. Esta exploración servirá como base para el artículo científico que el Dr. Arturo Rizo publicará próximamente.

## Estructura del repositorio.
````
├── data/
│   ├── raw/              # NO se incluye por privacidad
│   └── cleaned/
│       ├── df_limpio.csv
│       └── df_eda.csv
├── notebooks/
│   ├── data_cleaning.ipynb
│   └── eda.ipynb
├── outputs/
│   └── [gráficas generadas]
├── docs/
│   └── doc_eda.md
│   └── doc_limpieza.md
├── reporte/
│   └── reporte.md
│   └── reporte.html
├── index.html            # redirecciona al informe HTML
├── README.md             # este archivo
````

## Archivos principales.
- `df_limpio.csv`: Versión estructurada y depurada del dataset original, sin información sensible.
- `df_eda.csv`: Subconjunto de variables relevantes para el análisis exploratorio con variables derivadas.
- `data_cleaning.ipynb`: Notebook con la limpieza y transformación estructural de los datos.
- `eda.ipynb`: Notebook con la generación de variables auxiliares y análisis previos al reporte.
- `reporte.html`: Visualización del informe final generado para el doctor responsable del estudio.

## Privacidad de los datos.
Por solicitud del médico responsable, los datos originales en crudo no están incluidos en este repositorio. Estos contienen información sensible y privada de los pacientes. Sólo se comparte el dataset limpio (`df_limpio.csv`) que no contiene información identificable ni datos confidenciales.

## Contacto.
- Linkedin: [Christian Campos Regalado](https://www.linkedin.com/in/christian-campos-regalado/)
- X: [soychriscampos](https://x.com/soychriscampos)

## Licencia
Este proyecto se comparte con fines académicos y profesionales, sin fines de lucro. El contenido puede ser reutilizado siempre que se reconozca la autoría original y no se intente reconstruir o inferir los datos privados del estudio.