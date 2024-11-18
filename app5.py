import streamlit as st

# Título y descripción de la app
st.title("La Importancia de la Inteligencia Artificial para el Mundo; por chatGPT asistido por Jhoan Ramirez")
st.write("""
    La Inteligencia Artificial (IA) es una de las tecnologías más transformadoras de nuestro tiempo. 
    Está afectando a múltiples sectores, desde la salud hasta la educación, pasando por el medio ambiente y la economía. 
    En esta aplicación exploraremos cómo la IA está cambiando el mundo y mejorando nuestras vidas en diferentes áreas.
""")

# Menú de navegación
opcion = st.sidebar.radio("Selecciona una sección para explorar", [
    "Introducción a la IA", 
    "IA en la Salud", 
    "IA en la Educación", 
    "IA en el Medio Ambiente", 
    "IA en la Economía", 
    "IA en la Tecnología"
])

# Función para mostrar información sobre la IA
def mostrar_introduccion():
    st.subheader("¿Qué es la Inteligencia Artificial?")
    st.write("""
        La **Inteligencia Artificial** se refiere a la simulación de procesos de inteligencia humana mediante 
        algoritmos y sistemas computacionales. En otras palabras, la IA permite que las máquinas realicen tareas 
        que normalmente requieren inteligencia humana, como el aprendizaje, el razonamiento y la resolución de problemas.
        
        Con el avance de la tecnología y el aumento de la capacidad de procesamiento, la IA está alcanzando niveles 
        de sofisticación que están cambiando la forma en que vivimos y trabajamos. La IA no solo mejora la eficiencia, 
        sino que también ofrece soluciones a desafíos globales complejos.
    """)

def mostrar_ia_en_salud():
    st.subheader("IA en la Salud")
    st.write("""
        La **Inteligencia Artificial** está transformando el sector salud de maneras que antes parecían impensables. 
        Gracias a la IA, los diagnósticos médicos son más rápidos y precisos, y los tratamientos se personalizan según 
        las características individuales de cada paciente.

        Algunos avances importantes de la IA en la salud incluyen:
        - **Diagnóstico médico asistido por IA**: Herramientas de IA pueden analizar imágenes médicas (como radiografías y resonancias magnéticas) para detectar enfermedades como el cáncer.
        - **Medicina personalizada**: Los algoritmos de IA pueden ayudar a crear tratamientos personalizados basados en el perfil genético de un paciente.
        - **Asistentes virtuales para la salud**: Los chatbots de IA ofrecen asesoramiento médico instantáneo, ayudando a aliviar la carga de los sistemas de salud.
    """)

def mostrar_ia_en_educacion():
    st.subheader("IA en la Educación")
    st.write("""
        La **IA en la educación** está revolucionando la forma en que aprendemos y enseñamos. Los sistemas de 
        aprendizaje adaptativo basados en IA personalizan el contenido para cada estudiante, adaptándose a sus 
        necesidades y ritmo de aprendizaje.

        La IA también está mejorando la eficiencia de los docentes y el acceso a la educación:
        - **Plataformas educativas inteligentes**: Los sistemas de IA pueden crear planes de estudio personalizados y proporcionar retroalimentación instantánea a los estudiantes.
        - **Evaluación automática**: Las herramientas de IA pueden calificar exámenes y trabajos de manera más rápida y objetiva.
        - **Accesibilidad**: Los asistentes de IA pueden ayudar a estudiantes con discapacidades mediante tecnología de asistencia, como el reconocimiento de voz y la conversión de texto a voz.
    """)

def mostrar_ia_en_medio_ambiente():
    st.subheader("IA en el Medio Ambiente")
    st.write("""
        La **Inteligencia Artificial** juega un papel crucial en la lucha contra el cambio climático y en la protección 
        del medio ambiente. La IA puede analizar grandes cantidades de datos ambientales y predecir cambios en el 
        clima, lo que ayuda a tomar decisiones más informadas para mitigar el impacto del cambio climático.

        Algunos ejemplos de cómo la IA está ayudando al medio ambiente incluyen:
        - **Monitoreo ambiental**: Sensores y sistemas de IA pueden analizar datos sobre calidad del aire, temperatura, y contaminación, proporcionando información valiosa para la toma de decisiones políticas.
        - **Energía renovable**: La IA optimiza el uso de energías renovables, como la energía solar y eólica, ajustando la producción según la demanda y las condiciones meteorológicas.
        - **Agricultura de precisión**: La IA ayuda a los agricultores a utilizar recursos de manera más eficiente, reduciendo el desperdicio y promoviendo prácticas agrícolas sostenibles.
    """)

def mostrar_ia_en_economia():
    st.subheader("IA en la Economía")
    st.write("""
        La **IA en la economía** está transformando la manera en que las empresas operan y los mercados funcionan. 
        Desde la automatización de procesos hasta la creación de nuevos modelos de negocio, la IA está impulsando el crecimiento económico global.

        Algunos impactos clave de la IA en la economía incluyen:
        - **Automatización industrial**: La IA y la robótica están reemplazando trabajos manuales, aumentando la eficiencia y reduciendo los costos.
        - **Creación de nuevos empleos**: Aunque la automatización elimina ciertos trabajos, también crea nuevos roles en sectores como la programación, la ciencia de datos y la ciberseguridad.
        - **Optimización de procesos empresariales**: Las empresas están utilizando la IA para predecir demandas, gestionar inventarios y mejorar la atención al cliente mediante chatbots y asistentes virtuales.
    """)

def mostrar_ia_en_tecnologia():
    st.subheader("IA en la Tecnología")
    st.write("""
        La **IA** está en el corazón de muchas de las innovaciones tecnológicas que estamos viendo hoy. 
        Desde la automatización de tareas hasta la creación de sistemas autónomos, la IA está impulsando la evolución de la tecnología.

        Algunas áreas donde la IA está avanzando rápidamente incluyen:
        - **Automóviles autónomos**: Los vehículos autónomos están utilizando IA para detectar obstáculos, planificar rutas y tomar decisiones en tiempo real.
        - **Sistemas de recomendación**: Plataformas como Netflix, YouTube y Spotify utilizan IA para sugerir contenido a los usuarios basado en su historial y preferencias.
        - **Ciberseguridad**: Los sistemas de IA están mejorando la seguridad en línea mediante la detección de patrones inusuales y la identificación de posibles amenazas en tiempo real.
    """)

# Mostrar el contenido según la opción seleccionada
if opcion == "Introducción a la IA":
    mostrar_introduccion()
elif opcion == "IA en la Salud":
    mostrar_ia_en_salud()
elif opcion == "IA en la Educación":
    mostrar_ia_en_educacion()
elif opcion == "IA en el Medio Ambiente":
    mostrar_ia_en_medio_ambiente()
elif opcion == "IA en la Economía":
    mostrar_ia_en_economia()
elif opcion == "IA en la Tecnología":
    mostrar_ia_en_tecnologia()
