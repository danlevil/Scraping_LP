import pandas as pd
import matplotlib.pyplot as plt

categorias = {
    "net": ["net", ".net"],
    "java": ["java"],
    "backend": ["backend"],
    "mobile": ["mobile", "android", "kotlin", "swift", "ios"],
    "analista": ["analista"],
    "data": ["data", "big data", "data science", "scientist"],
    "ciberseguridad": ["ciberseguridad", "seguridad", "cyber", "security"],
    "project manager": ["project", "manager"],
    "fullstack": ["fullstack", "full stack"]
}
def asignar_categoria(nombre):
    nombre = nombre.lower()
    for categoria, palabras in categorias.items():
        if any(palabra in nombre for palabra in palabras):
            return categoria
    return None

def extraer_años_experiencia(cadena):
    try:
        partes = cadena.split()
        if "anos" in partes:
            index = partes.index("anos")
            return int(partes[index - 1])  
    except:
        return None
    return None

file1 = "../datosCSV/Empleo_ofertas.csv"
file2 = "../datosCSV/CompuTrabajo_ofertas.csv"

df1 = pd.read_csv(file1, encoding='utf-8')
df2 = pd.read_csv(file2, encoding='utf-8')
df = pd.concat([df1, df2], ignore_index=True)
df["Categoria"] = df["Nombre"].apply(asignar_categoria)
df_valid = df[df["Categoria"].notnull()].copy()
df_valid["Años Experiencia"] = df_valid["Experiencia"].apply(extraer_años_experiencia)
df_valid = df_valid[df_valid["Años Experiencia"].notnull()]
promedio_experiencia = df_valid.groupby("Categoria")["Años Experiencia"].mean().sort_values()

plt.figure(figsize=(10, 6))
plt.barh(promedio_experiencia.index, promedio_experiencia.values, color='blue')
plt.xlabel("Años de experiencia promedio")
plt.ylabel("Categoría tecnológica")
plt.title("Promedio de años de experiencia requeridos por área tecnológica")
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()
