#1. Ejercicio 1 (3,33 puntos)
#Vayamos a hacer un programa que hará uso de los componentes de QLineEdit y de un
#QLabel. Por eso, asignaremos un tamaño máximo de texto de 5 caracteres al QLine y
#un tamaño fijo de 50x30 píxeles. El QLabel también tendrá un tamaño de 50x30 píxeles
#y se desplazará 50 píxeles por no solaparse con el QLineEdit. Finalmente, cuánto lo
#QLineEdit cambio, la etiqueta mostrará el texto introducido

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    # constructor de clase 
    def __init__(self):
        # llama al constructor de la clase padre (QMainWindow)
        super().__init__()
        # en este ejercicio no parece necesario indicar tamaño mínimo
        self.setWindowTitle("Ex1") # nombre ventana

        #componentes
        self.texto = QLineEdit(self)        # de esta manera el texto se puede mover a si mismo con .move()
        self.texto.setMaxLength(5)          # el 5 indica el largo
        self.texto.setFixedSize(50, 30)     # La posición que pide el ejercicio (largo, ancho)
        #self.texto.move(0, 0)              # posición de la ventana (en este caso no hace ni falta)

        self.copia = QLabel(self)           # asi se puede mover a si mismo
        self.copia.setFixedSize(50, 30)     # tamaño
        self.copia.move(50, 0)              # ajusta la posición para que no se solape

        # listener. Con el conect lo haces de una manera sencilla
        self.texto.textChanged.connect(self.copia.setText) 



# Una manera sencilla de crear un "main"
if __name__ == "__main__":
    # crea el objeto de la gestión gráfica (app)
    app = QApplication(sys.argv)
    # así se llama al constructor de la ventana (window)
    window = MainWindow()
    # método para mostrar la pantalla
    window.show()
    # de esta manera se centra un poco la ventana, pero no
    # tiene como java swing una opción directa de centrarla
    window.move(500,300)
    # configura la operación de cerrar cuando le das al boton de la ventana
    sys.exit(app.exec_())