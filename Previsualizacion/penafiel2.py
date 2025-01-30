import pandas as pd
import re
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

def analisis_peñafiel2():
    PATH_EmpleosCSV = "datosCSV/Empleo_ofertas.csv" 
    PATH_ComputrabajoCSV  = "datosCSV/CompuTrabajo_ofertas.csv"

    # Lista de lenguajes de programación más comunes
    lenguajes_programacion = [
        "python", "java", "c++", "c#", "javascript", "typescript", "php", "ruby",
        "swift", "kotlin", "go", "r", "perl", "dart", "scala", "matlab", "rust", "sql",
        "bash", "shell", "html", "css", "react", "angular", "vue", "node", "flutter",
        "tecnologia de la informacion", "lean", "agile", "wordpress", "mysql",
        "objective-c", "node.js", "microsoft excel", "excel", "microsoft office",
        "impala", "angularjs", "angular", "oracle", "sql server", "dot net"
    ]

    df = pd.read_csv(PATH_EmpleosCSV)
    df2 = pd.read_csv(PATH_ComputrabajoCSV)

    def extraer_lenguajes(descripcion):
        if pd.isna(descripcion):
            return [] 
        descripcion = descripcion.lower()  
        encontrados = [lang for lang in lenguajes_programacion if re.search(rf'\b{lang}\b', descripcion)]
        return encontrados

    df['Lenguajes'] = df['Descripcion'].apply(extraer_lenguajes)
    df2['Lenguajes'] = df2['Conocimientos'].apply(extraer_lenguajes)


    conteo_colombia = Counter([lang for sublist in df['Lenguajes'] for lang in sublist])
    conteo_ecuador = Counter([lang for sublist in df2['Lenguajes'] for lang in sublist])

    # Crear un DataFrame comparativo con los lenguajes encontrados en ambos países
    todas_las_tecnologias = set(conteo_ecuador.keys()).union(set(conteo_colombia.keys()))

    todas_las_tecnologias = sorted(list(todas_las_tecnologias)) 

    comparativo = pd.DataFrame({
        'Ecuador': [conteo_ecuador.get(tec, 0) for tec in todas_las_tecnologias],
        'Colombia': [conteo_colombia.get(tec, 0) for tec in todas_las_tecnologias]
    }, index=todas_las_tecnologias)

    # Calcular la diferencia en demanda (Ecuador - Colombia)
    comparativo['Diferencia'] = comparativo['Ecuador'] - comparativo['Colombia']

    # Ordenar por mayor diferencia positiva
    comparativo = comparativo.sort_values(by='Diferencia', ascending=False)

    top_10_colombia = comparativo['Colombia'].sort_values(ascending=False).head(10)
    top_10_ecuador = comparativo['Ecuador'].sort_values(ascending=False).head(10)

    top_lenguajes = comparativo.head(6).index

    valores_ecuador = comparativo.loc[top_lenguajes, 'Ecuador'].values
    valores_colombia = comparativo.loc[top_lenguajes, 'Colombia'].values

    valores_max = max(valores_ecuador.max(), valores_colombia.max())
    valores_ecuador = valores_ecuador / valores_max
    valores_colombia = valores_colombia / valores_max

    # Crear ángulos para el radar
    num_vars = len(top_lenguajes)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    # Cerrar la forma del radar
    valores_ecuador = np.concatenate((valores_ecuador, [valores_ecuador[0]]))
    valores_colombia = np.concatenate((valores_colombia, [valores_colombia[0]]))
    angles += angles[:1]

    fig, axs = plt.subplots(1, 2, figsize=(14, 6))

    # --- Gráfico 1: Scatter Top 10 Colombia ---
    axs[0].scatter(top_10_colombia.index, top_10_colombia.values, color='red', s=100, edgecolors='black')

    for lang, demand in zip(top_10_colombia.index, top_10_colombia.values):
        axs[0].text(lang, demand + 2, f"{demand}", fontsize=12, ha='center', color='black')

    axs[0].set_title("Top 10 Lenguajes más Demandados en Colombia", fontsize=14)
    axs[0].set_xlabel("Lenguajes de Programación", fontsize=12)
    axs[0].set_ylabel("Cantidad de Ofertas", fontsize=12)
    axs[0].tick_params(axis='x', rotation=45)
    axs[0].grid(axis='y', linestyle='--', alpha=0.7)

    # --- Gráfico 2: Scatter Top 10 Ecuador ---
    axs[1].scatter(top_10_ecuador.index, top_10_ecuador.values, color='blue', s=100, edgecolors='black')

    for lang, demand in zip(top_10_ecuador.index, top_10_ecuador.values):
        axs[1].text(lang, demand + 2, f"{demand}", fontsize=12, ha='center', color='black')

    axs[1].set_title("Top 10 Lenguajes más Demandados en Ecuador", fontsize=14)
    axs[1].set_xlabel("Lenguajes de Programación", fontsize=12)
    axs[1].set_ylabel("Cantidad de Ofertas", fontsize=12)
    axs[1].tick_params(axis='x', rotation=45)
    axs[1].grid(axis='y', linestyle='--', alpha=0.7)


    # --- Grafico de radar ---
    fig, ax_radar = plt.subplots(figsize=(10, 6), subplot_kw=dict(polar=True))

    ax_radar.plot(angles, valores_ecuador, label='Ecuador', color='blue', linewidth=2, linestyle='solid', alpha=0.7)
    ax_radar.fill(angles, valores_ecuador, color='blue', alpha=0.2)
    ax_radar.plot(angles, valores_colombia, label='Colombia', color='red', linewidth=2, linestyle='dashed', alpha=0.7)
    ax_radar.fill(angles, valores_colombia, color='red', alpha=0.2)

    ax_radar.set_xticks(angles[:-1])
    ax_radar.set_xticklabels(top_lenguajes, fontsize=11, ha='center')

    for angle, value, label in zip(angles[:-1], valores_ecuador[:-1], top_lenguajes):
        ax_radar.text(angle, value + 0.1, f"{int(value * valores_max)}", fontsize=10, ha='center', color='blue', fontweight='bold')
    for angle, value, label in zip(angles[:-1], valores_colombia[:-1], top_lenguajes):
        ax_radar.text(angle, value + 0.1, f"{int(value * valores_max)}", fontsize=10, ha='center', color='red', fontweight='bold')

    ax_radar.set_title("Comparación de Lenguajes más Demandados en Ecuador vs. Colombia", fontsize=14, pad=20)
    ax_radar.legend(loc="upper right", bbox_to_anchor=(1.2, 1.1))

    plt.tight_layout()
    return plt

if __name__ == "__main__":
    plt= analisis_peñafiel2()
    plt.show()