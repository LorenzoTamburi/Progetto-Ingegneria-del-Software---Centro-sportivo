from datetime import datetime
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from ProgettoIS_CentroSportivo.Handler.HandlerUtenti import HandlerUtenti
from ProgettoIS_CentroSportivo.Handler.HandlerPrenotazioni import HandlerPrenotazioni
from ProgettoIS_CentroSportivo.Views.popup_ok import Ui_conferma
from ProgettoIS_CentroSportivo.Views.popup_okcancel import Ui_verifica
from ProgettoIS_CentroSportivo.Views.visualizzazione_liste import Ui_visualizzazioneliste
from ProgettoIS_CentroSportivo.Views.gestionepartite import Ui_gestionepartite
from ProgettoIS_CentroSportivo.Views.menu_prenotazione import Ui_menuprenotazione

class Ui_prenotazioni(object):

    # metodo che gestisce la chiamata degli altri metodi per la gestione delle partite
    def gestionePartite(self):
        if (self.tabellaprenotazioni.currentItem() == None):
            self.window_conferma = QtWidgets.QDialog()
            self.ui_conferma = Ui_conferma()
            self.ui_conferma.setupUi(self.window_conferma, "Nessuna prenotazione trovata")
            self.window_conferma.show()
        else:
            data = str(self.calendario.selectedDate()) \
            .replace('PyQt5.QtCore.QDate', '') \
            .replace('(', '') \
            .replace(')', '')
            riga = self.tabellaprenotazioni.currentRow()
            colonna = self.tabellaprenotazioni.currentColumn()
            self.window = QtWidgets.QMainWindow()
            prenotazione = HandlerPrenotazioni.cercaPrenotazione(data, riga, colonna)
            self.ui = Ui_gestionepartite()
            self.ui.setupUi(self.window, prenotazione)
            self.window.show()

    # metodo che elimina la prenotazione selezionata
    def eliminaPrenotazione(self):
        data = str(self.calendario.selectedDate()) \
            .replace('PyQt5.QtCore.QDate', '') \
            .replace('(', '') \
            .replace(')', '')
        riga = self.tabellaprenotazioni.currentRow()
        colonna = self.tabellaprenotazioni.currentColumn()

        if (self.tabellaprenotazioni.currentItem() != None
                and (self.tabellaprenotazioni.currentItem().text() == HandlerUtenti.utenteConnesso.nome
                or HandlerUtenti.utenteConnesso.isAdmin == True)):
            self.window_conferma = QtWidgets.QDialog()
            self.ui_conferma = Ui_verifica()
            self.ui_conferma.setupUi(self.window_conferma,"Vuoi eliminare la prenotazione?")
            if (self.window_conferma.exec() == 1):
                HandlerPrenotazioni.eliminaPrenotazione(data, riga, colonna)
            self.visualizzaPrenotazioni()
        else:
            self.window_conferma = QtWidgets.QDialog()
            self.ui_conferma = Ui_conferma()
            self.ui_conferma.setupUi(self.window_conferma,"Nessuna prenotazione\nda eliminare")
            self.window_conferma.show()

    # metodo che gestisce i metodi e le interfacce necessarie alla prenotazione, da utente o da admin
    def inserisciPrenotazione(self):
        data = str(self.calendario.selectedDate())\
            .replace('PyQt5.QtCore.QDate','')\
            .replace('(','')\
            .replace(')','')
        riga = self.tabellaprenotazioni.currentRow()
        colonna = self.tabellaprenotazioni.currentColumn()

        #prenotazione se si è loggati come admin
        if(self.tabellaprenotazioni.currentItem() == None and HandlerUtenti.utenteConnesso.isAdmin == True):
            self.windows_visualizza = QtWidgets.QDialog()
            self.ui_visualizza = Ui_visualizzazioneliste()
            self.ui_visualizza.setupUi(self.windows_visualizza, False)
            self.windows_visualizza.show()
            if (self.windows_visualizza.exec() == 1):
                if (self.ui_visualizza.tabellautenti.currentItem()!=None):
                    HandlerPrenotazioni.inserisciPrenotazione(data, riga, colonna, self.ui_visualizza.getRigaSelezionata())
                else:
                    self.windows_errore = QtWidgets.QDialog()
                    self.ui_errore = Ui_conferma()
                    self.ui_errore.setupUi(self.windows_errore, "Devi selezionare un utente!")
                    self.windows_errore.show()
             #refresha la tabella per vedere la prenotazione aggiunta
            self.visualizzaPrenotazioni()

        #prenotazione da utente
        elif (self.tabellaprenotazioni.currentItem() == None and len(self.tabellaprenotazioni.selectedIndexes())>0 ):
            self.window_conferma = QtWidgets.QDialog()
            self.ui_conferma = Ui_conferma()

            if colonna == 1 or colonna == 2:
                if (HandlerPrenotazioni.inverno == False):
                    messaggiocopertura = "ll' aperto"
                else:
                    messaggiocopertura = "l chiuso"
            elif colonna == 0:
                messaggiocopertura = "l chiuso"
            elif colonna == 3 or colonna == 4:
                messaggiocopertura = "ll' aperto"

            if colonna == 0 or colonna == 1 or colonna == 3:
                num = 11
            else: num = 15
            self.ui_prenota = Ui_menuprenotazione()
            self.ui_prenota.prenotazione_confermata = False
            self.ui_prenota.setupUI(num, messaggiocopertura, data)
            if self.ui_prenota.prenotazione_confermata:
                HandlerPrenotazioni.inserisciPrenotazione(data, riga, colonna, 0)
            self.visualizzaPrenotazioni()

        else:
            self.window_conferma = QtWidgets.QDialog()
            self.ui_conferma = Ui_conferma()
            self.ui_conferma.setupUi(self.window_conferma,"Prenotazione\nnon disponibile")
            self.window_conferma.show()

    # metodo che chiama un pop up con le statistiche sulle prenotazioni
    def statistichePrenotazioni(self):
        message = self.calcolaStatistiche()
        self.window_conferma = QtWidgets.QDialog()
        self.ui_conferma = Ui_conferma()
        self.ui_conferma.setupUi(self.window_conferma, message)
        self.window_conferma.show()

    # metodo che calcola il mese e l'orario con più prenotazioni
    def calcolaStatistiche(self):
        mesi = {}
        ore = {'08:30': 0, '10:00': 0, '11:30': 0, '13:00': 0, '14:30': 0, '16:00': 0, '17:30': 0, '19:00': 0, '20:30': 0, '22:00': 0}
        if(len(HandlerPrenotazioni.collectionPrenotazioni) != 0):
            for prenotazione in HandlerPrenotazioni.collectionPrenotazioni:
                data_str = prenotazione.data
                anno, mese, giorno = map(int, data_str.split(','))
                data = datetime(anno, mese, giorno)
                # Calcola il mese
                mese = data.month
                if mese in mesi:
                    mesi[mese] += 1
                else:
                    mesi[mese] = 1
                # Calcola l'ora
                ora = prenotazione.oraInizio
                if ora in ore:
                    ore[ora] += 1
                else:
                    ore[ora] = 1

            # Trova il mese con il maggior numero di prenotazioni
            mese_max = max(mesi, key=mesi.get)
            # Trova l'ora con il maggior numero di prenotazioni
            ora_max = max(ore, key=ore.get)

            messaggio = "Mese con più prenotazioni: " + str(
                self.converti_mese(mese_max)) + "\nOra con più prenotazioni:" + str(ora_max)
        else: messaggio = "Non sono state effettuate prenotazioni"
        return messaggio

    # metodo che converte il numero del mese nella stringa di testo col nome del mese corrispondente
    def converti_mese(self, numero):
        mesi = {
            1: "Gennaio",
            2: "Febbraio",
            3: "Marzo",
            4: "Aprile",
            5: "Maggio",
            6: "Giugno",
            7: "Luglio",
            8: "Agosto",
            9: "Settembre",
            10: "Ottobre",
            11: "Novembre",
            12: "Dicembre"
        }
        return mesi.get(numero, "Numero di mese non valido")

    #  metodo che mostra a schermo la tabella delle prenotazioni
    def visualizzaPrenotazioni(self):
        self.tabellaprenotazioni.clearContents()
        #siccome la data ritornata dal calendario è una stringa strana, la pulisco
        data = str(self.calendario.selectedDate())\
            .replace('PyQt5.QtCore.QDate','')\
            .replace('(','')\
            .replace(')','')
        #inizializzo la variabile
        colonna = 0
        for i in range(len(HandlerPrenotazioni.collectionPrenotazioni)):
            if HandlerPrenotazioni.collectionPrenotazioni[i].data == str(data):
                if HandlerPrenotazioni.collectionPrenotazioni[i].campo.tipoCampo == "PVC - Indoor ":
                    colonna = 0
                if HandlerPrenotazioni.collectionPrenotazioni[i].campo.tipoCampo == "Sintetico - Indoor/Outdoor" \
                      and HandlerPrenotazioni.collectionPrenotazioni[i].campo.sport == "Calcio a 5" :
                    colonna = 1
                if HandlerPrenotazioni.collectionPrenotazioni[i].campo.tipoCampo == "Sintetico - Indoor/Outdoor"\
                      and HandlerPrenotazioni.collectionPrenotazioni[i].campo.sport == "Calcio a 7" :
                    colonna = 2
                if HandlerPrenotazioni.collectionPrenotazioni[i].campo.tipoCampo == "Sintetico - Outdoor"\
                      and HandlerPrenotazioni.collectionPrenotazioni[i].campo.sport == "Calcio a 5" :
                    colonna = 3
                if HandlerPrenotazioni.collectionPrenotazioni[i].campo.tipoCampo == "Sintetico - Outdoor"\
                      and HandlerPrenotazioni.collectionPrenotazioni[i].campo.sport == "Calcio a 7" :
                    colonna = 4
                    # ciclo per scrivere velocemente oraInizio, per risparmiare un blocco di if
                for j in range(1, 11):
                    if j%2 != 0:
                        if j == 1 : oraInizio = "08:30"
                        else: oraInizio = str(8+((j-1)*3)//2) + ":30"
                    else: oraInizio = str(10+((j-2)*3)//2) + ":00"

                    if HandlerPrenotazioni.collectionPrenotazioni[i].oraInizio == oraInizio:
                        item = QTableWidgetItem(HandlerPrenotazioni.collectionPrenotazioni[i].utente.nome)
                        self.tabellaprenotazioni.setItem(j-1, colonna, item)

    # metodo che gestisce l'interfaccia completa del menu prenotazioni, con il calendario, la tabella e i pulsanti
    def setupUi(self, prenotazioni):
        prenotazioni.setObjectName("prenotazioni")
        prenotazioni.resize(1500, 450)
        #lista di orari che andranno scritti sulle colonne della tabella
        self.orari = ["8:30-10", "10-11:30", "11:30-13", "13-14:30", "14:30-16",
                    "16-17:30", "17:30-19", "19-20:30", "20:30-22", "22-23:30"]

        self.calendario = QtWidgets.QCalendarWidget(prenotazioni)
        self.calendario.setGeometry(QtCore.QRect(20, 10, 304, 173))
        self.calendario.setMinimumDate(QtCore.QDate(2022, 7, 4))
        self.calendario.setMaximumDate(QtCore.QDate(2050, 12, 31))
        self.calendario.setFirstDayOfWeek(QtCore.Qt.Sunday)
        self.calendario.setGridVisible(True)
        self.calendario.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendario.setNavigationBarVisible(True)
        self.calendario.setObjectName("calendario")

        self.tabellaprenotazioni = QtWidgets.QTableWidget(prenotazioni)
        self.tabellaprenotazioni.setGeometry(QtCore.QRect(335, 10, 1100, 410))
        self.tabellaprenotazioni.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tabellaprenotazioni.setRowCount(10)
        self.tabellaprenotazioni.setColumnCount(5)
        self.tabellaprenotazioni.setObjectName("tabellaprenotazioni")
        self.tabellaprenotazioni.horizontalHeader().setDefaultSectionSize(202.8)
        self.tabellaprenotazioni.verticalHeader().setDefaultSectionSize(20)
        self.tabellaprenotazioni.setHorizontalHeaderLabels(["PVC - Indoor", "Sintetico - Indoor/Outdoor",
                                                            "Sintetico - Indoor/Outdoor", "Sintetico - Outdoor",
                                                            "Sintetico - Outdoor"])

        self.tabellaprenotazioni.setVerticalHeaderLabels(self.orari)
        self.tabellaprenotazioni.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.inserisciprenotazione = QtWidgets.QPushButton(prenotazioni)
        self.inserisciprenotazione.setGeometry(QtCore.QRect(210, 190, 113, 32))
        self.inserisciprenotazione.setObjectName("inserisciprenotazione")

        self.eliminaprenotazione = QtWidgets.QPushButton(prenotazioni)
        self.eliminaprenotazione.setGeometry(QtCore.QRect(210, 260, 113, 32))
        self.eliminaprenotazione.setObjectName("eliminaprenotazione")

        self.gestionepartite = QtWidgets.QPushButton(prenotazioni)
        self.gestionepartite.setGeometry(QtCore.QRect(50, 230, 113, 32))
        self.gestionepartite.setObjectName("modificaprenotazione")

        self.statisticheButton = QtWidgets.QPushButton(prenotazioni)
        self.statisticheButton.setGeometry(QtCore.QRect(50, 300, 113, 32))
        self.statisticheButton.setObjectName("statisticheButton")

        self.statisticheButton.clicked.connect(self.statistichePrenotazioni)

        #refresha la tabella appena si clicca su una data
        self.visualizzaPrenotazioni()

        #azione quando si clicca una data
        self.calendario.clicked.connect(self.visualizzaPrenotazioni)

        #azione quando si clicca inserisci prenotazione
        self.inserisciprenotazione.clicked.connect(self.inserisciPrenotazione)

        #elimina prenotazione
        self.eliminaprenotazione.clicked.connect(self.eliminaPrenotazione)

        #gestione partite
        self.gestionepartite.clicked.connect(self.gestionePartite)

        self.retranslateUi(prenotazioni)
        QtCore.QMetaObject.connectSlotsByName(prenotazioni)

    def retranslateUi(self, prenotazioni):
        _translate = QtCore.QCoreApplication.translate
        prenotazioni.setWindowTitle(_translate("prenotazioni", "Form"))
        self.inserisciprenotazione.setText(_translate("prenotazioni", "Inserisci"))
        self.eliminaprenotazione.setText(_translate("prenotazioni", "Elimina"))
        self.gestionepartite.setText(_translate("prenotazioni", "Partite"))
        self.statisticheButton.setText(_translate("prenotazioni", "Statistiche"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    prenotazioni = QtWidgets.QWidget()
    ui = Ui_prenotazioni()
    ui.setupUi(prenotazioni)
    prenotazioni.show()
    sys.exit(app.exec_())
