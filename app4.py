import streamlit as st
import pandas as pd

# Función para calcular el PAPA global y por tipología
def calcular_papa(df):
    # PAPA Global
    suma_ponderada = (df["Calificación"] * df["Créditos"]).sum()
    suma_creditos = df["Créditos"].sum()
    papa_global = suma_ponderada / suma_creditos if suma_creditos != 0 else 0

    # PAPA por tipología
    papa_por_tipologia = df.groupby("Tipología").apply(
        lambda x: (x["Calificación"] * x["Créditos"]).sum() / x["Créditos"].sum() if x["Créditos"].sum() != 0 else 0
    ).reset_index(name="PAPA")

    return papa_global, papa_por_tipologia

# Título y descripción de la app
st.title("Cálculo de PAPA (Promedio Acumulado de Ponderación Académica)")
st.write("""
Esta aplicación permite calcular el PAPA global y por tipología de asignatura. 
Para cada asignatura, ingresa su calificación, los créditos y su tipología (teórica, práctica, etc.).
""")

# Inicialización del DataFrame en el estado de sesión
if 'asignaturas' not in st.session_state:
    st.session_state['asignaturas'] = pd.DataFrame(columns=["Asignatura", "Calificación", "Créditos", "Tipología"])

# Función para registrar asignaturas
def registrar_asignatura():
    # Campos de entrada
    asignatura = st.text_input("Nombre de la asignatura")
    calificacion = st.number_input("Calificación (0-10)", min_value=0.0, max_value=10.0, step=0.1)
    creditos = st.number_input("Créditos", min_value=1, step=1)
    tipologia = st.selectbox("Tipología de asignatura", ["Teórica", "Práctica", "Optativa", "Obligatoria"])
    
    if st.button("Registrar Asignatura"):
        # Registrar la asignatura en el DataFrame
        nueva_asignatura = pd.DataFrame([[asignatura, calificacion, creditos, tipologia]],
                                        columns=["Asignatura", "Calificación", "Créditos", "Tipología"])
        st.session_state['asignaturas'] = pd.concat([st.session_state['asignaturas'], nueva_asignatura], ignore_index=True)
        st.success(f"Asignatura {asignatura} registrada correctamente!")

# Mostrar las asignaturas registradas
def mostrar_asignaturas():
    st.write("### Asignaturas Registradas")
    st.dataframe(st.session_state['asignaturas'])

# Cálculo y visualización del PAPA
def mostrar_reportes():
    if len(st.session_state['asignaturas']) == 0:
        st.write("Aún no se han registrado asignaturas. Por favor, ingrese al menos una asignatura para calcular el PAPA.")
        return

    # Calcular el PAPA global y por tipología
    papa_global, papa_por_tipologia = calcular_papa(st.session_state['asignaturas'])

    # Mostrar el PAPA global
    st.write(f"### PAPA Global: {papa_global:.2f}")

    # Mostrar el PAPA por tipología
    st.write("### PAPA por Tipología de Asignatura")
    st.dataframe(papa_por_tipologia)

# Menú lateral para elegir la funcionalidad
opcion = st.sidebar.radio("Selecciona una opción", ["Registrar Asignaturas", "Ver Reportes"])

# Lógica de la app
if opcion == "Registrar Asignaturas":
    registrar_asignatura()
    mostrar_asignaturas()
elif opcion == "Ver Reportes":
    mostrar_reportes()
