# Questa classe genera un pop-up con un messaggio personalizzabile e che ha due pulsanti:
# Ok per confermare, Cancel per annullare

from PyQt5 import QtCore, QtWidgets

class Ui_verifica(object):

    def setupUi(self, popupOkCanc, messaggio):

        popupOkCanc.setObjectName("erroreprenotazione")
        popupOkCanc.resize(400, 106)

        self.buttonBox = QtWidgets.QDialogButtonBox(popupOkCanc)
        self.buttonBox.setGeometry(QtCore.QRect(290, 20, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.lbl = QtWidgets.QLabel(popupOkCanc)
        self.lbl.setGeometry(QtCore.QRect(80, 30, 181, 51))
        self.lbl.setObjectName("lbl")

        self.retranslateUi(popupOkCanc, messaggio)
        self.buttonBox.accepted.connect(popupOkCanc.accept)
        self.buttonBox.rejected.connect(popupOkCanc.reject)
        QtCore.QMetaObject.connectSlotsByName(popupOkCanc)

    def retranslateUi(self, popupOkCanc, messaggio):
        _translate = QtCore.QCoreApplication.translate
        popupOkCanc.setWindowTitle(_translate("popupOkCanc", "Dialog"))
        self.lbl.setText(_translate("popupOkCanc", messaggio))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    popupOkCanc = QtWidgets.QDialog()
    ui = Ui_verifica()
    ui.setupUi(popupOkCanc)
    popupOkCanc.show()
    sys.exit(app.exec_())
