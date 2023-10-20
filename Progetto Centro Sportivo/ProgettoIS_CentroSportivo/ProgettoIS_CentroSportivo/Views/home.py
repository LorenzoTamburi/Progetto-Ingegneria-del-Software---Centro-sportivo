# questa classe rappresenta l'interfaccia grafica principale dell'applicazione e contiene i metodi per gestire
# l'accesso alle varie funzionalità dell'applicazione, come il login, la registrazione, la gestione delle prenotazioni
# e dell'organizzazione, la gestione del backup dei dati e il logout dell'utente

from PyQt5 import QtCore, QtWidgets
from ProgettoIS_CentroSportivo.Handler.HandlerUtenti import HandlerUtenti
from ProgettoIS_CentroSportivo.Views.gestionebackup import Ui_gestionebackup
from ProgettoIS_CentroSportivo.Views.gestione_organizzazione import Ui_gestioneOrganizzazione
from ProgettoIS_CentroSportivo.Views.login import Login
from ProgettoIS_CentroSportivo.Views.prenotazioni import Ui_prenotazioni
from ProgettoIS_CentroSportivo.Views.registrazione_socio import Ui_registrazionesocio

class Ui_Form(object):

    # metodo che permette di accedere all'interfaccia per la gestione del backup dei dati dell'applicazione
    # solo se si effettuato il login come admin
    def gestioneBackup(self):
        if (HandlerUtenti.loginEffettuato == True
                and (HandlerUtenti.utenteConnesso.isAdmin == True)):
            self.window_conferma = QtWidgets.QDialog()
            self.ui_conferma = Ui_gestionebackup()
            self.ui_conferma.setupUi(self.window_conferma)
            self.window_conferma.show()

    # metodo che permette di accedere all'interfaccia per la gestione dell'utente per effettuare
    # il login o la registrazione
    def gestioneUtente(self):
        self.login = QtWidgets.QMainWindow()
        self.ui_login = Login()
        self.ui_login.setupUi(self.login)
        self.login.show()

    # metodo che permette a un utente registrato, ma non amministratore,
    # di accedere all'interfaccia per tesserarsi
    def gestioneTesseramento(self):
        if (HandlerUtenti.loginEffettuato == True and HandlerUtenti.utenteConnesso.isAdmin == False):
            self.window=QtWidgets.QWidget()
            self.ui=Ui_registrazionesocio()
            self.ui.setupUi(self.window)
            self.window.show()

    # metodo che permette solo all'amministratore di accedere all'interfaccia per la visualizzazione delle
    # liste di utenti
    def gestioneOrganizzazione(self):
        if (HandlerUtenti.loginEffettuato == True and HandlerUtenti.utenteConnesso.isAdmin == True):
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_gestioneOrganizzazione()
            self.ui.setupUi(self.window)
            self.window.show()

    # metodo che permette di accedere all'interfaccia per la gestione delle prenotazioni
    # solo se è stato effettuato il login
    def gestionePrenotazioni(self):
        if (HandlerUtenti.loginEffettuato == True):
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_prenotazioni()
            self.ui.setupUi(self.window)
            self.window.show()

    # metodo che esegue il logout dell'utente e chiude l'applicazione
    def logoutHome(self):
        # Chiudo la finestra corrente
        Form = self.gestioneprenotazioni.window()
        Form.close()
        # Termina l'applicazione
        QtWidgets.QApplication.quit()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 405)

        self.gestioneprenotazioni = QtWidgets.QPushButton(Form)
        self.gestioneprenotazioni.setGeometry(QtCore.QRect(20, 30, 171, 111))
        self.gestioneprenotazioni.setObjectName("gestionePrenotazioni")

        self.gestioneutente = QtWidgets.QPushButton(Form)
        self.gestioneutente.setGeometry(QtCore.QRect(20, 150, 171, 111))
        self.gestioneutente.setObjectName("gestioneUtente")

        self.gestionetesseramento = QtWidgets.QPushButton(Form)
        self.gestionetesseramento.setGeometry(QtCore.QRect(20, 270, 171, 111))
        self.gestionetesseramento.setObjectName("gestioneTesseramento")

        self.gestionetorneo = QtWidgets.QPushButton(Form)
        self.gestionetorneo.setGeometry(QtCore.QRect(210, 30, 171, 111))
        self.gestionetorneo.setObjectName("gestioneBackup")

        self.gestioneorganizzazione = QtWidgets.QPushButton(Form)
        self.gestioneorganizzazione.setGeometry(QtCore.QRect(210, 150, 171, 111))
        self.gestioneorganizzazione.setObjectName("gestioneOrganizzazione")

        self.logout = QtWidgets.QPushButton(Form)
        self.logout.setGeometry(QtCore.QRect(210, 270, 85, 50))
        self.logout.setObjectName("logout")

        # azioni dei pulsanti
        self.gestioneutente.clicked.connect(self.gestioneUtente)
        self.gestionetesseramento.clicked.connect(self.gestioneTesseramento)
        self.gestioneorganizzazione.clicked.connect(self.gestioneOrganizzazione)
        self.gestioneprenotazioni.clicked.connect(self.gestionePrenotazioni)
        self.gestionetorneo.clicked.connect(self.gestioneBackup)
        self.logout.clicked.connect(self.logoutHome)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.gestioneprenotazioni.setText(_translate("Form", "Prenotazioni"))
        self.gestioneutente.setText(_translate("Form", "Gestione Utente"))
        self.gestionetesseramento.setText(_translate("Form", "Tesseramento"))
        self.gestionetorneo.setText(_translate("Form", "Backup"))
        self.gestioneorganizzazione.setText(_translate("Form", "Visualizza\n Utenti"))
        self.logout.setText(_translate("Form", "Esci"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
