import streamlit as st

# Función para realizar la conversión según la categoría y tipo de conversión
def convertir(categoria, tipo_conversion, valor):
    if categoria == "Tiempo":
        if tipo_conversion == "Horas a minutos":
            return valor * 60, "minutos"
        elif tipo_conversion == "Minutos a segundos":
            return valor * 60, "segundos"
        elif tipo_conversion == "Días a horas":
            return valor * 24, "horas"
        elif tipo_conversion == "Semanas a días":
            return valor * 7, "días"

    elif categoria == "Longitud":
        if tipo_conversion == "Pies a metros":
            return valor * 0.3048, "metros"
        elif tipo_conversion == "Metros a pies":
            return valor / 0.3048, "pies"
        elif tipo_conversion == "Pulgadas a centímetros":
            return valor * 2.54, "centímetros"
        elif tipo_conversion == "Centímetros a pulgadas":
            return valor / 2.54, "pulgadas"

    elif categoria == "Peso/Masa":
        if tipo_conversion == "Libras a kilogramos":
            return valor * 0.453592, "kilogramos"
        elif tipo_conversion == "Kilogramos a libras":
            return valor / 0.453592, "libras"
        elif tipo_conversion == "Onzas a gramos":
            return valor * 28.3495, "gramos"
        elif tipo_conversion == "Gramos a onzas":
            return valor / 28.3495, "onzas"

    elif categoria == "Volumen":
        if tipo_conversion == "Galones a litros":
            return valor * 3.78541, "litros"
        elif tipo_conversion == "Litros a galones":
            return valor / 3.78541, "galones"
        elif tipo_conversion == "Pulgadas cúbicas a centímetros cúbicos":
            return valor * 16.387, "centímetros cúbicos"
        elif tipo_conversion == "Centímetros cúbicos a pulgadas cúbicas":
            return valor / 16.387, "pulgadas cúbicas"

    elif categoria == "Velocidad":
        if tipo_conversion == "Millas por hora a kilómetros por hora":
            return valor * 1.60934, "kilómetros por hora"
        elif tipo_conversion == "Kilómetros por hora a metros por segundo":
            return valor / 3.6, "metros por segundo"
        elif tipo_conversion == "Nudos a millas por hora":
            return valor * 1.15078, "millas por hora"
        elif tipo_conversion == "Metros por segundo a pies por segundo":
            return valor * 3.28084, "pies por segundo"

    elif categoria == "Área":
        if tipo_conversion == "Metros cuadrados a pies cuadrados":
            return valor * 10.7639, "pies cuadrados"
        elif tipo_conversion == "Pies cuadrados a metros cuadrados":
            return valor / 10.7639, "metros cuadrados"
        elif tipo_conversion == "Kilómetros cuadrados a millas cuadradas":
            return valor / 2.58999, "millas cuadradas"
        elif tipo_conversion == "Millas cuadradas a kilómetros cuadrados":
            return valor * 2.58999, "kilómetros cuadrados"

    elif categoria == "Energía":
        if tipo_conversion == "Julios a calorías":
            return valor * 0.239006, "calorías"
        elif tipo_conversion == "Calorías a kilojulios":
            return valor * 0.004184, "kilojulios"
        elif tipo_conversion == "Kilovatios-hora a megajulios":
            return valor * 3.6, "megajulios"
        elif tipo_conversion == "Megajulios a kilovatios-hora":
            return valor / 3.6, "kilovatios-hora"

    elif categoria == "Presión":
        if tipo_conversion == "Pascales a atmósferas":
            return valor / 101325, "atmósferas"
        elif tipo_conversion == "Atmósferas a pascales":
            return valor * 101325, "pascales"
        elif tipo_conversion == "Barras a libras por pulgada cuadrada":
            return valor * 14.5038, "libras por pulgada cuadrada"
        elif tipo_conversion == "Libras por pulgada cuadrada a bares":
            return valor * 0.0689476, "bares"

    elif categoria == "Tamaño de datos":
        if tipo_conversion == "Megabytes a gigabytes":
            return valor / 1024, "gigabytes"
        elif tipo_conversion == "Gigabytes a Terabytes":
            return valor / 1024, "terabytes"
        elif tipo_conversion == "Kilobytes a megabytes":
            return valor / 1024, "megabytes"
        elif tipo_conversion == "Terabytes a petabytes":
            return valor / 1024, "petabytes"

    return None, None  # Si la conversión no es válida

# Título de la aplicación
st.title("Conversor Universal de Unidades hecho por Jhoan Ramirez")

# Selección de la categoría
categoria = st.selectbox("Selecciona la categoría de conversión", [
    "Tiempo", "Longitud", "Peso/Masa", "Volumen", "Velocidad", "Área", "Energía", "Presión", "Tamaño de datos"
])

# Selección del tipo de conversión dentro de la categoría seleccionada
if categoria == "Tiempo":
    tipo_conversion = st.selectbox("Selecciona el tipo de conversión", [
        "Horas a minutos", "Minutos a segundos", "Días a horas", "Semanas a días"
    ])
elif categoria == "Longitud":
    tipo_conversion = st.selectbox("Selecciona el tipo de conversión", [
        "Pies a metros", "Metros a pies", "Pulgadas a centímetros", "Centímetros a pulgadas"
    ])
elif categoria == "Peso/Masa":
    tipo_conversion = st.selectbox("Selecciona el tipo de conversión", [
        "Libras a kilogramos", "Kilogramos a libras", "Onzas a gramos", "Gramos a onzas"
    ])
elif categoria == "Volumen":
    tipo_conversion = st.selectbox("Selecciona el tipo de conversión", [
        "Galones a litros", "Litros a galones", "Pulgadas cúbicas a centímetros cúbicos", "Centímetros cúbicos a pulgadas cúbicas"
    ])
elif categoria == "Velocidad":
    tipo_conversion = st.selectbox("Selecciona el tipo de conversión", [
        "Millas por hora a kilómetros por hora", "Kilómetros por hora a metros por segundo", 
        "Nudos a millas por hora", "Metros por segundo a pies por segundo"
    ])
elif categoria == "Área":
    tipo_conversion = st.selectbox("Selecciona el tipo de conversión", [
        "Metros cuadrados a pies cuadrados", "Pies cuadrados a metros cuadrados",
        "Kilómetros cuadrados a millas cuadradas", "Millas cuadradas a kilómetros cuadrados"
    ])
elif categoria == "Energía":
    tipo_conversion = st.selectbox("Selecciona el tipo de conversión", [
        "Julios a calorías", "Calorías a kilojulios", "Kilovatios-hora a megajulios", "Megajulios a kilovatios-hora"
    ])
elif categoria == "Presión":
    tipo_conversion = st.selectbox("Selecciona el tipo de conversión", [
        "Pascales a atmósferas", "Atmósferas a pascales", "Barras a libras por pulgada cuadrada", 
        "Libras por pulgada cuadrada a bares"
    ])
elif categoria == "Tamaño de datos":
    tipo_conversion = st.selectbox("Selecciona el tipo de conversión", [
        "Megabytes a gigabytes", "Gigabytes a Terabytes", "Kilobytes a megabytes", "Terabytes a petabytes"
    ])

# Entrada de valor para la conversión
valor = st.number_input(f"Ingresa el valor a convertir (en {categoria})", min_value=0.0)

# Realizar la conversión y mostrar el resultado
if st.button("Convertir"):
    resultado, unidad_destino = convertir(categoria, tipo_conversion, valor)
    if resultado is not None:
        st.write(f"El resultado de la conversión es: {resultado} {unidad_destino}")
    else:
        st.write("Hubo un error en la conversión. Intenta nuevamente.")
