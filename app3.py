import streamlit as st
import pandas as pd
import datetime

# Configuración inicial
st.set_page_config(page_title="Finanzas Personales", layout="wide")

# Función para inicializar datos
@st.cache_data
def initialize_data():
    return {
        "transactions": pd.DataFrame(columns=["Fecha", "Tipo", "Categoría", "Monto"]),
        "budgets": pd.DataFrame(columns=["Categoría", "Presupuesto Mensual"]),
        "savings_goals": pd.DataFrame(columns=["Meta", "Monto", "Progreso"]),
    }

# Función para agregar una transacción
def add_transaction(data, fecha, tipo, categoria, monto):
    new_transaction = {"Fecha": fecha, "Tipo": tipo, "Categoría": categoria, "Monto": monto}
    data["transactions"] = pd.concat([data["transactions"], pd.DataFrame([new_transaction])], ignore_index=True)
    return data

# Función para agregar o actualizar un presupuesto
def add_budget(data, categoria, presupuesto):
    budgets = data["budgets"]
    if categoria in budgets["Categoría"].values:
        budgets.loc[budgets["Categoría"] == categoria, "Presupuesto Mensual"] = presupuesto
    else:
        new_budget = {"Categoría": categoria, "Presupuesto Mensual": presupuesto}
        budgets = pd.concat([budgets, pd.DataFrame([new_budget])], ignore_index=True)
    data["budgets"] = budgets
    return data

# Función para calcular reportes
def generate_report(data, period="Mensual"):
    transactions = data["transactions"]
    budgets = data["budgets"]

    # Filtro de fecha según el período
    today = datetime.date.today()
    if period == "Semanal":
        start_date = today - datetime.timedelta(days=7)
    else:  # Mensual
        start_date = today.replace(day=1)
    
    filtered_transactions = transactions[transactions["Fecha"] >= str(start_date)]

    # Sumar ingresos y gastos por categoría
    summary = filtered_transactions.groupby(["Tipo", "Categoría"])["Monto"].sum().reset_index()
    budget_summary = budgets.merge(summary[summary["Tipo"] == "Gasto"], on="Categoría", how="left")
    budget_summary["Monto"].fillna(0, inplace=True)
    budget_summary["Diferencia"] = budget_summary["Presupuesto Mensual"] - budget_summary["Monto"]

    return summary, budget_summary

# Inicialización de datos
data = initialize_data()

# Interfaz de usuario
st.title("Gestor de Finanzas Personales")
st.sidebar.header("Opciones")

# Selección de funcionalidad
option = st.sidebar.selectbox("Selecciona una opción:", ["Registrar Transacción", "Definir Presupuesto", "Metas de Ahorro", "Generar Reporte"])

if option == "Registrar Transacción":
    st.header("Registrar Transacción")
    with st.form("transaction_form"):
        fecha = st.date_input("Fecha", value=datetime.date.today())
        tipo = st.selectbox("Tipo", ["Ingreso", "Gasto"])
        categoria = st.text_input("Categoría")
        monto = st.number_input("Monto", min_value=0.0, step=0.01)
        submitted = st.form_submit_button("Registrar")
        if submitted:
            data = add_transaction(data, fecha, tipo, categoria, monto)
            st.success("Transacción registrada exitosamente.")
            st.dataframe(data["transactions"])

elif option == "Definir Presupuesto":
    st.header("Definir Presupuesto")
    with st.form("budget_form"):
        categoria = st.text_input("Categoría")
        presupuesto = st.number_input("Presupuesto Mensual", min_value=0.0, step=0.01)
        submitted = st.form_submit_button("Guardar Presupuesto")
        if submitted:
            data = add_budget(data, categoria, presupuesto)
            st.success("Presupuesto guardado exitosamente.")
            st.dataframe(data["budgets"])

elif option == "Metas de Ahorro":
    st.header("Metas de Ahorro")
    with st.form("savings_form"):
        meta = st.text_input("Meta de Ahorro")
        monto = st.number_input("Monto Objetivo", min_value=0.0, step=0.01)
        progreso = st.number_input("Progreso Actual", min_value=0.0, step=0.01)
        submitted = st.form_submit_button("Guardar Meta")
        if submitted:
            new_goal = {"Meta": meta, "Monto": monto, "Progreso": progreso}
            data["savings_goals"] = pd.concat([data["savings_goals"], pd.DataFrame([new_goal])], ignore_index=True)
            st.success("Meta de ahorro guardada exitosamente.")
            st.dataframe(data["savings_goals"])

elif option == "Generar Reporte":
    st.header("Generar Reporte")
    periodo = st.selectbox("Período", ["Semanal", "Mensual"])
    summary, budget_summary = generate_report(data, period=periodo)

    st.subheader("Resumen de Transacciones")
    st.dataframe(summary)

    st.subheader("Presupuesto vs Real")
    st.dataframe(budget_summary)

    st.download_button(
        "Descargar Reporte",
        data=budget_summary.to_csv(index=False).encode("utf-8"),
        file_name=f"reporte_{periodo.lower()}.csv",
        mime="text/csv",
    )
