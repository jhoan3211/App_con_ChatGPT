import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Inicialización de variables y almacenamiento de datos
if 'finanzas' not in st.session_state:
    st.session_state['finanzas'] = {
        'ingresos': pd.DataFrame(columns=["Fecha", "Categoría", "Monto"]),
        'gastos': pd.DataFrame(columns=["Fecha", "Categoría", "Monto"]),
        'presupuestos': pd.DataFrame(columns=["Mes", "Categoría", "Monto"]),
        'metas_ahorro': pd.DataFrame(columns=["Mes", "Meta de ahorro", "Monto"])
    }

# Títulos y descripción
st.title("App de Finanzas Personales")
st.write("Registra tus ingresos, gastos, presupuestos y metas de ahorro. Esta aplicación generará reportes semanales y mensuales.")

# Menú de navegación
opcion = st.sidebar.radio("Selecciona una opción", ["Registrar Datos", "Ver Reportes"])

# Función para registrar ingresos, gastos, presupuestos y metas de ahorro
def registrar_datos():
    tipo = st.selectbox("¿Qué deseas registrar?", ["Ingreso", "Gasto", "Presupuesto", "Meta de Ahorro"])

    if tipo == "Ingreso":
        fecha = st.date_input("Fecha", datetime.today())
        categoria = st.text_input("Categoría (Ej. Sueldo, Freelance, etc.)")
        monto = st.number_input("Monto", min_value=0.0, format="%.2f")
        if st.button("Registrar Ingreso"):
            st.session_state['finanzas']['ingresos'] = pd.concat([
                st.session_state['finanzas']['ingresos'],
                pd.DataFrame([[fecha, categoria, monto]], columns=["Fecha", "Categoría", "Monto"])
            ], ignore_index=True)
            st.success("Ingreso registrado exitosamente.")
    
    elif tipo == "Gasto":
        fecha = st.date_input("Fecha", datetime.today())
        categoria = st.text_input("Categoría (Ej. Alquiler, Alimentación, etc.)")
        monto = st.number_input("Monto", min_value=0.0, format="%.2f")
        if st.button("Registrar Gasto"):
            st.session_state['finanzas']['gastos'] = pd.concat([
                st.session_state['finanzas']['gastos'],
                pd.DataFrame([[fecha, categoria, monto]], columns=["Fecha", "Categoría", "Monto"])
            ], ignore_index=True)
            st.success("Gasto registrado exitosamente.")
    
    elif tipo == "Presupuesto":
        mes = st.selectbox("Selecciona el mes", ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"])
        categoria = st.text_input("Categoría (Ej. Alimentación, Transporte, etc.)")
        monto = st.number_input("Monto Presupuestado", min_value=0.0, format="%.2f")
        if st.button("Registrar Presupuesto"):
            st.session_state['finanzas']['presupuestos'] = pd.concat([
                st.session_state['finanzas']['presupuestos'],
                pd.DataFrame([[mes, categoria, monto]], columns=["Mes", "Categoría", "Monto"])
            ], ignore_index=True)
            st.success("Presupuesto registrado exitosamente.")
    
    elif tipo == "Meta de Ahorro":
        mes = st.selectbox("Selecciona el mes", ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"])
        monto = st.number_input("Monto Meta de Ahorro", min_value=0.0, format="%.2f")
        if st.button("Registrar Meta de Ahorro"):
            st.session_state['finanzas']['metas_ahorro'] = pd.concat([
                st.session_state['finanzas']['metas_ahorro'],
                pd.DataFrame([[mes, monto]], columns=["Mes", "Meta de ahorro", "Monto"])
            ], ignore_index=True)
            st.success("Meta de Ahorro registrada exitosamente.")

# Función para generar los reportes
def generar_reportes():
    # Reporte semanal y mensual
    st.subheader("Reportes de Finanzas")
    
    # Filtrar datos por fecha
    fecha_hoy = datetime.today()
    semana_inicio = fecha_hoy - timedelta(days=fecha_hoy.weekday())  # Lunes de esta semana
    semana_fin = semana_inicio + timedelta(days=6)  # Domingo de esta semana
    
    # Filtrar datos semanales
    ingresos_semanales = st.session_state['finanzas']['ingresos'][st.session_state['finanzas']['ingresos']["Fecha"].between(semana_inicio, semana_fin)]
    gastos_semanales = st.session_state['finanzas']['gastos'][st.session_state['finanzas']['gastos']["Fecha"].between(semana_inicio, semana_fin)]
    
    # Reporte mensual
    mes_actual = fecha_hoy.strftime("%B")
    ingresos_mensuales = st.session_state['finanzas']['ingresos'][st.session_state['finanzas']['ingresos']["Fecha"].dt.month == fecha_hoy.month]
    gastos_mensuales = st.session_state['finanzas']['gastos'][st.session_state['finanzas']['gastos']["Fecha"].dt.month == fecha_hoy.month]
    
    # Calcular el total de ingresos y gastos
    total_ingresos_semanales = ingresos_semanales["Monto"].sum()
    total_gastos_semanales = gastos_semanales["Monto"].sum()
    total_ingresos_mensuales = ingresos_mensuales["Monto"].sum()
    total_gastos_mensuales = gastos_mensuales["Monto"].sum()
    
    # Mostrar reportes semanales y mensuales
    st.write("### Reporte Semanal")
    st.write(f"Total Ingresos: ${total_ingresos_semanales:.2f}")
    st.write(f"Total Gastos: ${total_gastos_semanales:.2f}")
    st.write(f"Diferencia: ${total_ingresos_semanales - total_gastos_semanales:.2f}")
    
    st.write("### Reporte Mensual")
    st.write(f"Total Ingresos: ${total_ingresos_mensuales:.2f}")
    st.write(f"Total Gastos: ${total_gastos_mensuales:.2f}")
    st.write(f"Diferencia: ${total_ingresos_mensuales - total_gastos_mensuales:.2f}")

# Ejecución según la opción seleccionada
if opcion == "Registrar Datos":
    registrar_datos()
elif opcion == "Ver Reportes":
    generar_reportes()
