# classe che rappresenta il menu utente per la prenotazione di un campo da gioco e fornisce metodi per
# gestire la selezione degli optional e l'aggiunta di eventtuali giocatori tesserati, il calcolo del totale
# della prenotazione e la conferma della prenotazione stessa

import datetime, re
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QCheckBox, QVBoxLayout, QPushButton, QLabel, QDialog, QHBoxLayout, \
    QLineEdit

from ProgettoIS_CentroSportivo.Handler.HandlerUtenti import HandlerUtenti
from ProgettoIS_CentroSportivo.Views.popup_ok import Ui_conferma

class Ui_menuprenotazione(object):
    calciatori = []
    prenotazione_confermata = False  # definisci l'attributo

    # metodo che inizializza la GUI del menu di prenotazione e la mostra all'utente
    def setupUI(self, max, mess, data):
        dialog = QDialog()
        dialog.setWindowTitle('Menu prenotazione')

        data_dt = datetime.datetime.strptime(data, "%Y, %m, %d")  # converti la stringa in un oggetto datetime
        data_str = data_dt.strftime("%d-%m-%Y")  # formatta l'oggetto datetime

        dialog.vbox = QVBoxLayout()

        messaggio = 'Riepilogo prenotazione:\nCalcio a '+ str((max-1)//2)+', campo a'+mess+', ' + data_str
        # Aggiungi il QLabel con il testo sopra alla checkbox
        label = QLabel(messaggio)
        label.setAlignment(QtCore.Qt.AlignLeft)
        dialog.vbox.addWidget(label)

        self.cb1 = QCheckBox('Palloni 1€ a persona')
        self.cb1.stateChanged.connect(self.checkbox_checked)

        self.cb2 = QCheckBox('Casacche 1€ a persona')
        self.cb2.stateChanged.connect(self.checkbox_checked)

        self.cb3 = QCheckBox('Docce 3€ a persona')
        self.cb3.stateChanged.connect(self.checkbox_checked)

        dialog.vbox.addWidget(self.cb1)
        dialog.vbox.addWidget(self.cb2)
        dialog.vbox.addWidget(self.cb3)

        self.lbl = QLabel('Totale per ogni giocatore non tesserato:5€')
        dialog.vbox.addWidget(self.lbl)

        self.lbl_tesserati = QLabel('Numero di giocatori tesserati: 0')
        dialog.vbox.addWidget(self.lbl_tesserati)

        self.btn = QPushButton('Inserisci tesserati')
        self.btn.clicked.connect(lambda: self.inserisciTesserati(max, dialog))
        dialog.vbox.addWidget(self.btn)

        self.btn2 = QPushButton('Conferma')
        self.btn2.clicked.connect(lambda: self.conferma_prenotazione(messaggio, max, self.lbl, self.lbl_tesserati))
        self.btn2.clicked.connect(lambda: self.conferma(dialog))
        dialog.vbox.addWidget(self.btn2)

        dialog.setLayout(dialog.vbox)
        dialog.setGeometry(300, 300, 350, 200)
        dialog.setWindowTitle('Menu')
        dialog.exec_()

    # metodo che calcola la spesa totale della prenotazione in base alla selezione dell'utente
    def calcoloSpesa(self, lbl, lbltesserati, max):

        #x = totale di euro per ogni giocatore non tesserato
        x = int(re.findall(r'\d+', lbl.text())[0])
        #num = numero di giocatori tesserati
        num = int(re.findall(r'\d+', lbltesserati.text())[0])
        tot = (max-1 - num)*x + (num*5)
        return tot

    # metodo che conferma la prenotazione dell'utente e mostra un messaggio di conferma
    def conferma_prenotazione(self, mess, max, lbl, lbl_tesserati):
        tot = self.calcoloSpesa(lbl, lbl_tesserati, max)
        messaggio = mess + "\nSpesa totale = "+str(tot)+"€"
        conferma_dialog = QtWidgets.QDialog()
        ui_conferma = Ui_conferma()
        ui_conferma.setupUi(conferma_dialog, messaggio)
        conferma_dialog.exec_()

    # metodo viene chiamato ogni volta che l'utente seleziona o deseleziona una checkbox.
    # Aggiorna il valore del totale per ogni giocatore non tesserato
    def checkbox_checked(self):
        x = 0
        if self.cb1.isChecked():
            x += 1
        if self.cb2.isChecked():
            x += 1
        if self.cb3.isChecked():
            x += 3
        self.lbl.setText('Totale per ogni giocatore non tesserato: ' + str(x + 5)+'€')

    # questo metodo mostra una finestra di dialogo per l'inserimento dei giocatori tesserati
    def inserisciTesserati(self, max, dialog):
        dialog2 = QDialog(dialog)
        dialog2.setWindowTitle('Inserisci giocatori tesserati')
        dialog2.vbox = QVBoxLayout()

        self.calciatori = []
        for i in range(1, max):
            hbox = QHBoxLayout()
            label = QLabel('Giocatore ' + str(i) + ':')
            hbox.addWidget(label)
            calciatore = QLineEdit()
            hbox.addWidget(calciatore)
            self.calciatori.append(calciatore)
            dialog2.vbox.addLayout(hbox)

        invio = QPushButton('Invio')
        invio.clicked.connect(lambda: self.pulsanteInvio(dialog2))
        dialog2.vbox.addWidget(invio)
        dialog2.setLayout(dialog2.vbox)
        dialog2.exec_()

    # metodo che viene chiamato quando l'utente preme il pulsante Invio nella finestra di dialogo per l'inserimento
    # dei giocatori tesserati. Aggiorna il numero di giocatori tesserati nella GUI
    def pulsanteInvio(self, dialog2):
        calciatori_tesserati = []
        for calciatore in self.calciatori:
            if not calciatore.text() == '':
                for utente in HandlerUtenti.collectionUtenti:
                    if str(calciatore.text()) == str(utente.nomeUtente) and utente.tesserato:
                        if(calciatore.text() not in calciatori_tesserati):
                            calciatori_tesserati.append(calciatore.text())

        self.lbl_tesserati.setText('Numero di tesserati: ' + str(len(calciatori_tesserati)))
        self.calciatori = []
        dialog2.accept()

    # metodo che conferma la prenotazione dell'utente e chiude la finestra di dialogo
    def conferma(self, dialog):
        self.prenotazione_confermata = True
        dialog.accept()


if __name__ == '__main__':
    app = QApplication([])
    ui = Ui_menuprenotazione()
    ui.setupUI(5)
    app.exec_()