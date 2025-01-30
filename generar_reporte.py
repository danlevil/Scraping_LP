from matplotlib.backends.backend_pdf import PdfPages
from Previsualizacion.penafiel1 import analisis_peñafiel1
from Previsualizacion.penafiel2 import analisis_peñafiel2
from Previsualizacion.penafiel3 import analisis_peñafiel3
from Previsualizacion.Villamar1 import analisis_provincias_experiencia
from Previsualizacion.Villamar2 import analisis_experiencia_por_categoria
from Previsualizacion.Villamar3 import analisis_idioma_ingles
from Previsualizacion.analysis  import analisis_gaibor1

def generar_pdf():
    with PdfPages("Analisis_ofertas_G7LP.pdf") as pdf:  

        plt_p1 = analisis_peñafiel1()
        pdf.savefig(plt_p1.gcf())
        plt_p1.close()

        plt_p2 = analisis_peñafiel2()
        pdf.savefig(plt_p2.gcf())
        plt_p2.close()

        plt_p3 = analisis_peñafiel3()
        pdf.savefig(plt_p3.gcf())
        plt_p3.close()

        plt_provincia = analisis_provincias_experiencia()
        pdf.savefig(plt_provincia.gcf())
        plt_provincia.close()

        plt_exp = analisis_experiencia_por_categoria()
        pdf.savefig(plt_exp.gcf())
        plt_exp.close()

        plt_idioma = analisis_idioma_ingles()
        pdf.savefig(plt_idioma.gcf())
        plt_idioma.close()

        plt_gb = analisis_gaibor1()
        pdf.savefig(plt_gb.gcf())
        plt_gb.close()

    print("Reporte generado exitosamente")

if __name__ == "__main__":
    generar_pdf()
