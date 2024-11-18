import streamlit as st

# Funciones de conversión
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_a_kelvin(celsius):
    return celsius + 273.15

def kelvin_a_celsius(kelvin):
    return kelvin - 273.15

def pies_a_metros(pies):
    return pies * 0.3048

def metros_a_pies(metros):
    return metros / 0.3048

def pulgadas_a_centimetros(pulgadas):
    return pulgadas * 2.54

def centimetros_a_pulgadas(centimetros):
    return centimetros / 2.54

def libras_a_kilogramos(libras):
    return libras * 0.453592

def kilogramos_a_libras(kilogramos):
    return kilogramos / 0.453592

def onzas_a_gramos(onzas):
    return onzas * 28.3495

def gramos_a_onzas(gramos):
    return gramos / 28.3495

def galones_a_litros(galones):
    return galones * 3.78541

def litros_a_galones(litros):
    return litros / 3.78541

def pulgadas_cubicas_a_centimetros_cubicos(pulgadas_cubicas):
    return pulgadas_cubicas * 16.387

def centimetros_cubicos_a_pulgadas_cubicas(centimetros_cubicos):
    return centimetros_cubicos / 16.387

def horas_a_minutos(horas):
    return horas * 60

def minutos_a_segundos(minutos):
    return minutos * 60

def dias_a_horas(dias):
    return dias * 24

def semanas_a_dias(semanas):
    return semanas * 7

def millas_por_hora_a_kilometros_por_hora(millas_por_hora):
    return millas_por_hora * 1.60934

def kilometros_por_hora_a_metros_por_segundo(kilometros_por_hora):
    return kilometros_por_hora / 3.6

def nudos_a_millas_por_hora(nudos):
    return nudos * 1.15078

def metros_por_segundo_a_pies_por_segundo(metros_por_segundo):
    return metros_por_segundo * 3.28084

def metros_cuadrados_a_pies_cuadrados(metros_cuadrados):
    return metros_cuadrados * 10.7639

def pies_cuadrados_a_metros_cuadrados(pies_cuadrados):
    return pies_cuadrados / 10.7639

def kilometros_cuadrados_a_millas_cuadradas(kilometros_cuadrados):
    return kilometros_cuadrados / 2.58999

def millas_cuadradas_a_kilometros_cuadrados(millas_cuadradas):
    return millas_cuadradas * 2.58999

def julios_a_calorias(julios):
    return julios / 4.184

def calorias_a_kilojulios(calorias):
    return calorias / 239.006

def kilovatios_hora_a_megajulios(kilovatios_hora):
    return kilovatios_hora * 3600 * 1e3

def megajulios_a_kilovatios_hora(megajulios):
    return megajulios / (3600 * 1e3)

def pascales_a_atmosferas(pascales):
    return pascales / 101325

def atmosferas_a_pascales(atmosferas):
    return atmosferas * 101325

def barras_a_libras_por_pulgada_cuadrada(barras):
    return barras * 14.5038

def libras_por_pulgada_cuadrada_a_bares(libras_por_pulgada_cuadrada):
    return libras_por_pulgada_cuadrada / 14.5038

def megabytes_a_gigabytes(megabytes):
    return megabytes / 1024

def gigabytes_a_terabytes(gigabytes):
    return gigabytes / 1024

def kilobytes_a_megabytes(kilobytes):
    return kilobytes / 1024

def terabytes_a_petabytes(terabytes):
    return terabytes / 1024

# Interfaz de usuario
st.title("Conversor Universal")

# Categoría de conversiones
categoria = st.selectbox(
    "Selecciona una categoría de conversión:",
    ("Temperatura", "Longitud", "Peso/Masa", "Volumen", "Tiempo", "Velocidad", "Área", "Energía", "Presión", "Tamaño de datos")
)

if categoria == "Temperatura":
    tipo_conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        ("Celsius a Fahrenheit", "Fahrenheit a Celsius", "Celsius a Kelvin", "Kelvin a Celsius")
    )
    valor = st.number_input("Ingresa el valor a convertir:", type=float)
    
    if tipo_conversion == "Celsius a Fahrenheit":
        resultado = celsius_a_fahrenheit(valor)
    elif tipo_conversion == "Fahrenheit a Celsius":
        resultado = fahrenheit_a_celsius(valor)
    elif tipo_conversion == "Celsius a Kelvin":
        resultado = celsius_a_kelvin(valor)
    else:
        resultado = kelvin_a_celsius(valor)
    
    st.write(f"El resultado es: {resultado}")

elif categoria == "Longitud":
    tipo_conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        ("Pies a metros", "Metros a pies", "Pulgadas a centímetros", "Centímetros a pulgadas")
    )
    valor = st.number_input("Ingresa el valor a convertir:", type=float)
    
    if tipo_conversion == "Pies a metros":
        resultado = pies_a_metros(valor)
    elif tipo_conversion == "Metros a pies":
        resultado = metros_a_pies(valor)
    elif tipo_conversion == "Pulgadas a centímetros":
        resultado = pulgadas_a_centimetros(valor)
    else:
        resultado = centimetros_a_pulgadas(valor)
    
    st.write(f"El resultado es: {resultado}")

elif categoria == "Peso/Masa":
    tipo_conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        ("Libras a kilogramos", "Kilogramos a libras", "Onzas a gramos", "Gramos a onzas")
    )
    valor = st.number_input("Ingresa el valor a convertir:", type=float)
    
    if tipo_conversion == "Libras a kilogramos":
        resultado = libras_a_kilogramos(valor)
    elif tipo_conversion == "Kilogramos a libras":
        resultado = kilogramos_a_libras(valor)
    elif tipo_conversion == "Onzas a gramos":
        resultado = onzas_a_gramos(valor)
    else:
        resultado = gramos_a_onzas(valor)
    
    st.write(f"El resultado es: {resultado}")

# Repetir la estructura anterior para cada categoría...
