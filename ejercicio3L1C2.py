"""
Construir un programa que muestre una ventana a través de la
cual se pueda leer su número de cédula y su nombre completo.
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
        self.setWindowTitle("Ejercicio 3 - Lab1 - C2")
        # Dimensiones de ventana.
        self.setGeometry(750,400,400,400)
        # Label que indica utilidad de los LineEdit.
        self.lblNom = QLabel("Ingresa tu nombre")
        self.lblDui = QLabel("Ingresa tu DUI")
        # LineEdit para nombre y DUI.
        self.txtNom = QLineEdit()
        self.txtDui = QLineEdit()
        # Botón para ver información.
        self.btnVer = QPushButton("Ver información")
        # Evento que realizará el botón (ir a la función "VerInfo").
        self.btnVer.clicked.connect(self.VerInfo)
        # Label para informar resultado del click al botón.
        self.lblDatos = QLabel()

        # Creación del layout tipo formulario.
        layoutF = QFormLayout()
        # Ordenar los Widgets en el layout de formulario.
        layoutF.addRow(self.lblNom, self.txtNom)
        layoutF.addRow(self.lblDui, self.txtDui)
        layoutF.addRow(self.btnVer)
        layoutF.addRow(self.lblDatos)

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

    # Función que realiza el botón Ver información.
    def VerInfo(self):
        # Si todo sale bien.
        try:
            # Si los LineEdit tienen contenido.
            if (self.txtDui.text() and self.txtNom.text()):
                # Guardar contenido de LineEdit.
                dui  = self.txtDui.text()
                nombre  = self.txtNom.text()
                # Mostrar datos.
                self.lblDatos.setText(f"Nombre: {nombre}.\nDUI: {dui}.")
                # Limpia los LineEdit.
                self.txtDui.clear()
                self.txtNom.clear()
            # Si los LineEdit están vacíos.
            else:
                self.lblDatos.setText(" Advertencia: debes llenar todos los campos.")
        # En caso de excepción.
        except:
            self.lblDatos.setText("Ocurrió un error.")

# Creación de aplicaión.
app = QApplication(sys.argv)
# Creación de instancia.
ventana = Main()
# show() muestra la ventana.
ventana.show()
# Función para cerrar ventana.
app.exec()