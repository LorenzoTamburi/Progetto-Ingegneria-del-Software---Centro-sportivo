# Classe che gestisce la registrazione di un nuovo socio e l'interfaccia grafica apposita, con tutti i metodi
# necessari al tesseramento

from PyQt5 import QtCore, QtWidgets
import re
from ProgettoIS_CentroSportivo.Handler.HandlerUtenti import HandlerUtenti
from ProgettoIS_CentroSportivo.Views.popup_ok import Ui_conferma

class Ui_registrazionesocio(object):

    # metodo che gestisce il tesseramento
    def tesseramento(self):
        appoggioCF = self.codicefiscale.text()
        appoggioEM = self.email.text()
        flag1 = 0
        flag2 = 0
        for x in appoggioEM:
            if(x=="@"):
                flag1 = 1
            if(x=="."):
                flag2 = 1

    # controllo codice fiscale ed email
        if (self.is_valid_codice_fiscale(appoggioCF) and flag1 == 1 and flag2 == 1 ):
            codiceFiscale=self.codicefiscale.text()
            email = self.email.text()
            self.popup()
            HandlerUtenti.creaTesseramento(email, codiceFiscale)
        else:
            self.popupET()

    # metodo che controlla la correttezza del codice fiscale
    def is_valid_codice_fiscale(self, codice):
        pattern = re.compile("[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]")
        if pattern.fullmatch(codice):
            return True
        else:
            return False

    # metodo che chiama il pop up per confermare il tesseramento
    def popup(self):
        self.window_tesseramento = QtWidgets.QDialog()
        self.ui_tesseramento = Ui_conferma()
        self.ui_tesseramento.setupUi(self.window_tesseramento, "Tesseramento effettuato con successo")
        self.window_tesseramento.show()

    # metodo che chiama il pop up per avvisare dell'errore nel tesseramento
    def popupET(self):
        self.window_etesseramento = QtWidgets.QDialog()
        self.ui_etesseramento = Ui_conferma()
        self.ui_etesseramento.setupUi(self.window_etesseramento, "Hai sbagliato a mettere i campi")
        self.window_etesseramento.show()

    def setupUi(self, registrazionesocio):
        registrazionesocio.setObjectName("registrazionesocio")
        registrazionesocio.resize(500, 170)

        #inserimento testo codice fiscale
        self.codicefiscale = QtWidgets.QLineEdit(registrazionesocio)
        self.codicefiscale.setGeometry(QtCore.QRect(172, 30, 245, 21))
        self.codicefiscale.setObjectName("codicefiscale")

        self.label = QtWidgets.QLabel(registrazionesocio)
        self.label.setGeometry(QtCore.QRect(69, 30, 98, 20))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(registrazionesocio)
        self.label_2.setGeometry(QtCore.QRect(110, 60, 45, 20))
        self.label_2.setObjectName("label_2")

        # inserimento testo email
        self.email = QtWidgets.QLineEdit(registrazionesocio)
        self.email.setGeometry(QtCore.QRect(173, 60, 245, 21))
        self.email.setObjectName("email")

        self.frame = QtWidgets.QFrame(registrazionesocio)
        self.frame.setGeometry(QtCore.QRect(70, 90, 261, 91))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 91, 51))
        self.label_3.setObjectName("label_3")

        self.invia = QtWidgets.QPushButton(registrazionesocio)
        self.invia.setGeometry(QtCore.QRect(305, 100, 113, 32))
        self.invia.setObjectName("Invia")

        self.frame.raise_()
        self.codicefiscale.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.email.raise_()
        self.invia.raise_()

        #azioni dei pulsanti (se è già un socio o è admin pulsante non funziona
        if (HandlerUtenti.utenteConnesso.tesserato
                or HandlerUtenti.utenteConnesso.isAdmin == True ):
            self.invia.setEnabled(False)
        else:
            self.invia.clicked.connect(self.tesseramento)

        self.retranslateUi(registrazionesocio)
        QtCore.QMetaObject.connectSlotsByName(registrazionesocio)

    def retranslateUi(self, registrazionesocio):
        _translate = QtCore.QCoreApplication.translate
        registrazionesocio.setWindowTitle(_translate("registrazionesocio", "Form"))
        self.label.setText(_translate("registrazionesocio", "Codice Fiscale"))
        self.label_2.setText(_translate("registrazionesocio", "E-mail"))
        self.invia.setText(_translate("registrazionesocio", "Invia"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    registrazionesocio = QtWidgets.QWidget()
    ui = Ui_registrazionesocio()
    ui.setupUi(registrazionesocio)
    registrazionesocio.show()
    sys.exit(app.exec_())
