"""
Construir un programa que muestre una ventana a través de la
cual se puedan leer 10 datos característicos de una persona.
"""

# Importar las herramientas necesarias.
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QFormLayout, QHBoxLayout, QLabel, QLineEdit,
                             QPushButton, QSizePolicy, QSpacerItem)

# Definir clase y heredar de QMainWindow.
class Main(QMainWindow):
    def __init__(self):
        # Heredar el constructor.
        super().__init__()
        # Título de ventana.
        self.setWindowTitle("Ejercicio 5 - Lab1 - C2")
        # Dimensiones de ventana.
        self.setGeometry(750,250,500,600)
        # Creación de los widgets necesarios.
        self.lblTitulo = QLabel("Ingresa los siguientes datos.")
        self.lblNom = QLabel("Nombre")
        self.txtNom = QLineEdit()
        self.lblApe = QLabel("Apellido")
        self.txtApe = QLineEdit()
        self.lblEdad = QLabel("Edad (años)")
        self.txtEdad = QLineEdit()
        self.lblSexo = QLabel("Sexo")
        self.txtSexo = QLineEdit()
        self.lblPeso = QLabel("Peso (kg)")
        self.txtPeso = QLineEdit()
        self.lblEstatura = QLabel("Estatura (fts)")
        self.txtEstatura = QLineEdit()
        self.lblPelo = QLabel("Color de pelo")
        self.txtPelo = QLineEdit()
        self.lblPiel = QLabel("Color de piel")
        self.txtPiel = QLineEdit()
        self.lblNacion = QLabel("Nacionalidad")
        self.txtNacion = QLineEdit()
        self.lblDisc = QLabel("Discapacidad física")
        self.txtDisc = QLineEdit()
        self.lblDatos = QLabel()
        self.btnGuardar = QPushButton("Guardar")
        self.btnVerInfo = QPushButton("Ver Información")
        # Conectar botones a sus respectivas funciones.
        self.btnGuardar.clicked.connect(self.GuadarInfo)
        self.btnVerInfo.clicked.connect(self.VerInfo)
        self.btnVerInfo.setDisabled(True)

        # Creación del layout tipo formulario.
        layoutF = QFormLayout()
        # Ordenar los Widgets en el layout de formulario.
        layoutF.addRow(self.lblTitulo)
        layoutF.addRow(self.lblNom, self.txtNom)
        layoutF.addRow(self.lblApe, self.txtApe)
        layoutF.addRow(self.lblEdad, self.txtEdad)
        layoutF.addRow(self.lblSexo, self.txtSexo)
        layoutF.addRow(self.lblPeso, self.txtPeso)
        layoutF.addRow(self.lblEstatura, self.txtEstatura)
        layoutF.addRow(self.lblPelo, self.txtPelo)
        layoutF.addRow(self.lblPiel, self.txtPiel)
        layoutF.addRow(self.lblNacion, self.txtNacion)
        layoutF.addRow(self.lblDisc, self.txtDisc)
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

    # Función para almacenar valores de LineEdit.
    def GuadarInfo(self):
        # Si todo sale bien.
        try:
            # Si los LineEdit tienen contenido.
            if (self.txtNom.text() and self.txtApe.text() and self.txtEdad.text() and self.txtSexo.text()
                and self.txtPeso.text() and self.txtEstatura.text() and self.txtPelo.text() and self.txtPiel.text()
                and self.txtNacion.text() and self.txtDisc.text()):
                # Guardar contenido de LineEdit.
                self.nomb = self.txtNom.text()
                self.ape = self.txtApe.text()
                self.edad = self.txtEdad.text()
                self.sexo = self.txtSexo.text()
                self.peso = self.txtPeso.text()
                self.estatura = self.txtEstatura.text()
                self.pelo = self.txtPelo.text()
                self.piel = self.txtPiel.text()
                self.nacion = self.txtNacion.text()
                self.disc = self.txtDisc.text()
                self.btnVerInfo.setDisabled(False)
                self.lblDatos.setText("Información guardada exitosamente.")
                # Limpia los LineEdit.
                self.txtNom.clear()
                self.txtApe.clear()
                self.txtEdad.clear()
                self.txtSexo.clear()
                self.txtPeso.clear()
                self.txtEstatura.clear()
                self.txtPelo.clear()
                self.txtPiel.clear()
                self.txtNacion.clear()
                self.txtDisc.clear()
            # Si los LineEdit están vacíos.
            else:
                self.lblDatos.setText(" Advertencia: debes llenar todos los campos.")
        # En caso de excepción.
        except:
            self.lblDatos.setText("Ocurrió un error.")

    # Función que muestra el último animal registrado y sus datos.
    def VerInfo(self):
        self.lblDatos.setText(f"Datos de la persona.\nNombre completo: {self.nomb+" "+self.ape}.\nEdad: {self.edad} años.\n"
                              f"Sexo: {self.sexo}. \nPeso: {self.peso} kg.\nEstatura: {self.estatura}.\nColor de pelo: {self.pelo}.\n"
                              f"Color de piel: {self.piel}.\nNacionalidad: {self.nacion}.\nDiscapacidad física: {self.disc}.")

# Creación de aplicaión.
app = QApplication(sys.argv)
# Creación de instancia.
ventana = Main()
# show() muestra la ventana.
ventana.show()
# Función para cerrar ventana.
app.exec()