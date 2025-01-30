import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re

def analisis_peñafiel1():
    PATH_EmpleosCSV      = "datosCSV/Empleo_ofertas.csv"  

    df = pd.read_csv(PATH_EmpleosCSV) 

    def clasificar_experiencia(exp):
        if pd.isna(exp) or re.search(r'sin experiencia|no aplica', str(exp).lower()):
            return 'Sin experiencia'
        exp = exp.lower()
        if re.search(r'sin experiencia|no aplica', exp):
            return 'Sin experiencia'
        elif re.search(r'\b([1-3])\b', exp):
            return 'Poca experiencia (1-3 años)'
        elif re.search(r'\b([4-6])\b', exp):
            return 'Mediana experiencia (4-6 años)'
        elif re.search(r'\b(10|[7-9])\b', exp):
            return 'Mucha experiencia (7-10 años)'
        else:
            return 'Sin experiencia'

    df['Nivel_Experiencia'] = df['Experiencia'].apply(clasificar_experiencia)

    # Calcular el porcentaje
    total_ofertas = len(df)
    conteo_niveles = df['Nivel_Experiencia'].value_counts()

    # Crear gráfico de pastel
    labels = conteo_niveles.index
    sizes = conteo_niveles.values
    colors = ['#66b3ff', '#ff9999', '#99ff99', '#ffcc99']
    explode = [0.05] * len(sizes)

    plt.figure(figsize=(10, 8))
    wedges, texts, autotexts = plt.pie(
        sizes,
        labels=None,  
        autopct=lambda p: f'{p:.1f}%\n({int(p * total_ofertas / 100)})',  
        colors=colors,
        startangle=90,
        explode=explode,
        wedgeprops={'edgecolor': 'black'}, 
        pctdistance=0.8 
    )

    plt.legend(
        wedges,
        [f'{label} ({count})' for label, count in zip(labels, sizes)],
        title="Niveles de experiencia",
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1),
        fontsize=10
    )

    plt.title('Distribución de Niveles de Experiencia en las Ofertas')
    plt.tight_layout()
    return plt

if __name__ == "__main__":
    plt= analisis_peñafiel1()
    plt.show()