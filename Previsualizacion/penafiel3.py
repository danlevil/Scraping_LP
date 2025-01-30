import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def analisis_peñafiel3():

    df = pd.read_csv("datosCSV/Empleo_ofertas.csv")  

    df['Experiencia'] = df['Experiencia'].astype(str).str.lower()

    contratos_definidos = ['definido', 'por obra o labor', 'de aprendizaje', 'prestacion de servicios']

    patron_contratos = r'\b(?:' + '|'.join(map(re.escape, contratos_definidos)) + r')\b'

    contrato_definido = df['Experiencia'].str.contains(patron_contratos, regex=True, na=False).sum()
    contrato_indefinido = len(df) - contrato_definido  

    porcentaje_definido = (contrato_definido / len(df)) * 100
    porcentaje_indefinido = (contrato_indefinido / len(df)) * 100

    labels = ["Indefinido", "Definido"]
    values = [porcentaje_indefinido, porcentaje_definido]
    colors = ["#ff9999", "#66b3ff"]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(labels, values, color=colors, edgecolor="black")

    for index, value in enumerate(values):
        ax.text(value - 2, index, f"{value:.2f}%", fontsize=9, ha='right', color="black", fontweight='bold')

    ax.set_title("Distribución de Tipos de Contrato", fontsize=12)
    ax.set_xlabel("Porcentaje de Ofertas", fontsize=12)
    ax.set_xlim(0, 100)
    ax.invert_yaxis() 
    ax.grid(axis='x', linestyle="--", alpha=0.7)

    return plt
