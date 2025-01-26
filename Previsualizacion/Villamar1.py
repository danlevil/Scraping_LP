import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
file_path = '../datosCSV/CompuTrabajo_ofertas.csv'
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv(file_path, encoding='utf-8')

# Filtrar y procesar datos de experiencia
def extraer_años_experiencia(cadena):
    try:
        return int(cadena.split()[0]) if 'anos' in cadena else None
    except:
        return None

df['Años Experiencia'] = df['Experiencia'].apply(extraer_años_experiencia)

# Manejar valores faltantes en la columna Ubicacion
def procesar_ubicacion(ubicacion):
    if ',' in ubicacion:
        return ubicacion.split(',')[1].strip()  # Obtener solo la provincia
    else:
        return "Sin provincia"

df['Provincia'] = df['Ubicacion'].apply(procesar_ubicacion)

# Filtrar filas válidas con años de experiencia no nulos
df_valid = df[df['Años Experiencia'].notnull()]

# Agrupar por provincia y calcular el promedio de años de experiencia
promedios_provincia = df_valid.groupby('Provincia')['Años Experiencia'].mean().sort_values()

# Determinar los colores para las barras
colores = ['red' if promedio >= 4 else 'green' for promedio in promedios_provincia]

# Graficar
plt.figure(figsize=(10, 6))
promedios_provincia.plot(kind='bar', color=colores)
plt.title('Promedio de años de experiencia por provincia', fontsize=14)
plt.xlabel('Provincia', fontsize=12)
plt.ylabel('Años de Experiencia (Promedio)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.text(-0.5, -2, 'Verde: Regular\nRojo: Difícil', fontsize=10, color='black', ha='left', va='top')


plt.tight_layout()
plt.show()
