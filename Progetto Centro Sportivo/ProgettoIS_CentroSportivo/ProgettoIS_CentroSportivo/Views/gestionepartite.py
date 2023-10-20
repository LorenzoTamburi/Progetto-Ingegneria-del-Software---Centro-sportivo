# classe per gestire, visualizzare, inserire e modificare i risultati delle partite di ogni utente

from PyQt5 import QtCore, QtGui, QtWidgets
from ProgettoIS_CentroSportivo.Model.Partita import Partita
from ProgettoIS_CentroSportivo.Handler.HandlerUtenti import HandlerUtenti
from PyQt5.QtWidgets import QTableWidgetItem
from ProgettoIS_CentroSportivo.Views.modificapartita import Ui_modificapartita


class Ui_gestionepartite(object):

    # metodo per modificare risultato e giocatori di una partita
    def modificaPartita(self):
        self.tabellapartite.currentRow()
        self.window = QtWidgets.QDialog()
        self.ui = Ui_modificapartita()
        self.ui.setupUi(self.window, self.tabellapartite.currentRow())
        self.window.show()
        if(self.window.exec()): self.visualizzaPartite()

    # metodo per aggiungere una nuova partita
    def aggiungiPartita(self):
        if(HandlerUtenti.utenteConnesso.isAdmin == False):giocatore1 = HandlerUtenti.utenteConnesso.nome
        else: giocatore1=self.giocatore1.text()
        giocatore2 = self.giocatore2.text()
        punteggio1 = self.spin1.value()
        punteggio2 = self.spin2.value()
        partita = Partita(giocatore1, punteggio1, giocatore2, punteggio2)
        Ui_gestionepartite.prenotazione.aggiungiPartita(partita)
        self.visualizzaPartite()

    # metodo che mostra la tabella partite che esce quando schiaccio inserisci partite
    def visualizzaPartite(self):
        self.tabellapartite.setRowCount(len(Ui_gestionepartite.prenotazione.collectionPartite))
        for i in range(len(Ui_gestionepartite.prenotazione.collectionPartite)):
            item = QTableWidgetItem(Ui_gestionepartite.prenotazione.collectionPartite[i].giocatore1)
            self.tabellapartite.setItem(i, 0, item)
            item = QTableWidgetItem(str(Ui_gestionepartite.prenotazione.collectionPartite[i].punteggio1))
            self.tabellapartite.setItem(i, 1, item)
            item = QTableWidgetItem(Ui_gestionepartite.prenotazione.collectionPartite[i].giocatore2)
            self.tabellapartite.setItem(i, 2, item)
            item = QTableWidgetItem(str(Ui_gestionepartite.prenotazione.collectionPartite[i].punteggio2))
            self.tabellapartite.setItem(i, 3, item)
        self.statistiche.setText(Ui_gestionepartite.prenotazione.getStatistiche())

    def setupUi(self, gestionepartite, prenotazione):
        Ui_gestionepartite.prenotazione = prenotazione
        gestionepartite.setObjectName("gestionepartite")
        gestionepartite.resize(500, 320)

        self.giocatore1 = QtWidgets.QLineEdit(gestionepartite)
        self.giocatore1.setGeometry(QtCore.QRect(40, 40, 113, 21))
        self.giocatore1.setObjectName("giocatoreuno")

        if HandlerUtenti.utenteConnesso.isAdmin == False:
            self.giocatore1.setEnabled(False)
            self.giocatore1.setText(HandlerUtenti.utenteConnesso.nome)

        self.giocatore2 = QtWidgets.QLineEdit(gestionepartite)
        self.giocatore2.setGeometry(QtCore.QRect(190, 40, 113, 21))
        self.giocatore2.setObjectName("giocatoredue")

        self.spin1 = QtWidgets.QSpinBox(gestionepartite)
        self.spin1.setGeometry(QtCore.QRect(50, 80, 48, 24))
        self.spin1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.spin1.setMaximum(25)
        self.spin1.setObjectName("spinuno")

        self.spin2 = QtWidgets.QSpinBox(gestionepartite)
        self.spin2.setGeometry(QtCore.QRect(220, 80, 48, 24))
        self.spin2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.spin2.setMaximum(25)
        self.spin2.setObjectName("spin2")

        #Giocatore 1
        self.label1 = QtWidgets.QLabel(gestionepartite)
        self.label1.setGeometry(QtCore.QRect(40, 20, 71, 16))
        self.label1.setObjectName("labeluno")

        #Giocaore 2
        self.label2 = QtWidgets.QLabel(gestionepartite)
        self.label2.setGeometry(QtCore.QRect(190, 20, 71, 16))
        self.label2.setObjectName("labeldue")

        self.tabellapartite = QtWidgets.QTableWidget(gestionepartite)
        self.tabellapartite.setGeometry(QtCore.QRect(10, 180, 461, 121))
        self.tabellapartite.setObjectName("tabellapartite")
        self.tabellapartite.setColumnCount(4)
        self.tabellapartite.setRowCount(0)
        self.tabellapartite.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.tabellapartite.setHorizontalHeaderLabels(["Giocatore 1","Punteggio","Giocatore 2","Punteggio"])
        self.tabellapartite.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        #Partite di utente prenotante
        self.label3 = QtWidgets.QLabel(gestionepartite)
        self.label3.setGeometry(QtCore.QRect(10, 160, 141, 16))
        self.label3.setObjectName("labeltre")

        self.statistiche = QtWidgets.QLineEdit(gestionepartite)
        self.statistiche.setGeometry(QtCore.QRect(250, 150, 113, 21))
        self.statistiche.setObjectName("statistiche")
        self.statistiche.setReadOnly(True)

        #Tendenza vittorie
        self.label4 = QtWidgets.QLabel(gestionepartite)
        self.label4.setGeometry(QtCore.QRect(250, 130, 111, 16))
        self.label4.setObjectName("labelquattro")

        #Aggiungi
        self.aggiungipartita = QtWidgets.QPushButton(gestionepartite)
        self.aggiungipartita.setGeometry(QtCore.QRect(30, 120, 113, 32))
        self.aggiungipartita.setObjectName("aggiungipartita")

        #visualizza subito le partite fatte quel giorno dall'utente
        self.visualizzaPartite()

        self.aggiungipartita.clicked.connect(self.aggiungiPartita)
        self.tabellapartite.doubleClicked.connect(self.modificaPartita)

        self.retranslateUi(gestionepartite)
        QtCore.QMetaObject.connectSlotsByName(gestionepartite)

    def retranslateUi(self, gestionepartite):
        _translate = QtCore.QCoreApplication.translate
        gestionepartite.setWindowTitle(_translate("gestionepartite", "Form"))
        self.label1.setText(_translate("gestionepartite", "Giocatore1"))
        self.label2.setText(_translate("gestionepartite", "Giocatore2"))
        self.label3.setText(_translate("gestionepartite", "Partite di: "+Ui_gestionepartite.prenotazione.utente.nome))
        self.label4.setText(_translate("gestionepartite", "Tendenza vittorie"))
        self.aggiungipartita.setText(_translate("gestionepartite", "Aggiungi"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gestionepartite = QtWidgets.QWidget()
    ui = Ui_gestionepartite()
    ui.setupUi(gestionepartite)
    gestionepartite.show()
    sys.exit(app.exec_())
