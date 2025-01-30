import pandas as pd
import matplotlib.pyplot as plt

def analisis_provincias_experiencia():
    file_path = 'datosCSV/CompuTrabajo_ofertas.csv'
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv(file_path, encoding='utf-8')

    def extraer_años_experiencia(cadena):
        try:
            return int(cadena.split()[0]) if 'anos' in cadena else None
        except:
            return None

    df['Años Experiencia'] = df['Experiencia'].apply(extraer_años_experiencia)

    def procesar_ubicacion(ubicacion):
        if ',' in ubicacion:
            return ubicacion.split(',')[1].strip()   
        else:
            return "Sin provincia"

    df['Provincia'] = df['Ubicacion'].apply(procesar_ubicacion)

    df_valid = df[df['Años Experiencia'].notnull()]

    promedios_provincia = df_valid.groupby('Provincia')['Años Experiencia'].mean().sort_values()

    colores = ['red' if promedio >= 4 else 'green' for promedio in promedios_provincia]

    plt.figure(figsize=(10, 6))
    promedios_provincia.plot(kind='bar', color=colores)
    plt.title('Promedio de años de experiencia por provincia', fontsize=14)
    plt.xlabel('Provincia', fontsize=12)
    plt.ylabel('Años de Experiencia (Promedio)', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.text(-0.5, -2, 'Verde: Regular\nRojo: Difícil', fontsize=10, color='black', ha='left', va='top')


    plt.tight_layout()
    return plt

if __name__ == "__main__":
    plt= analisis_provincias_experiencia()
    plt.show()