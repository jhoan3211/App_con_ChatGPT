import streamlit as st
import pandas as pd
import datetime

# Configuración inicial
st.set_page_config(page_title="Finanzas Personales por Jhoan Ramirez", layout="wide")

# Inicialización de datos en session_state
if "transactions" not in st.session_state:
    st.session_state["transactions"] = pd.DataFrame(columns=["Fecha", "Tipo", "Categoría", "Monto"])
if "budgets" not in st.session_state:
    st.session_state["budgets"] = pd.DataFrame(columns=["Categoría", "Presupuesto Mensual"])
if "savings_goals" not in st.session_state:
    st.session_state["savings_goals"] = pd.DataFrame(columns=["Meta", "Monto", "Progreso"])

# Función para agregar una transacción
def add_transaction(fecha, tipo, categoria, monto):
    new_transaction = {"Fecha": fecha, "Tipo": tipo, "Categoría": categoria, "Monto": monto}
    st.session_state["transactions"] = pd.concat(
        [st.session_state["transactions"], pd.DataFrame([new_transaction])], ignore_index=True
    )

# Función para agregar o actualizar un presupuesto
def add_budget(categoria, presupuesto):
    budgets = st.session_state["budgets"]
    if categoria in budgets["Categoría"].values:
        budgets.loc[budgets["Categoría"] == categoria, "Presupuesto Mensual"] = presupuesto
    else:
        new_budget = {"Categoría": categoria, "Presupuesto Mensual": presupuesto}
        st.session_state["budgets"] = pd.concat([budgets, pd.DataFrame([new_budget])], ignore_index=True)

# Función para agregar una meta de ahorro
def add_savings_goal(meta, monto, progreso):
    new_goal = {"Meta": meta, "Monto": monto, "Progreso": progreso}
    st.session_state["savings_goals"] = pd.concat(
        [st.session_state["savings_goals"], pd.DataFrame([new_goal])], ignore_index=True
    )

# Función para calcular reportes
def generate_report(period="Mensual"):
    transactions = st.session_state["transactions"]
    budgets = st.session_state["budgets"]

    # Asegurarse de que la columna 'Fecha' sea de tipo datetime
    if not transactions.empty:
        transactions["Fecha"] = pd.to_datetime(transactions["Fecha"], errors="coerce")

    # Filtro de fecha según el período
    today = datetime.date.today()
    if period == "Semanal":
        start_date = today - datetime.timedelta(days=7)
    else:  # Mensual
        start_date = today.replace(day=1)

    # Filtrar transacciones por fecha
    filtered_transactions = transactions[transactions["Fecha"] >= pd.Timestamp(start_date)]

    # Sumar ingresos y gastos por categoría
    summary = filtered_transactions.groupby(["Tipo", "Categoría"])["Monto"].sum().reset_index()

    # Comparar con presupuestos
    budget_summary = budgets.merge(summary[summary["Tipo"] == "Gasto"], on="Categoría", how="left")
    budget_summary["Monto"].fillna(0, inplace=True)
    budget_summary["Diferencia"] = budget_summary["Presupuesto Mensual"] - budget_summary["Monto"]

    return summary, budget_summary

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
            add_transaction(fecha, tipo, categoria, monto)
            st.success("Transacción registrada exitosamente.")
            st.dataframe(st.session_state["transactions"])

elif option == "Definir Presupuesto":
    st.header("Definir Presupuesto")
    with st.form("budget_form"):
        categoria = st.text_input("Categoría")
        presupuesto = st.number_input("Presupuesto Mensual", min_value=0.0, step=0.01)
        submitted = st.form_submit_button("Guardar Presupuesto")
        if submitted:
            add_budget(categoria, presupuesto)
            st.success("Presupuesto guardado exitosamente.")
            st.dataframe(st.session_state["budgets"])

elif option == "Metas de Ahorro":
    st.header("Metas de Ahorro")
    with st.form("savings_form"):
        meta = st.text_input("Meta de Ahorro")
        monto = st.number_input("Monto Objetivo", min_value=0.0, step=0.01)
        progreso = st.number_input("Progreso Actual", min_value=0.0, step=0.01)
        submitted = st.form_submit_button("Guardar Meta")
        if submitted:
            add_savings_goal(meta, monto, progreso)
            st.success("Meta de ahorro guardada exitosamente.")
            st.dataframe(st.session_state["savings_goals"])

elif option == "Generar Reporte":
    st.header("Generar Reporte")
    periodo = st.selectbox("Período", ["Semanal", "Mensual"])
    summary, budget_summary = generate_report(period=periodo)

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

