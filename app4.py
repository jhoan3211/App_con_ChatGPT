import streamlit as st
import pandas as pd
from io import BytesIO  # Para manejar archivos en memoria
from pandas.errors import EmptyDataError  # Para manejar errores en la carga de Excel

# Verifica si `xlsxwriter` o `openpyxl` está disponible
try:
    import xlsxwriter  # Motor para escribir archivos Excel
except ImportError:
    st.error("Falta el paquete 'xlsxwriter'. Instálalo con 'pip install xlsxwriter'.")
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
Esta aplicación permite calcular el PAPA global y por tipología. Puedes registrar asignaturas manualmente o cargar un archivo Excel con tus notas.
""")

# Inicialización del DataFrame en el estado de sesión
if 'asignaturas' not in st.session_state:
    st.session_state['asignaturas'] = pd.DataFrame(columns=["Asignatura", "Calificación", "Créditos", "Tipología"])

# Función para descargar plantilla
def descargar_plantilla():
    # Crear un DataFrame vacío con las columnas esperadas
    plantilla = pd.DataFrame(columns=["Asignatura", "Calificación", "Créditos", "Tipología"])

    # Guardar el DataFrame en un buffer de bytes como archivo Excel
    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        plantilla.to_excel(writer, index=False, sheet_name='Plantilla')
    buffer.seek(0)

    # Proporcionar un enlace para descargar el archivo
    st.download_button(
        label="Descargar Plantilla Excel",
        data=buffer,
        file_name="plantilla_notas.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

# Función para subir y cargar archivo Excel
def cargar_plantilla():
    archivo_subido = st.file_uploader("Sube tu archivo Excel con las notas", type=["xlsx"])
    if archivo_subido:
        try:
            # Leer el archivo Excel subido
            nuevo_df = pd.read_excel(archivo_subido)

            # Verificar si las columnas requeridas están presentes
            columnas_requeridas = ["Asignatura", "Calificación", "Créditos", "Tipología"]
            if all(col in nuevo_df.columns for col in columnas_requeridas):
                # Actualizar las asignaturas en el estado de sesión
                st.session_state['asignaturas'] = pd.concat([st.session_state['asignaturas'], nuevo_df], ignore_index=True)
                st.success("Archivo cargado y asignaturas registradas correctamente.")
            else:
                st.error(f"El archivo debe contener las columnas: {', '.join(columnas_requeridas)}")
        except Exception as e:
            st.error("Ocurrió un error al procesar el archivo. Por favor, verifica el formato.")

# Función para registrar asignaturas manualmente
def registrar_asignatura():
    # Campos de entrada
    asignatura = st.text_input("Nombre de la asignatura")
    calificacion = st.number_input("Calificación (0-5)", min_value=0.0, max_value=5.0, step=0.1)
    creditos = st.number_input("Créditos", min_value=1, step=1)
    tipologia = st.selectbox("Afecta el PAPA?", ["Si", "No"])
    
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
opcion = st.sidebar.radio("Selecciona una opción", ["Registrar Asignaturas", "Cargar Archivo", "Ver Reportes", "Descargar Plantilla"])

# Lógica de la app
if opcion == "Registrar Asignaturas":
    registrar_asignatura()
    mostrar_asignaturas()
elif opcion == "Cargar Archivo":
    cargar_plantilla()
    mostrar_asignaturas()
elif opcion == "Ver Reportes":
    mostrar_reportes()
elif opcion == "Descargar Plantilla":
    descargar_plantilla()
