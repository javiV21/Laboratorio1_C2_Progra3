"""
Construir un programa que muestre una ventana a través de la
cual se pueda leer tres datos básicos de 3 mascotas diferentes.
"""

# Importar las herramientas necesarias.
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QFormLayout, QHBoxLayout, QLabel, QLineEdit,
                             QPushButton, QSizePolicy, QSpacerItem, QComboBox)

# Definir clase y heredar de QMainWindow.
class Main(QMainWindow):
    def __init__(self):
        # Heredar el constructor.
        super().__init__()
        # Título de ventana.
        self.setWindowTitle("Ejercicio 4 - Lab1 - C2")
        # Dimensiones de ventana.
        self.setGeometry(750,400,400,400)
        # Creación de los widgets necesarios.
        self.lblTitulo = QLabel("Selecciona una opción")
        self.combo = QComboBox()
        # Agregar elementos al comboBox.
        self.combo.addItem("Seleccionar")
        self.combo.addItem("Perro")
        self.combo.addItem("Gato")
        self.combo.addItem("Conejo")
        # Conectar comboBox con la función para obtener elección.
        self.combo.currentIndexChanged.connect(self.SeleccionarOp)
        self.lblDato1 = QLabel("Nombre")
        self.txtDato1 = QLineEdit()
        self.lblDato2 = QLabel("Edad (años)")
        self.txtDato2 = QLineEdit()
        self.lblDato3 = QLabel("Peso (kg)")
        self.txtDato3 = QLineEdit()
        self.lblDatos = QLabel()
        self.btnGuardar = QPushButton("Guardar")
        self.btnVerInfo = QPushButton("Ver Información")
        self.btnGuardar.clicked.connect(self.GuadarInfo)
        self.btnVerInfo.clicked.connect(self.VerInfo)
        # Mientras no se haga una elección los widgets estarán desactivados.
        self.txtDato1.setDisabled(True)
        self.txtDato2.setDisabled(True)
        self.txtDato3.setDisabled(True)
        self.btnGuardar.setDisabled(True)
        self.btnVerInfo.setDisabled(True)

        # Creación del layout tipo formulario.
        layoutF = QFormLayout()
        # Ordenar los Widgets en el layout de formulario.
        layoutF.addRow(self.lblTitulo, self.combo)
        layoutF.addRow(self.lblDato1, self.txtDato1)
        layoutF.addRow(self.lblDato2, self.txtDato2)
        layoutF.addRow(self.lblDato3, self.txtDato3)
        layoutF.addRow(self.btnGuardar, self.btnVerInfo)
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

    # Función para recibir elección del comboBox.
    def SeleccionarOp(self):
        # Limpia el label que informa proceso.
        self.lblDatos.clear()
        # Si se ha elegido una opción diferente de "Seleccionar".
        if self.combo.currentText() != "Seleccionar":
            opSelected = self.combo.currentText()
            self.lblTitulo.setText(f"Has seleccionado: {opSelected}")
            self.txtDato1.setDisabled(False)
            self.txtDato2.setDisabled(False)
            self.txtDato3.setDisabled(False)
            self.btnGuardar.setDisabled(False)
        # Si permanece en "Seleccionar".
        else:
            self.lblTitulo.setText("Selecciona una opción")
            self.txtDato1.setDisabled(True)
            self.txtDato2.setDisabled(True)
            self.txtDato3.setDisabled(True)
            self.btnGuardar.setDisabled(True)

    # Función para almacenar valores de LineEdit.
    def GuadarInfo(self):
        # Si todo sale bien.
        try:
            # Si los LineEdit tienen contenido.
            if (self.txtDato1.text() and self.txtDato2.text() and self.txtDato3.text()):
                # Guardar contenido de LineEdit.
                self.nombre = self.txtDato1.text()
                self.edad = self.txtDato2.text()
                self.peso = self.txtDato3.text()
                self.animal = self.combo.currentText()
                self.lblDatos.setText("Información guardada exitosamente.")
                # Limpia los LineEdit.
                self.txtDato1.clear()
                self.txtDato2.clear()
                self.txtDato3.clear()
                self.btnVerInfo.setDisabled(False)
            # Si los LineEdit están vacíos.
            else:
                self.lblDatos.setText(" Advertencia: debes llenar todos los campos.")
        # En caso de excepción.
        except:
            self.lblDatos.setText("Ocurrió un error.")

    # Función que muestra el último animal registrado y sus datos.
    def VerInfo(self):
        self.lblDatos.setText(f"Animal: {self.animal}.\nNombre: {self.nombre}.\nEdad: {self.edad} años.\nPeso: {self.peso} kg.")

# Creación de aplicaión.
app = QApplication(sys.argv)
# Creación de instancia.
ventana = Main()
# show() muestra la ventana.
ventana.show()
# Función para cerrar ventana.
app.exec()