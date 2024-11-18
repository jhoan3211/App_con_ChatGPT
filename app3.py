import streamlit as st
import pandas as pd

# Simulación de datos de ejemplo en pandas para fines demostrativos
data = {
    'Fecha': ['2024-11-01', '2024-11-02', '2024-11-07', '2024-11-10', '2024-11-15'],
    'Ingreso': [200, 300, 150, 400, 250],
    'Gasto': [50, 100, 80, 120, 90]
}

# Crear el DataFrame
finanzas_df = pd.DataFrame(data)

# Convertir la columna 'Fecha' a datetime
finanzas_df['Fecha'] = pd.to_datetime(finanzas_df['Fecha'])

# Almacenamos el DataFrame en el estado de la sesión para fines de ejemplo
if 'finanzas' not in st.session_state:
    st.session_state['finanzas'] = {'ingresos': finanzas_df}

# Solicitar al usuario las fechas de inicio y fin para el reporte
semana_inicio = st.date_input("Fecha de inicio de la semana")
semana_fin = st.date_input("Fecha de fin de la semana")

# Asegúrate de que las fechas de inicio y fin sean del tipo correcto
semana_inicio = pd.to_datetime(semana_inicio)
semana_fin = pd.to_datetime(semana_fin)

# Generar reportes de ingresos semanales
def generar_reportes():
    # Filtrar los ingresos dentro del rango de fechas
    ingresos_semanales = st.session_state['finanzas']['ingresos'][st.session_state['finanzas']['ingresos']["Fecha"].between(semana_inicio, semana_fin)]

    # Calcular el total de los ingresos dentro del rango
    total_ingresos = ingresos_semanales['Ingreso'].sum()

    st.write(f"Total de ingresos entre {semana_inicio.date()} y {semana_fin.date()}: {total_ingresos}")

# Botón para generar el reporte
if st.button("Generar reporte semanal"):
    generar_reportes()
