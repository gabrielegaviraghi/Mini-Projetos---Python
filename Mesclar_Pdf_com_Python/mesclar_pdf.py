import PyPDF2
import os # navegar entre as pastas 

# inicialização | mesclar vários arquivos pdf
merger = PyPDF2.PdfMerger()

lista_arquivos = os.listdir("pdfs_mesclar")

# percorer a os arquivos da lista e merger
for arquivo in lista_arquivos:
    if ".pdf" in arquivo: # caso o arquivo for em pdf
        merger.append(f"pdfs_mesclar/{arquivo}")

merger.write("PDF_Final.pdf")
print("TERMINOU")