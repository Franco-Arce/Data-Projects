import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from db_manager import add_postulation, delete_postulation, get_postulations
import datetime

# Configuración de la aplicación
st.set_page_config(page_title="Codeflow Postulaciones", page_icon=":diamonds:", layout="wide")

# Estilo general
st.markdown(
    """
    <style>
    .main { background-color: #000000; }
    .css-18e3th9 { color: #ffffff; } /* Ajusta el color de los textos y títulos */
    .css-1v3fvcr { background-color: #2a0a3b; } /* Color de fondo para elementos secundarios */
    .css-16huue1 { color: #9b4d9c; } /* Color de los textos en botones y enlaces */
    </style>
    """,
    unsafe_allow_html=True
)

# Título de la aplicación
st.title("💎 Codeflow Postulaciones")

# Cargar los datos
data = get_postulations()

# Dividir la pantalla en dos columnas
col1, col2 = st.columns([1, 2])

with col1:
    # Sección para agregar una nueva postulación
    st.header("Agregar Nueva Postulación")
    with st.form(key='add_postulation_form'):
        titulo = st.text_input('Título del Puesto')
        estado = st.selectbox('Estado', ['Por postular', 'Postulado', 'Rechazado', 'Avanzado'])
        fecha = st.date_input('Fecha de Postulación', datetime.date.today())
        plataforma = st.text_input('Plataforma')
        empresa = st.text_input('Empresa')
        enlace = st.text_input('Enlace a la Oferta Laboral')
        submit_button = st.form_submit_button(label='Agregar')

    if submit_button:
        # Convertir la fecha en un objeto datetime.date
        fecha_obj = fecha
        add_postulation(titulo, estado, fecha_obj, plataforma, empresa, enlace)
        st.success(f"Se ha agregado la postulación para {titulo}.")
        # Actualizar la tabla automáticamente sin recargar la página
        data = get_postulations()

    # Botón para actualizar la tabla
    if st.button('Actualizar Tabla'):
        # Actualizar la tabla sin necesidad de recargar toda la página
        data = get_postulations()

with col2:
    # Mostrar las postulaciones en una tabla
    st.header("📊 Todas las Postulaciones")
    
    if not data.empty:
        # Agregar columna con enlaces a la oferta laboral
        data['Enlace'] = data['enlace'].apply(lambda x: f'<a href="{x}" target="_blank">Ver Oferta</a>')

        # Mostrar la tabla con formato HTML
        st.write(
            data.to_html(escape=False, index=False, 
                        classes='table table-dark table-striped'), 
            unsafe_allow_html=True
        )
        
        # Sección para eliminar una postulación
        st.header("Eliminar Postulación")
        titulo_a_eliminar = st.selectbox(
            'Selecciona el título de la postulación que deseas eliminar:',
            options=data['titulo'].unique()  # Asegúrate de usar el nombre correcto de la columna
        )
        if st.button('Eliminar Postulación'):
            delete_postulation(titulo_a_eliminar)
            st.success(f"La postulación de {titulo_a_eliminar} ha sido eliminada.")
            # Actualizar la tabla automáticamente sin recargar la página
            data = get_postulations()
    else:
        st.write("No hay postulaciones cargadas.")

# Sección de análisis de datos
st.header("📊 Análisis de Datos de Postulaciones")

# Dividir la pantalla en dos columnas para gráficos
col1, col2 = st.columns(2)

with col1:
    # Estadísticas por estado (gráfico de barras)
    st.subheader("Distribución por Estado")
    estado_counts = data['estado'].value_counts().sort_index()

    # Crear gráfico de barras atractivo
    fig_bars, ax_bars = plt.subplots(figsize=(5, 3))  # Tamaño ajustado
    sns.barplot(x=estado_counts.index, y=estado_counts.values, ax=ax_bars, palette='viridis')
    ax_bars.set_title('Distribución por Estado', fontsize=14, color='#ffffff')
    ax_bars.set_xlabel('Estado', fontsize=12, color='#ffffff')
    ax_bars.set_ylabel('Número de Postulaciones', fontsize=12, color='#ffffff')
    ax_bars.set_facecolor('#2a0a3b')
    fig_bars.patch.set_facecolor('#000000')
    plt.xticks(rotation=45, color='#ffffff')
    plt.yticks(color='#ffffff')
    plt.grid(True, linestyle='--', alpha=0.5, color='#ffffff')
    # Asegurarse de que el gráfico de barras muestre números enteros
    ax_bars.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: int(x)))

    st.pyplot(fig_bars)

with col2:
    # Estadísticas por fecha (gráfico de líneas)
    st.subheader("Número de Postulaciones por Mes")
    if not data['fecha'].empty:
        # Convertir la columna 'fecha' en formato de fecha ISO
        data['fecha'] = pd.to_datetime(data['fecha'], format="%Y-%m-%d")
        data['Mes'] = data['fecha'].dt.to_period('M').astype(str)
        monthly_counts = data['Mes'].value_counts().sort_index()

        # Asegurarse de que los números sean enteros
        monthly_counts = monthly_counts.astype(int)

        # Crear gráfico de líneas atractivo
        fig_line, ax_line = plt.subplots(figsize=(5, 3))  # Tamaño ajustado
        sns.lineplot(x=monthly_counts.index, y=monthly_counts.values, ax=ax_line, color='#9b4d9c', marker='o')
        ax_line.set_title('Número de Postulaciones por Mes', fontsize=14, color='#ffffff')
        ax_line.set_xlabel('Mes', fontsize=12, color='#ffffff')
        ax_line.set_ylabel('Número de Postulaciones', fontsize=12, color='#ffffff')
        ax_line.set_facecolor('#2a0a3b')
        fig_line.patch.set_facecolor('#000000')
        plt.xticks(rotation=45, color='#ffffff')
        plt.yticks(color='#ffffff')
        plt.grid(True, linestyle='--', alpha=0.5, color='#ffffff')
        # Asegurarse de que el gráfico de líneas muestre números enteros
        ax_line.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: int(x)))

        st.pyplot(fig_line)

# Dividir la pantalla en dos columnas para gráficos adicionales
col1, col2 = st.columns(2)

with col1:
    # Gráfico de torta
    st.subheader("Distribución por Plataforma (Gráfico de Torta)")
    plataforma_counts = data['plataforma'].value_counts()

    # Crear gráfico de torta atractivo
    fig_pie, ax_pie = plt.subplots(figsize=(5, 3))  # Tamaño ajustado para igualar los otros gráficos
    ax_pie.pie(plataforma_counts, labels=plataforma_counts.index, autopct='%1.1f%%', colors=sns.color_palette('viridis', len(plataforma_counts)))
    ax_pie.set_title('Distribución por Plataforma', fontsize=14, color='#ffffff')
    fig_pie.patch.set_facecolor('#000000')
    plt.gca().set_facecolor('#000000')
    plt.xticks(color='#ffffff')
    plt.yticks(color='#ffffff')

    st.pyplot(fig_pie)

with col2:
    # Gráfico de barras apiladas por plataforma y estado
    st.subheader("Postulaciones por Plataforma y Estado")
    platform_state_counts = pd.crosstab(data['plataforma'], data['estado'])

    # Crear gráfico de barras apiladas atractivo
    fig_stacked, ax_stacked = plt.subplots(figsize=(5, 3))  # Tamaño ajustado
    platform_state_counts.plot(kind='bar', stacked=True, ax=ax_stacked, colormap='viridis')
    ax_stacked.set_title('Postulaciones por Plataforma y Estado', fontsize=14, color='#ffffff')
    ax_stacked.set_xlabel('Plataforma', fontsize=12, color='#ffffff')
    ax_stacked.set_ylabel('Número de Postulaciones', fontsize=12, color='#ffffff')
    ax_stacked.set_facecolor('#2a0a3b')
    fig_stacked.patch.set_facecolor('#000000')
    plt.xticks(rotation=45, color='#ffffff')
    plt.yticks(color='#ffffff')
    plt.grid(True, linestyle='--', alpha=0.5, color='#ffffff')

    st.pyplot(fig_stacked)
