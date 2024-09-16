"""
Construir un programa que muestre una ventana y que lea una
clave secreta sin mostrar los caracteres que la componen.
"""
# Importar las herramientas necesarias.
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QFormLayout, QLabel, QLineEdit, QPushButton,
                             QSizePolicy, QSpacerItem, QHBoxLayout)

# Definir clase y heredar de QMainWindow.
class Main(QMainWindow):
    def __init__(self):
        # Heredar el constructor.
        super().__init__()
        # Título de ventana.
        self.setWindowTitle("Ejercicio 2 - Lab1 - C2")
        # Dimensiones de ventana.
        self.setGeometry(750,400,400,400)
        # LineEdit para contraseña.
        self.txtPass = QLineEdit()
        # Ocultación de contraseña.
        self.txtPass.setEchoMode(QLineEdit.Password)
        # Label que indica utilidad del LineEdit.
        self.lblPass = QLabel("Ingresa la contraseña")
        # Botón para ingresar la contraseña.
        self.btnIngresar = QPushButton("Ingresar")
        # Evento que realizará el botón (ir a la función "IngresarContr").
        self.btnIngresar.clicked.connect(self.IngresarContr)
        # Label para informar resultado del click al botón.
        self.lblConfirm = QLabel()

        # Creación del layout tipo formulario.
        layoutF = QFormLayout()
        # Ordenar los Widgets en el layout de formulario.
        layoutF.addRow(self.lblPass, self.txtPass)
        layoutF.addRow(self.btnIngresar)
        layoutF.addRow(self.lblConfirm)

        # Creación del layout vertical.
        layoutV = QVBoxLayout()
        # Espacios arriba y abajo para centrar verticalmente.
        layoutV.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))
        layoutV.addLayout(layoutF)
        layoutV.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Creación del layout horizontal.
        layoutH = QHBoxLayout()
        # Espacios a la izquierda y derecha para centrar horizontalmente.
        layoutH.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        layoutH.addLayout(layoutV)
        layoutH.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Cración del widget central.
        central = QWidget()
        # Asignación del layout principal (horizontal).
        central.setLayout(layoutH)
        # Asignación del widget central.
        self.setCentralWidget(central)

    # Función que realiza el botón Ingresar.
    def IngresarContr(self):
        # Si todo sale bien.
        try:
            # Si el LineEdit tiene contenido.
            if (self.txtPass.text()):
                # Almacenar y mostrar contraseña (si fuese necesario).
                #password  = self.txtPass.text()
                #self.lblConfirm.setText(f"La contraseña es: {password}.")
                self.lblConfirm.setText("                  Contraseña ingresada.")
                # Limpia el LineEdit.
                self.txtPass.clear()
            # Si el LineEdit está vacío.
            else:
                self.lblConfirm.setText(" Advertencia: debes ingresar una contraseña.")
        # En caso de excepción.
        except:
            self.lblConfirm.setText("Ocurrió un error.")

# Creación de aplicaión.
app = QApplication(sys.argv)
# Creación de instancia.
ventana = Main()
# show() muestra la ventana.
ventana.show()
# Función para cerrar ventana.
app.exec()