"""
Construir un programa que muestre una ventana en la
cual aparezca su nombre completo y su edad centrados.
"""
# Importar las herramientas necesarias.
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow,
                             QWidget, QVBoxLayout, QLabel)

# Definir clase y heredar de QMainWindow.
class Main(QMainWindow):
    def __init__(self):
        # Heredar el constructor.
        super().__init__()
        # Título de ventana.
        self.setWindowTitle("Ejercicio 1 - Lab1 - C2")
        # Dimensiones de ventana.
        self.setGeometry(750,400,400,400)

        # Creación del label que mostrará la información.
        self.datos = QLabel("Nombre: Javier Alexander Vargas Díaz.\n"
                            "                Edad: 19 años")
        # Creación del layout vertical.
        layout = QVBoxLayout()
        # Ubicando el label centrado en el layout.
        layout.addWidget(self.datos, alignment=Qt.AlignCenter)
        # Creación del widget central.
        central = QWidget()
        # Asignación del layout principal.
        central.setLayout(layout)
        # Asignación del widget central.
        self.setCentralWidget(central)

# Creación de aplicaión.
app = QApplication(sys.argv)
# Creación de instancia.
ventana = Main()
# show() muestra la ventana.
ventana.show()
# Función para cerrar ventana.
app.exec()