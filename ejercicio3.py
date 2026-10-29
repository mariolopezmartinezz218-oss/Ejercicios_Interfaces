#Haz un programa que disponga de un botón y cada vez que hacemos clic, nos mostrará
#un refrán de manera aleatoria en el título de la ventana.
#Si el refrán es “De los errores se aprende”, el botón quedará deshabilitado y ya no
#dejará clicar y leer más refranes aleatorios. Haremos uso de la función choice de la
#librería random para hacer el ramdom.
#from random importe choice
#Los refrans populares serán los siguientes:
#• "Haz el bien sin mirar a quien",
#• "Más vale prevenir que curar",
#• "A mal tiempo, buena cara",
#• "Quien tiene un amigo tiene un tesoro",
#• "La avaricia rompe el saco",
#• "De los errores se aprende".

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from random import choice
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #nombre inicial
        self.setWindowTitle("Ex3")
        # no hace falta poner tamaño

        # inicia el widget pushButton
        self.boton = QPushButton("pulsa aquí")

        # para que aparezca hay que posicionarlo
        self.setCentralWidget(self.boton)

        # listener
        self.boton.clicked.connect(self.cambio)

    # funcion que elije un refran aletorio
    def cambio (self): 

        # array con todos los refranes
        refranes = [
            "Haz el bien sin mirar a quien",
            "Más vale prevenir que curar",
            "A mal tiempo, buena cara",
            "Quien tiene un amigo tiene un tesoro", 
            "La avaricia rompe el saco",
            "De los errores se aprende"
        ]

        # crea la variable op y le asigna un refrán aleatorio
        op = choice(refranes)

        # cambia el título de la ventana
        self.setWindowTitle(op)

        # comprueba si es el que desactiva el botón
        if op == "De los errores se aprende":
            self.boton.setEnabled(False)

#main
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