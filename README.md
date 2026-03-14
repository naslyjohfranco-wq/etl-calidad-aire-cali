# Stack Tecnológico — Proyecto ETL de Calidad del Aire

## Lenguaje Principal

**Python**

Python será el lenguaje principal para el desarrollo del proceso ETL, debido a su amplio ecosistema para la manipulación de datos, integración con APIs y generación de análisis y visualizaciones.

---

## Extracción de Datos (Extract)

Herramientas utilizadas para obtener datos desde APIs y fuentes abiertas:

- **requests** → Librería utilizada para realizar peticiones HTTP y consumir datos desde APIs públicas relacionadas con la calidad del aire.

---

## Transformación de Datos (Transform)

Librerías utilizadas para la limpieza, procesamiento y transformación de los datos:

- **pandas** → Manipulación, limpieza y transformación de datos tabulares.
- **numpy** → Soporte para operaciones numéricas y cálculos necesarios durante el procesamiento de datos.

Estas herramientas permitirán realizar procesos como:

- Limpieza de datos
- Eliminación de valores nulos
- Conversión de formatos de fecha
- Normalización de datos
- Agregaciones y análisis preliminar

---

## Carga de Datos (Load)

Para la fase de carga, los datos procesados serán almacenados en archivos estructurados para su posterior análisis.

- **pandas** → Utilizado para exportar los datos transformados a formatos como **CSV o Excel**.

---

## Visualización y Análisis de Datos

Librerías utilizadas para el análisis exploratorio y la visualización de los datos de calidad del aire:

- **matplotlib** → Librería para la creación de gráficos y visualizaciones básicas.
- **seaborn** → Librería basada en matplotlib que permite generar visualizaciones estadísticas más avanzadas y estéticas.

---

## Herramientas de Desarrollo

- **VS Code** → Editor de código utilizado para el desarrollo del proyecto.
- **Git** → Sistema de control de versiones para la gestión del código y seguimiento de cambios en el proyecto.
