# Classe che gestisce l'interfaccia e il metodo per modificare e gestire i giocatori e i risultati delle partite

from PyQt5 import QtCore, QtGui, QtWidgets

from ProgettoIS_CentroSportivo.Model.Partita import Partita
from ProgettoIS_CentroSportivo.Handler.HandlerUtenti import HandlerUtenti

class Ui_modificapartita(object):

    # metodo che modifica l'oggetto partita con i dati inseriti dall'utente
    def modificaPartita(self):
        giocatore1 = self.giocatore1.text()
        giocatore2 = self.giocatore2.text()
        punteggio1 = self.spin1.value()
        punteggio2 = self.spin2.value()
        partita = Partita(giocatore1, punteggio1, giocatore2, punteggio2)
        from ProgettoIS_CentroSportivo.Views.gestionepartite import Ui_gestionepartite
        Ui_gestionepartite.prenotazione.modificaPartita(Ui_modificapartita.rigapartita,partita)

    # metodo che modifica l'interfaccia grafica per la modifica della partita
    def setupUi(self, gestionepartite, rigapartita):

        gestionepartite.setObjectName("modificapartita")
        gestionepartite.resize(326, 189)

        self.buttonBox = QtWidgets.QDialogButtonBox(gestionepartite)
        self.buttonBox.setGeometry(QtCore.QRect(70, 130, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.giocatore1 = QtWidgets.QLineEdit(gestionepartite)
        self.giocatore1.setGeometry(QtCore.QRect(30, 50, 113, 21))
        self.giocatore1.setObjectName("giocatoreuno")

        self.label1 = QtWidgets.QLabel(gestionepartite)
        self.label1.setGeometry(QtCore.QRect(30, 30, 71, 16))
        self.label1.setObjectName("labeluno")

        self.spin2 = QtWidgets.QSpinBox(gestionepartite)
        self.spin2.setGeometry(QtCore.QRect(210, 90, 48, 24))
        self.spin2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.spin2.setMaximum(3)
        self.spin2.setObjectName("spin2")

        self.spin1 = QtWidgets.QSpinBox(gestionepartite)
        self.spin1.setGeometry(QtCore.QRect(40, 90, 48, 24))
        self.spin1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.spin1.setMaximum(3)
        self.spin2.setObjectName("spinuno")

        self.label2 = QtWidgets.QLabel(gestionepartite)
        self.label2.setGeometry(QtCore.QRect(180, 30, 71, 16))
        self.label2.setObjectName("labeldue")

        self.giocatore2 = QtWidgets.QLineEdit(gestionepartite)
        self.giocatore2.setGeometry(QtCore.QRect(180, 50, 113, 21))
        self.giocatore2.setObjectName("giocatoredue")

        self.retranslateUi(gestionepartite)
        self.buttonBox.accepted.connect(self.modificaPartita)
        self.buttonBox.accepted.connect(gestionepartite.accept)  # type: ignore
        self.buttonBox.rejected.connect(gestionepartite.reject)  # type: ignore

        QtCore.QMetaObject.connectSlotsByName(gestionepartite)
        from ProgettoIS_CentroSportivo.Views.gestionepartite import Ui_gestionepartite

        if (HandlerUtenti.utenteConnesso.isAdmin == False):
            self.giocatore1.setText(HandlerUtenti.utenteConnesso.nome)
            self.giocatore1.setEnabled(False)
        self.giocatore2.setText(Ui_gestionepartite.prenotazione.collectionPartite[rigapartita].giocatore2)
        self.spin1.setValue(Ui_gestionepartite.prenotazione.collectionPartite[rigapartita].punteggio1)
        self.spin2.setValue(Ui_gestionepartite.prenotazione.collectionPartite[rigapartita].punteggio2)
        Ui_modificapartita.rigapartita = rigapartita

    def retranslateUi(self, modificapartita):
        _translate = QtCore.QCoreApplication.translate
        modificapartita.setWindowTitle(_translate("modificapartita", "Dialog"))
        self.label1.setText(_translate("modificapartita", "Giocatore1"))
        self.label2.setText(_translate("modificapartita", "Giocatore2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gestionepartite = QtWidgets.QDialog()
    ui = Ui_modificapartita()
    ui.setupUi(gestionepartite)
    gestionepartite.show()
    sys.exit(app.exec_())

