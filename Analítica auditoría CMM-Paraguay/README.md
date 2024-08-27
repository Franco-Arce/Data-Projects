
---

# 📊 **Analítica auditoría a CMM, Paraguay Jun_2024** 🌎

Este proyecto aborda el análisis detallado de la baja tasa de retorno de inversión en el mercado paraguayo, identificando posibles fallos estratégicos por parte de los directivos de CMM. A través de una rigurosa limpieza y modelado de datos, se generaron visualizaciones que destacan las principales diferencias entre los mercados de Paraguay, Brasil, y Argentina, enfocándose en la inversión inicial y la ganancia obtenida.

## 📝 **Contexto y Objetivo del Proyecto**

El proyecto fue impulsado por la necesidad de comprender la baja tasa de retorno de inversión en Paraguay, a pesar de que un análisis preliminar no mostró irregularidades contables o financieras significativas. El objetivo fue identificar y demostrar analíticamente si existían factores subyacentes que podrían haber afectado el rendimiento en el mercado paraguayo, y compararlos con otros mercados como Brasil y Argentina.

## 📁 **Fuentes de Datos Utilizadas**

Se utilizaron varias fuentes de datos para este análisis, proporcionadas por diferentes equipos y organismos:

- **Resumen de Ventas en Paraguay:** `sales_in_Paraguay.xlsx` (Ventas por distribuidor y producto).
- **Perfil de Distribuidores en Paraguay:** `distributors_profiles.csv` (Nombre, actividades y años en el mercado de la construcción).
- **Exportaciones a Paraguay:** `exports_to_Paraguay.csv` (Resúmenes y reportes de exportación de materiales).
- **Perfiles de Localidades en Paraguay:** `locations_profiles.csv` (Principales actividades económicas por ciudad, departamento y ciudad con distribuidores).

Adicionalmente, se utilizó información del CNAEP, UNFPA, DGEEC, y el artículo "Mapeo de industrias del Paraguay registradas en el Ministerio de Industria y Comercio" para contextualizar el análisis.

## 🛠️ **Procesos Implementados**

### 1. **Importación y Limpieza de Datos**
   - Se realizó la importación de datos a Google Colaboratory utilizando librerías de Python como `Pandas` y `Numpy`.
   - Se inspeccionaron y limpiaron los datos, eliminando duplicados y columnas innecesarias, y asegurando la relevancia y consistencia de la información.

### 2. **Modelado de Datos**
   - Se estructuraron los datos relevantes en sets adecuados para el análisis.
   - Se validaron las relaciones entre las diferentes variables, preparando los datos para la visualización.

### 3. **Análisis Exploratorio**
   - Se exploraron y analizaron las tendencias en los datos, enfocándose en las diferencias de transacciones, inversión y recuperación de inversión por país.
   - Se identificaron las discrepancias entre las expectativas de ganancia y los resultados reales en cada mercado.

### 4. **Visualización de Resultados**
   - **Gráfico de Inversión vs Ganancia Real:** Mostrando la relación directa entre la inversión inicial y la ganancia obtenida en cada país.
   - **Porcentaje de Recuperación de Inversión por País:** Destacando las diferencias en la recuperación de inversión entre Paraguay, Brasil, y Argentina.
   - **Transacciones por País y Ganancias:** Visualización de la cantidad de transacciones realizadas en cada país y su impacto en las ganancias.
   - **Transacciones por Mes:** Análisis temporal de las transacciones para identificar patrones o tendencias.
   - **Distribuidores y Ciudades Alcanzadas:** Muestra la cobertura geográfica y la cantidad de distribuidores activos en cada mercado.

## 🔍 **Conclusión**

El análisis concluye que la ganancia obtenida en todos los países fue menor al 1% respecto a la inversión inicial, con Brasil mostrando una diferencia significativa en la cantidad de transacciones (253% más que en Argentina), pero con una recuperación de inversión similar a la de Argentina. Este hallazgo sugiere la necesidad de auditar las operaciones en Brasil para entender mejor el desbalance entre el esfuerzo comercial y los resultados financieros.

## 📈 **Resultados Presentados en Looker**

La visualización final de los datos se realizó en Looker, donde se presentaron los hallazgos de manera clara y accesible para la toma de decisiones estratégicas.

## 📌 **Tecnologías y Herramientas Utilizadas**

- **Limpieza y Modelado de Datos:** Python, Pandas, Numpy.
- **Visualización:** Matplotlib, Seaborn, Looker.
- **Colaboración y Documentación:** Google Colaboratory, Google Sheets.



## 🗂️ **Estructura del Proyecto**

- **/data** - Carpeta que contiene los datasets utilizados.
- **/notebooks** - Notebooks de Google Colaboratory con el análisis y visualización de datos.
- **/visualizations** - Carpeta con las imágenes de los gráficos generados.
- **README.md** - Este archivo.

## 🤝 **Colaboradores**

Este proyecto fue desarrollado por [Franco Arce] como parte de un análisis estratégico para CMM, en el cursado de la carrera Big Data de Codo a Codo. 

---
