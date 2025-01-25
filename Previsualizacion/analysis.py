import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re

PATH_BuscoJobsCSV     = "datosCSV/BuscoJobs_ofertas.csv"
PATH_ComputrabajoCSV  = "datosCSV/CompuTrabajo_ofertas.csv"
PATH_InfoJobsCSV      = "datosCSV/InfoJobs_ofertas.csv" #España
PATH_EmpleosCSV      = "datosCSV/Empleo_ofertas.csv"  #Colombia

df = pd.read_csv(PATH_ComputrabajoCSV) # Cargar el archivo CSV

# Función para extraer la experiencia numérica
def extraer_experiencia(exp):
    if '-' in exp:  # Manejar rangos como '2-3 años'
        bajo, alto = map(float, exp.split('-')[:2])
        return (bajo + alto) / 2  # Tomar el promedio
    elif '+' in exp:  # Manejar '10+ años'
        return float(exp.split('+')[0])
    else:  # Manejar números simples
        return float(''.join(filter(str.isdigit, exp)))

# Función para limpiar la columna 'Ubicacion'
def limpiar_ubicacion(ubicacion):
    # Usar una expresión regular para eliminar números flotantes al principio y espacios/tabulaciones
    ubicacion_limpia = re.sub(r'^\d+(,\d+)?\s+', '', ubicacion.strip())
    return ubicacion_limpia

# Función  para dividir los conocimientos por comas, limpiar espacios y manejar títulos/columnas con dos puntos
def obtener_totales_conocimientos(conocimientos):
    conocimientos_totales = []
    for lista_conocimientos in conocimientos.str.split(','):
        for conocimiento in lista_conocimientos:
            # Eliminar espacios y cualquier texto inicial con dos puntos
            conocimiento_limpio = conocimiento.strip().split(':')[-1].strip()
            conocimientos_totales.append(conocimiento_limpio)
    return conocimientos_totales

# Función para recortar las etiquetas si son más largas que el límite
def acortar_etiqueta(etiqueta, longitud_max=15):
    if len(etiqueta) > longitud_max:
        return etiqueta[:longitud_max] + "..."
    return etiqueta

# Graficar los conocimientos más comunes
def conocimientos_mas_comunes(fig, ax):
    conocimientos = df['Conocimientos'].dropna() # Eliminar filas con valores faltantes en la columna 'Conocimientos'
    conteo_conocimientos = Counter(obtener_totales_conocimientos(conocimientos)) # Contar los conocimientos más comunes
    conocimientos_mas_comunes = conteo_conocimientos.most_common(10)  # Top 10 conocimientos
    etiquetas, valores = zip(*conocimientos_mas_comunes) # Preparar datos para la visualización

    ax.bar(etiquetas, valores, color='skyblue', edgecolor='black')
    ax.set_title('Top 10 Conocimientos Más Comunes', fontsize=16)
    ax.set_xlabel('Conocimientos', fontsize=12)
    ax.set_ylabel('Frecuencia', fontsize=12)
    ax.tick_params(axis='x', rotation=90)
    fig.tight_layout()

# Gráfico de caja para 'Experiencia_Numérica'
def experiencia_por_ubicacion(fig, ax):
    df['Ubicacion'] = df['Ubicacion'].dropna().apply(limpiar_ubicacion).apply(acortar_etiqueta) # Aplicar la función de limpieza a la columna 'Ubicacion'
    df['Experiencia_Numérica'] = df['Experiencia'].apply(extraer_experiencia) # Crear una nueva columna con la experiencia numérica

    df.boxplot(column='Experiencia_Numérica', by='Ubicacion', ax=ax, grid=False, showmeans=True)
    ax.set_title('Distribución de experiencia por ubicación')
    ax.set_xlabel('Ubicación', fontsize=12)
    ax.set_ylabel('Experiencia (Numérica)', fontsize=12)
    ax.tick_params(axis='x', rotation=90)
    fig.tight_layout()

fig, axs = plt.subplots(1, 2, figsize=(10, 6))


conocimientos_mas_comunes(fig, axs[0])
experiencia_por_ubicacion(fig, axs[1])
fig.suptitle('Análisis CompuTrabajo', fontsize=16)
plt.show()
