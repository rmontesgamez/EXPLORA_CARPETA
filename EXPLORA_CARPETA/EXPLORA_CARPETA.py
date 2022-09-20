import sys
import os

from PyQt5.QtWidgets import QWidget, QFileDialog, QApplication, QVBoxLayout, QPushButton

class filedialog(QWidget):
    def __init__(self):
        super(filedialog,self).__init__()

        layout = QVBoxLayout()
        self.btn = QPushButton("SELECCIONA ARCHIVO EN CARPETA")
        self.btn.clicked.connect(self.getfile)

        layout.addWidget(self.btn)
        
        self.setLayout(layout)
        self.setWindowTitle("File Dialog demo")


    def getfile(self):
        """
        función para abrir desplegable para elegir una carpeta
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
