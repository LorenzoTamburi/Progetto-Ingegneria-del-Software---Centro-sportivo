# Classe che rappresenta l'interfaccia grafica per l'autenticazione dell'utente nell'applicazione

from PyQt5 import QtCore, QtWidgets

from ProgettoIS_CentroSportivo.Views.popup_ok import Ui_conferma
from ProgettoIS_CentroSportivo.Views.registrazione_utente import UI_Iscrizione
from ProgettoIS_CentroSportivo.Handler.HandlerUtenti import HandlerUtenti

class Login(object):

    # metodo che permette di verificare le credenziali inserite dall'utente e di effettuare il login.
    # Se l'autenticazione ha successo, viene impostato lo stato di login dell'utente e viene visualizzato
    # un messaggio di conferma
    def autenticazione(self, Form):
        nomeUtente = self.nomeUtente.text()
        pwd = self.password.text()
        for x in HandlerUtenti.collectionUtenti:
            if x.nomeUtente == nomeUtente and x.password == pwd:
                HandlerUtenti.setLoginEffettuato(self)
                HandlerUtenti.setUtenteConnesso(x)
                self.logIn.setEnabled(False)
                self.logOut.setEnabled(True)
                self.iscriviti.setEnabled(False)
                self.loginPopup()
                Form.close()

        if (HandlerUtenti.utenteConnesso!= None and HandlerUtenti.utenteConnesso.isAdmin == True):
            self.modifica.setEnabled(False)
            self.iscriviti.setEnabled(True)
        else:
            self.modifica.setEnabled(True)

        if(HandlerUtenti.utenteConnesso == None):
            self.logOut.setEnabled(False)
            self.logIn.setEnabled(True)
            self.modifica.setEnabled(False)
            self.iscriviti.setEnabled(True)
            self.window_conferma = QtWidgets.QDialog()
            self.ui_conferma = Ui_conferma()
            self.ui_conferma.setupUi(self.window_conferma, "Login errato")
            self.window_conferma.show()

    # metodo che chiude la finestra di pop up
    def close_popup(self):
        self.window_conferma.accept(self)

    # metodo che visualizza un messaggio di conferma dopo il login dell'utente
    def loginPopup(self):
        self.window_conferma = QtWidgets.QDialog()
        self.ui_conferma = Ui_conferma()
        self.ui_conferma.setupUi(self.window_conferma, "Login effettuato con successo")
        self.window_conferma.show()
        self.logIn.setEnabled(False)
        self.logOut.setEnabled(True)
        self.iscriviti.setEnabled(True)
        self.modifica.setEnabled(True)

    # metodo che visualizza un messaggio di conferma dopo il logout dell'utente
    def logoutPopup(self):
        if HandlerUtenti.loginEffettuato == True:
            HandlerUtenti.setLogoutEffettuato(self)

            self.window_conferma = QtWidgets.QDialog()
            self.ui_conferma = Ui_conferma()
            self.ui_conferma.setupUi(self.window_conferma, "Logout effettuato con successo")
            self.window_conferma.show()

            self.logIn.setEnabled(True)
            self.logOut.setEnabled(False)
            self.iscriviti.setEnabled(True)

    # metodo che permette di accedere all'interfaccia per l'iscrizione di un nuovo utente
    def iscrizione(self):
        self.window_iscrizione = QtWidgets.QMainWindow()
        self.ui_iscrizione = UI_Iscrizione()
        self.ui_iscrizione.setupUi(self.window_iscrizione, 0, False)
        self.window_iscrizione.show()

    # metodo che permette di accedere all'interfaccia per la modifica dei dati dell'utente connesso
    def modificaDati(self):
        if (HandlerUtenti.loginEffettuato):
            self.window_iscrizione = QtWidgets.QMainWindow()
            self.ui_iscrizione = UI_Iscrizione()
            self.ui_iscrizione.setupUi(self.window_iscrizione, 0, False)
            self.window_iscrizione.show()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(467, 269)

        self.logIn = QtWidgets.QPushButton(Form)
        self.logIn.setGeometry(QtCore.QRect(120, 140, 113, 32))
        self.logIn.setObjectName("logIn")

        self.logOut = QtWidgets.QPushButton(Form)
        self.logOut.setGeometry(QtCore.QRect(120, 210, 113, 32))
        self.logOut.setObjectName("logOut")

        self.modifica = QtWidgets.QPushButton(Form)
        self.modifica.setGeometry(QtCore.QRect(280, 210, 113, 32))
        self.modifica.setObjectName("modifica")

        self.iscriviti = QtWidgets.QPushButton(Form)
        self.iscriviti.setGeometry(QtCore.QRect(280, 140, 113, 32))
        self.iscriviti.setObjectName("iscriviti")

        self.nomeUtente = QtWidgets.QLineEdit(Form)
        self.nomeUtente.setGeometry(QtCore.QRect(170, 70, 171, 21))
        self.nomeUtente.setObjectName("nomeUtente")

        self.password = QtWidgets.QLineEdit(Form)
        self.password.setGeometry(QtCore.QRect(170, 100, 171, 21))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")

        #NomeUtente
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(78, 70, 91, 20))
        self.label.setObjectName("label")

        #Password
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(100, 100, 70, 20))
        self.label_2.setObjectName("label_2")

        if(HandlerUtenti.loginEffettuato):
            self.logOut.setEnabled(True)
            self.logIn.setEnabled(False)
            self.iscriviti.setEnabled(False)
            self.nomeUtente.setText(HandlerUtenti.utenteConnesso.nomeUtente)

            if(HandlerUtenti.utenteConnesso.isAdmin):
                self.modifica.setEnabled(False)

        else:
            self.logOut.setEnabled(False)
            self.logIn.setEnabled(True)
            self.modifica.setEnabled(False)

        # azione quando i pulsanti si cliccano
        self.logIn.clicked.connect(lambda: self.autenticazione(Form))
        self.iscriviti.clicked.connect(self.iscrizione)
        self.modifica.clicked.connect(self.modificaDati)
        self.logOut.clicked.connect(self.logoutPopup)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    # Funzione che serve per scrivere i testi che compariranno a schermo
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.logIn.setText(_translate("Form", "Login"))
        self.iscriviti.setText(_translate("Form", "Iscriviti"))
        self.label.setText(_translate("Form", "Nome utente"))
        self.label_2.setText(_translate("Form", "Password"))
        self.modifica.setText(_translate("Form", "Modifica"))
        self.logOut.setText(_translate("Form", "Logout"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Login()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
