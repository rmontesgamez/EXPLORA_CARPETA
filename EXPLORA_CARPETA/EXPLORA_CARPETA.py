import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class filedialogdemo(QWidget):
    def __init__(self):
        super(filedialogdemo,self).__init__()

        layout = QVBoxLayout()
        self.btn = QPushButton("SELECCIONA ARCHIVO EN CARPETA")
        self.btn.clicked.connect(self.getfile)

        layout.addWidget(self.btn)
        """
        self.le = QLabel("Hello")

        layout.addWidget(self.le)
        self.btn1 = QPushButton("QFileDialog object")
        self.btn1.clicked.connect(self.getfiles)
        layout.addWidget(self.btn1)

        self.contents = QTextEdit()
        layout.addWidget(self.contents)
        """
        self.setLayout(layout)
        self.setWindowTitle("File Dialog demo")


    def getfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            'c:\\activa\\',"Image files (*.dxf *.dwg)")

        print(fname)
        #self.le.setPixmap(QPixmap(fname))


def main():
    app = QApplication(sys.argv)
    ex = filedialogdemo()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
