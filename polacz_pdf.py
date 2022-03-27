# polacz pliki pdf w jeden
import PyPDF3


import os
def glowna( nazwa ):
    pliki = os.listdir()
    pdf_lista = []
    for el in pliki:
        filename, file_extension = os.path.splitext(el)
        if file_extension == '.pdf':
            pdf_lista.append(el)
    return pdf_polacz(pdf_lista, nazwa )

def pdf_polacz(pdf_lista, nazwa ):
    merger = PyPDF3.PdfFileMerger()
    print( pdf_lista )
    for pdf in pdf_lista:
        print( pdf )
        merger.append(pdf)
    merger.write(nazwa+'.pdf')



if __name__ == '__main__':
   glowna(input('wprowadz nazwe polaczonego pliku '))