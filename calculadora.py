import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("calculadora.ui", self)
        self.btn_sumar.clicked.connect(self.Sumar)
        self.btn_restar.clicked.connect(self.Restar)
        self.btn_mul.clicked.connect(self.multiplicacion)
        self.btn_division.clicked.connect(self.division)
        self.btn_divisionEn.clicked.connect(self.DivisionEntera)
        self.btn_modulo.clicked.connect(self.Modulo)

    def Sumar(self):
        number1 = int(self.inp_1.toPlainText())
        number2 = int(self.inp_2.toPlainText())
        result = number1 + number2
        self.respuesta.setText(str(result))

    def Restar(self):
        number1 = int(self.inp_1.toPlainText())
        number2 = int(self.inp_2.toPlainText())
        result = number1 - number2
        self.respuesta.setText(str(result))

    def multiplicacion(self):
        number1 = int(self.inp_1.toPlainText())
        number2 = int(self.inp_2.toPlainText())
        result = number1 * number2
        self.respuesta.setText(str(result))

    def division(self):
        number1 = int(self.inp_1.toPlainText())
        number2 = int(self.inp_2.toPlainText())
        result = number1 / number2
        self.respuesta.setText(str(result))

    def DivisionEntera(self):
        number1 = int(self.inp_1.toPlainText())
        number2 = int(self.inp_2.toPlainText())
        result = number1 // number2
        self.respuesta.setText(str(result))

    def Modulo(self):
        number1 = int(self.inp_1.toPlainText())
        number2 = int(self.inp_2.toPlainText())
        result = number1 % number2
        self.respuesta.setText(str(result))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = Calculadora()
    GUI.show()
    sys.exit(app.exec_())
