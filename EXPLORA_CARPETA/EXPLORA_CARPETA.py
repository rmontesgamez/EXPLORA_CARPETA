import sys
import os
import xlwt
from xlrd import open_workbook
from xlutils.copy import copy
from PyQt5.QtWidgets import QWidget, QFileDialog, QApplication, QVBoxLayout, QPushButton

class filedialog(QWidget):
    """
    clase filedialog deriva de QWidget

    """

    def __init__(self):
        """Inicializa la clase
        Crea un botón y un layout
        """
        super(filedialog, self).__init__()

        layout = QVBoxLayout()
        self.btn = QPushButton("SELECCIONA ARCHIVO EN CARPETA")
        self.btn.clicked.connect(self.getfile)

        layout.addWidget(self.btn)
        self.setLayout(layout)
        self.setWindowTitle("File Dialog demo")


    def getfile(self):
        """Funcion para abrir desplegable para elegir una carpeta

        entrada
        clase

        salida
        string con la ruta de la carpeta

        """

        fname = QFileDialog.getExistingDirectory(self, 'Open file',
                                            'c:\\activa\\')

        print(fname)

        lista_archivos(fname)
        #self.le.setPixmap(QPixmap(fname))

def lista_archivos(ruta):
    """
    funcion para obtener la lista de archivos de una carpeta

    entrada
    string  Ruta de la carpeta

    salida
    lista de string con nombres de archivos limitados a 50 caracteres
    """
    contenido = os.scandir(ruta)
    listado=[]
    for elemento in contenido:
        if elemento.is_file() and elemento.name.endswith(".dxf"):
            listado.append(elemento.name[:49].split(".")[0])

    print(listado)
    guarda_datos(listado)

def guarda_datos(nombres):

    book = open_workbook("C:\\activa\\adibujar\\oferta.xls")
    wb = copy(book)

    s = wb.get_sheet(0)


    style= xlwt.XFStyle()

    font = xlwt.Font() 

    font.bold = True
    font.color_index = 4
    font.height = 200
    pattern1 = xlwt.Pattern()
    pattern1.pattern=pattern1.SOLID_PATTERN
    #pattern.pattern_back_colour = 0x00BFBF
    pattern1.pattern_fore_colour = 0x32

    borders = xlwt.Borders()
    borders.left = 1
    borders.right = 1
    borders.top = 1
    borders.bottom = 1
    style.borders = borders
    style.font = font
    style.pattern= pattern1

    lista =["CLIENTE","" ,"NºPedido:","Fecha:", "Plazo:", "Horas O.T.:"]
    for i in range(len(lista)):
        s.write(i,0, lista[i],style)

    pattern2 = xlwt.Pattern()
    pattern2.pattern=pattern2.SOLID_PATTERN
    #pattern.pattern_back_colour = 0x00BFBF
    pattern2.pattern_fore_colour = 0x32

    pattern2.pattern_fore_colour = 0x0E
    style.pattern= pattern2

    lista = ["Padre","Version Padre", "Hijo", "Version Hijo", "Denominacion", "Material", "Esp.", "Cant.", "Procesos"]


    for i in range(len(lista)):
        s.write(7,i, lista[i],style)

    for i in range(len(nombres)):
        s.write(8+i,2, nombres[i])


    wb.save("C:\\activa\\oferta.xls")

def main():
    """
    función main
    """

    app = QApplication(sys.argv)
    ex = filedialog()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()