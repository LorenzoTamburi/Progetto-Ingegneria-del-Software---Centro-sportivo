# Classe per gestire la visualizzazione delle liste di tutti gli utenti iscritti e di tutti gli utenti tesserati
# stampandoli in due tabelle

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from ProgettoIS_CentroSportivo.Handler.HandlerUtenti import HandlerUtenti

class Ui_visualizzazioneliste(object):

    #ritorna la riga selezionata nella tabella
    def getRigaSelezionata(self):
        return self.tabellautenti.currentRow()

    # metodo per ricavare la tabella con tutti gli utenti iscritti
    def selezione(self):
        from ProgettoIS_CentroSportivo.Views.registrazione_utente import UI_Iscrizione
        self.window_iscrizione = QtWidgets.QMainWindow()
        self.ui_iscrizione = UI_Iscrizione()
        self.ui_iscrizione.setupUi(self.window_iscrizione, self.tabellautenti.currentRow(), True)
        self.window_iscrizione.show()

    # metodo per gestire l'interfaccia grafica che stampa le tabelle
    def setupUi(self, visualizzazioneliste, visualizzasoci):

        visualizzazioneliste.setObjectName("visualizzazioneliste")
        visualizzazioneliste.resize(822, 334)
        self.buttonBox = QtWidgets.QDialogButtonBox(visualizzazioneliste)
        self.buttonBox.setGeometry(QtCore.QRect(340, 290, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)

        self.buttonBox.setObjectName("buttonBox")

        self.tabellautenti = QtWidgets.QTableWidget(visualizzazioneliste)
        self.tabellautenti.setGeometry(QtCore.QRect(40, 10, 741, 251))
        self.tabellautenti.setObjectName("tabellautenti")
        self.tabellautenti.setColumnCount(7) #numero colonne
        self.tabellautenti.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.tabellautenti.setHorizontalHeaderLabels(["Nome", "Cognome", "Data di nascita", "Cellulare", "Username", "Password", "Socio"])
        self.retranslateUi(visualizzazioneliste)

        self.buttonBox.accepted.connect(visualizzazioneliste.accept)

        QtCore.QMetaObject.connectSlotsByName(visualizzazioneliste)

        # griglia non modificabile
        self.tabellautenti.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        if(visualizzasoci == True):
            self.tabellautenti.setRowCount(HandlerUtenti.contaSoci)
            j = 0
            for i in range(len(HandlerUtenti.collectionUtenti) - 2):

                if HandlerUtenti.collectionUtenti[i].tesserato == True:
                    item = QTableWidgetItem(HandlerUtenti.collectionUtenti[i].nome)
                    self.tabellautenti.setItem(j, 0, item)
                    item = QTableWidgetItem(HandlerUtenti.collectionUtenti[i].cognome)
                    self.tabellautenti.setItem(j, 1, item)
                    item = QTableWidgetItem(HandlerUtenti.collectionUtenti[i].dataNascita)
                    self.tabellautenti.setItem(j, 2, item)
                    item = QTableWidgetItem(HandlerUtenti.collectionUtenti[i].cellulare)
                    self.tabellautenti.setItem(j, 3, item)
                    item = QTableWidgetItem(HandlerUtenti.collectionUtenti[i].nomeUtente)
                    self.tabellautenti.setItem(j, 4, item)
                    item = QTableWidgetItem(HandlerUtenti.collectionUtenti[i].password)
                    self.tabellautenti.setItem(j, 5, item)
                    item = QTableWidgetItem(str(HandlerUtenti.collectionUtenti[i].getTesseramento()))
                    self.tabellautenti.setItem(j, 6, item)
                    j+=1
        else:
            self.tabellautenti.setRowCount(len(HandlerUtenti.collectionUtenti) - 1)

            #sottraggo 1 che sono gli account in cima alla lista: admin non voglio si veda
            for i in range(len(HandlerUtenti.collectionUtenti) - 1):
                item = QTableWidgetItem(HandlerUtenti.collectionUtenti[i].nome)
                self.tabellautenti.setItem(i, 0, item)
                item = QTableWidgetItem(HandlerUtenti.collectionUtenti[i].cognome)
                self.tabellautenti.setItem(i, 1, item)
                item = QTableWidgetItem(HandlerUtenti.collectionUtenti[i].dataNascita)
                self.tabellautenti.setItem(i, 2, item)
                item = QTableWidgetItem(HandlerUtenti.collectionUtenti[i].cellulare)
                self.tabellautenti.setItem(i, 3, item)
                item = QTableWidgetItem(HandlerUtenti.collectionUtenti[i].nomeUtente)
                self.tabellautenti.setItem(i, 4, item)
                item = QTableWidgetItem(HandlerUtenti.collectionUtenti[i].password)
                self.tabellautenti.setItem(i, 5, item)
                item = QTableWidgetItem(str(HandlerUtenti.collectionUtenti[i].getTesseramento()))
                self.tabellautenti.setItem(i, 6, item)
        if(HandlerUtenti.utenteConnesso.isAdmin == True): self.tabellautenti.doubleClicked.connect(self.selezione)

    def retranslateUi(self, visualizzazioneliste):
        _translate = QtCore.QCoreApplication.translate
        visualizzazioneliste.setWindowTitle(_translate("visualizzazioneliste", "Dialog"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    visualizzazioneliste = QtWidgets.QDialog()
    ui = Ui_visualizzazioneliste()
    ui.setupUi(visualizzazioneliste)
    visualizzazioneliste.show()
    sys.exit(app.exec_())
