# Questa classe genera un pop-up con un messaggio personalizzabile e che ha solo un pulsante Ok per chiuderlo

from PyQt5 import QtCore, QtWidgets

class Ui_conferma(object):

    def setupUi(self, popup, messaggio):
        popup.setObjectName("popup")
        popup.resize(400, 107)
        self.buttonBox = QtWidgets.QDialogButtonBox(popup)
        self.buttonBox.setGeometry(QtCore.QRect(280, 60, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)

        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.label = QtWidgets.QLabel(popup)
        self.label.setGeometry(QtCore.QRect(20, 20, 261, 51))
        self.label.setObjectName("label")

        self.retranslateUi(popup, messaggio)
        self.buttonBox.accepted.connect(popup.accept)
        QtCore.QMetaObject.connectSlotsByName(popup)

    def retranslateUi(self, popup, messaggio):
        _translate = QtCore.QCoreApplication.translate
        popup.setWindowTitle(_translate("popup", "Dialog"))
        self.label.setText(_translate("popup", messaggio))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    popup = QtWidgets.QDialog()
    ui = Ui_conferma()
    ui.setupUi(popup, "Prova")
    popup.show()
    sys.exit(app.exec_())
