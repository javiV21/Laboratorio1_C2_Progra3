"""
Después de realizar los cinco ejercicios, realizar un ejercicio con la librería de PyQt que utilice al menos dos de
estos widgets: radiobox, combobox y spinbox. El ejercicio debe permitir la entrada de datos. Además, proporcionen
una explicación detallada sobre qué hace el programa y qué problema resuelve.
-------------------------------------------------------------------------------------------------------------------
Con la utilización de <RadioButton> y <SpinBox> resolví el siguiente ejercicio:
-------------------------------------------------------------------------------------------------------------------
Un grupo de mariachi hace sus contratos por horas y solicita al cliente la cantidad de horas que
desea el servicio y en qué horario (am/pm). El programa se encarga de almacenar dichos datos. La mínima
cantidad de horas es 1 y la máxima es de 10 (horas).
"""

# Importar las herramientas necesarias.
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QFormLayout, QHBoxLayout, QLabel, QSpinBox, QButtonGroup,
                             QRadioButton, QPushButton, QSizePolicy, QSpacerItem)

# Definir clase y heredar de QMainWindow.
class Main(QMainWindow):
    def __init__(self):
        # Heredar el constructor.
        super().__init__()
        # Título de ventana.
        self.setWindowTitle("Ejercicio 6 - Lab1 - C2")
        # Dimensiones de ventana.
        self.setGeometry(750,400,400,400)
        # Creación de los widgets necesarios.
        self.lblTitulo = QLabel("Ingresa los siguientes datos del contrato.")
        self.lblHora = QLabel("Cantidad de horas")
        self.spinHora = QSpinBox()
        self.spinHora.setRange(1, 10)
        self.lblHorario = QLabel("Horario")
        self.radAm = QRadioButton("a.m.")
        self.radPm = QRadioButton("p.m.")
        self.lblDatos = QLabel()
        self.btnGuardar = QPushButton("Guardar")
        self.btnVerInfo = QPushButton("Ver Información")
        self.grupoRad = QButtonGroup()
        self.grupoRad.addButton(self.radAm)
        self.grupoRad.addButton(self.radPm)
        # Conectar botones a sus respectivas funciones.
        self.btnGuardar.clicked.connect(self.GuadarInfo)
        self.btnVerInfo.clicked.connect(self.VerInfo)
        self.btnVerInfo.setDisabled(True)
        # Creación de layout horizontal para agrupar RadioButton.
        layoutRad = QHBoxLayout()
        layoutRad.addWidget(self.radAm)
        layoutRad.addWidget(self.radPm)
        # Creación del layout tipo formulario.
        layoutF = QFormLayout()
        # Ordenar los Widgets en el layout de formulario.
        layoutF.addRow(self.lblTitulo)
        layoutF.addRow(self.lblHora, self.spinHora)
        layoutF.addRow(self.lblHorario, layoutRad)
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

    # Función para almacenar información.
    def GuadarInfo(self):
        # Si todo sale bien.
        try:
            # Si los datos están completos.
            if (self.spinHora.value() and (self.radAm.isChecked() or self.radPm.isChecked())):
                # Guardar contenido.
                self.hora = str(self.spinHora.value())
                if (self.radAm.isChecked()):
                    self.horario = self.radAm.text()
                else:
                    self.horario = self.radPm.text()
                self.btnVerInfo.setDisabled(False)
                self.lblDatos.setText("Información guardada exitosamente.")
                # Limpia el SpinBox y el RadioButton.
                self.spinHora.setValue(1)
                self.grupoRad.setExclusive(False)
                self.radAm.setChecked(False)
                self.radPm.setChecked(False)
                self.grupoRad.setExclusive(True)
            # Si falta ingresar datos.
            else:
                self.lblDatos.setText(" Advertencia: debes elegir un horario.")
        # En caso de excepción.
        except:
            self.lblDatos.setText("Ocurrió un error.")

    # Función que muestra los datos del contrato.
    def VerInfo(self):
        self.lblDatos.setText(f"Información del contrato.\nCantidad de horas: {self.hora}.\nHorario: {self.horario}")

# Creación de aplicaión.
app = QApplication(sys.argv)
# Creación de instancia.
ventana = Main()
# show() muestra la ventana.
ventana.show()
# Función para cerrar ventana.
app.exec()