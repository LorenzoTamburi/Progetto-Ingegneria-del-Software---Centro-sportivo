# Classe che gestisce la registrazione di un nuovo utente e l'interfaccia grafica apposita

from PyQt5 import QtCore, QtWidgets
from ProgettoIS_CentroSportivo.Model.Utente import Utente
from ProgettoIS_CentroSportivo.Handler.HandlerUtenti import HandlerUtenti
from ProgettoIS_CentroSportivo.Views.popup_ok import Ui_conferma

class UI_Iscrizione(object):

    # metodo per la creazione di un nuovo utente
    def creaUtente(self):
        if(self.nome.text() != ""
                and self.cognome.text() != ""
                and self.nomeUtente.text() != ""
                and self.password.text() != ""
                and self.cellulare.text() != ""
                and self.dataNascita.text() != ""):

            campoNome = self.nome.text()
            campoCognome = self.cognome.text()
            campoNomeUtente = self.nomeUtente.text()
            campoPassword = self.password.text()
            campoCellulare = self.cellulare.text()
            campoDataNascita = self.dataNascita.text()
            nuovoUtente = Utente(campoNome, campoCognome, campoDataNascita, campoCellulare, campoPassword, campoNomeUtente)
            unicita = True
            for x in HandlerUtenti.collectionUtenti:
                if(x.nomeUtente == campoNomeUtente): unicita = False
            if(unicita == True):
                HandlerUtenti.inserisciUtente(nuovoUtente)
                self.window_conferma = QtWidgets.QDialog()
                self.ui_conferma = Ui_conferma()
                self.ui_conferma.setupUi(self.window_conferma, "Iscrizione effettuata con successo" )
                self.window_conferma.show()
            else:
                self.popupEI("Nome utente già in uso")
        else:
            self.popupEI("Devi riempire tutti i campi")

    # popup errore nell'iscirzione per campi mancanti
    def popupEI(self, messaggio):
        self.window_eiscrizione = QtWidgets.QDialog()
        self.ui_eiscrizione = Ui_conferma()
        self.ui_eiscrizione.setupUi(self.window_eiscrizione, messaggio)
        self.window_eiscrizione.show()

    # popup modifica avvenuta con successo
    def popupMod(self):
        self.window_miscrizione = QtWidgets.QDialog()
        self.ui_miscrizione = Ui_conferma()
        self.ui_miscrizione.setupUi(self.window_miscrizione, "Modifica effettuata")
        self.window_miscrizione.show()

    # metodo per modificare le generalità dell'utente
    def modificaUtente(self):
        campoNome = self.nome.text()
        campoCognome = self.cognome.text()
        campoNomeUtente = self.nomeUtente.text()
        campoPassword = self.password.text()
        campoCellulare = self.cellulare.text()
        campoDataNascita = self.dataNascita.text()
        utenteModificato=Utente(campoNome, campoCognome, campoDataNascita, campoCellulare, campoPassword, campoNomeUtente)
        HandlerUtenti.modificaUtente(HandlerUtenti.utenteConnesso, utenteModificato)
        self.popupMod()

    # metodo per modificare le generalità dell'utente da parte dell'admin in gestione organizzazione
    def modificaUtenteAdmin(self):
        idUtente = UI_Iscrizione.idUtente
        print(idUtente)
        campoNome = self.nome.text()
        campoCognome = self.cognome.text()
        campoNomeUtente = self.nomeUtente.text()
        campoPassword = self.password.text()
        campoCellulare = self.cellulare.text()
        campoDataNascita = self.dataNascita.text()
        utenteModificato=Utente(campoNome, campoCognome, campoDataNascita, campoCellulare, campoPassword, campoNomeUtente)
        HandlerUtenti.modificaUtente(HandlerUtenti.collectionUtenti[idUtente], utenteModificato)
        self.popupMod()

    # metodo per gestire l'interfaccia da admin o da utente dell'iscrizione
    def setupUi(self, Iscrizione, idUtente, gestione):
        UI_Iscrizione.idUtente = idUtente
        Iscrizione.setObjectName("Iscrizione")
        Iscrizione.resize(400, 300)

        self.cognome = QtWidgets.QLineEdit(Iscrizione)
        self.cognome.setGeometry(QtCore.QRect(150, 60, 141, 21))
        self.cognome.setObjectName("cognome")

        self.password = QtWidgets.QLineEdit(Iscrizione)
        self.password.setGeometry(QtCore.QRect(150, 120, 141, 21))
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

        self.nomeUtente = QtWidgets.QLineEdit(Iscrizione)
        self.nomeUtente.setGeometry(QtCore.QRect(150, 90, 141, 21))
        self.nomeUtente.setObjectName("nomeUtente")

        self.nome = QtWidgets.QLineEdit(Iscrizione)
        self.nome.setGeometry(QtCore.QRect(150, 30, 141, 21))
        self.nome.setObjectName("nome")

        self.dataNascita = QtWidgets.QLineEdit(Iscrizione)
        self.dataNascita.setGeometry(QtCore.QRect(150, 180, 141, 21))
        self.dataNascita.setObjectName("dataNascita")

        self.label = QtWidgets.QLabel(Iscrizione)
        self.label.setGeometry(QtCore.QRect(100, 30, 41, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Iscrizione)
        self.label_2.setGeometry(QtCore.QRect(80, 60, 60, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Iscrizione)
        self.label_3.setGeometry(QtCore.QRect(59, 90, 81, 20))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(Iscrizione)
        self.label_4.setGeometry(QtCore.QRect(80, 120, 60, 16))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(Iscrizione)
        self.label_5.setGeometry(QtCore.QRect(80, 150, 60, 16))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(Iscrizione)
        self.label_6.setGeometry(QtCore.QRect(50, 180, 101, 20))
        self.label_6.setObjectName("label_6")

        self.invia = QtWidgets.QPushButton(Iscrizione)
        self.invia.setGeometry(QtCore.QRect(150, 220, 113, 32))
        self.invia.setFlat(False)
        self.invia.setObjectName("invia")

        self.cellulare = QtWidgets.QLineEdit(Iscrizione)
        self.cellulare.setGeometry(QtCore.QRect(150, 150, 141, 21))
        self.cellulare.setObjectName("cellulare")

        if(HandlerUtenti.loginEffettuato and
                HandlerUtenti.utenteConnesso.isAdmin == False):
            self.nome.setText(HandlerUtenti.utenteConnesso.nome)
            self.cognome.setText(HandlerUtenti.utenteConnesso.cognome)
            self.dataNascita.setText(HandlerUtenti.utenteConnesso.dataNascita)
            self.password.setText(HandlerUtenti.utenteConnesso.password)
            self.nomeUtente.setText(HandlerUtenti.utenteConnesso.nomeUtente)
            self.cellulare.setText(HandlerUtenti.utenteConnesso.cellulare)
            self.invia.clicked.connect(self.modificaUtente)

        elif(HandlerUtenti.loginEffettuato and
              HandlerUtenti.utenteConnesso.isAdmin == True
              and gestione == True):
            self.nome.setText(HandlerUtenti.collectionUtenti[idUtente].nome)
            self.cognome.setText(HandlerUtenti.collectionUtenti[idUtente].cognome)
            self.dataNascita.setText(HandlerUtenti.collectionUtenti[idUtente].dataNascita)
            self.password.setText(HandlerUtenti.collectionUtenti[idUtente].password)
            self.nomeUtente.setText(HandlerUtenti.collectionUtenti[idUtente].nomeUtente)
            self.cellulare.setText(HandlerUtenti.collectionUtenti[idUtente].cellulare)
            self.invia.clicked.connect(self.modificaUtenteAdmin)
        else:
            self.invia.clicked.connect(self.creaUtente)

        Iscrizione.setTabOrder(self.nome, self.cognome)
        Iscrizione.setTabOrder(self.cognome, self.nomeUtente)
        Iscrizione.setTabOrder(self.nomeUtente, self.password)
        Iscrizione.setTabOrder(self.password, self.cellulare)
        Iscrizione.setTabOrder(self.cellulare, self.dataNascita)
        self.retranslateUi(Iscrizione)
        QtCore.QMetaObject.connectSlotsByName(Iscrizione)

    def retranslateUi(self, Iscrizione):
        _translate = QtCore.QCoreApplication.translate
        Iscrizione.setWindowTitle(_translate("Iscrizione", "Form"))
        self.label.setText(_translate("Iscrizione", "Nome"))
        self.label_2.setText(_translate("Iscrizione", "Cognome"))
        self.label_3.setText(_translate("Iscrizione", "Nome Utente"))
        self.label_4.setText(_translate("Iscrizione", "Password"))
        self.label_5.setText(_translate("Iscrizione", "Cellulare"))
        self.label_6.setText(_translate("Iscrizione", "Data di nascita"))
        self.invia.setText(_translate("Iscrizione", "Invia"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Iscrizione = QtWidgets.QWidget()
    ui = Iscrizione()
    ui.setupUi(Iscrizione)
    Iscrizione.show()
    sys.exit(app.exec_())