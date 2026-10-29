#Se pide mostrar un listado con todos los meses del año, y al seleccionar un elemento
#concreto (por ejemplo abril), se imprimirá por consola el número que ocupa (posición
#real, por ejemplo abril ocupa la cuarta posición) y también mostrará el más exacto.

from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #nombre
        self.setWindowTitle("Ex2")
        # no hace falta poner tamaño

        # inicia el widget comboBox (para este menú simple era lo más sencillo)
        self.combo = QComboBox()
        # con el método addItems añado todos los meses a través del array que está escrito
        self.combo.addItems(["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Dicimebre"])

        #detectar el cambio de opción y dar el mensaje en consola
        self.combo.currentTextChanged.connect(self.cambio)

        #para que aparezca hay que posicionarlo
        self.setCentralWidget(self.combo)

    # funcion que imprime en consola la posición que ocupa el mes seleccionado en el menu (tiene que estar a esta altura para que funcione)
    def cambio (self, texto): 
        print((self.combo.currentIndex() + 1))

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