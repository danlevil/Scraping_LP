import pandas as pd
import matplotlib.pyplot as plt

def analisis_idioma_ingles():

    files = {
        "BuscoJobs": "datosCSV/BuscoJobs_ofertas.csv",
        "CompuTrabajo": "datosCSV/CompuTrabajo_ofertas.csv",
        "Empleo": "datosCSV/Empleo_ofertas.csv"
    }

    requiere_ingles = 0
    no_requiere_ingles = 0

    keywords = ["inglés", "ingles", "Inglés", "Ingles"]

    def menciona_ingles(texto):
        if pd.isna(texto):  
            return False
        return any(keyword in texto for keyword in keywords)

    df_buscojobs = pd.read_csv(files["BuscoJobs"], encoding="utf-8")
    requiere_ingles += df_buscojobs['Descripcion'].apply(menciona_ingles).sum()
    no_requiere_ingles += len(df_buscojobs) - df_buscojobs['Descripcion'].apply(menciona_ingles).sum()

    df_computrabajo = pd.read_csv(files["CompuTrabajo"], encoding="utf-8")
    requiere_ingles += df_computrabajo['Idioma'].str.startswith("Idiomas: Ingles", na=False).sum()
    no_requiere_ingles += len(df_computrabajo) - df_computrabajo['Idioma'].str.startswith("Idiomas: Ingles", na=False).sum()

    df_empleo = pd.read_csv(files["Empleo"], encoding="utf-8")
    requiere_ingles += df_empleo['Descripcion'].apply(menciona_ingles).sum()
    no_requiere_ingles += len(df_empleo) - df_empleo['Descripcion'].apply(menciona_ingles).sum()

    labels = ['No requiere Inglés', 'Requiere Inglés']
    sizes = [no_requiere_ingles, requiere_ingles]
    colors = ['#98FB98', '#9370DB']  
    plt.figure(figsize=(10, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=180, wedgeprops={'edgecolor': 'black'})
    plt.title('Requerimiento del idioma Inglés en ofertas de trabajo')
    plt.axis('equal') 
    plt.tight_layout()
    return plt

if __name__ == "__main__":
    plt= analisis_idioma_ingles()
    plt.show()