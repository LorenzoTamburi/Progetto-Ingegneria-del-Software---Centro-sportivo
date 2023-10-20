# Questa classe gestisce l'interfaccia grafica per la gestione degli utenti del centro sportivo, in
# particolare della visualizzazione delle liste di utenti iscritti e tesserati

from PyQt5 import QtCore, QtWidgets
from ProgettoIS_CentroSportivo.Views.visualizzazione_liste import Ui_visualizzazioneliste

class Ui_gestioneOrganizzazione(object):

    # metodo che chiama la classe visualizzazione_liste per visualizzare la tabella degli iscritti
    def visualizzaListaUtenti(self):
        self.visualizzasoci = False
        self.windows_visualizza = QtWidgets.QDialog()
        self.ui_visualizza = Ui_visualizzazioneliste()
        self.ui_visualizza.setupUi(self.windows_visualizza, self.visualizzasoci)
        self.windows_visualizza.show()


    # metodo che chiama la classe visualizzazione_liste per visualizzare la tabella dei tesserati
    def visualizzaListaSoci(self):
        self.visualizzasoci = True
        self.windows_visualizza = QtWidgets.QDialog()
        self.ui_visualizza = Ui_visualizzazioneliste()
        self.ui_visualizza.setupUi(self.windows_visualizza, self.visualizzasoci)
        self.windows_visualizza.show()

    def setupUi(self, gestioneOrganizzazione):
        gestioneOrganizzazione.setObjectName("gestioneOrganizzazione")

        gestioneOrganizzazione.resize(400, 300)
        self.listautenti = QtWidgets.QPushButton(gestioneOrganizzazione)
        self.listautenti.setGeometry(QtCore.QRect(110, 30, 171, 32))
        self.listautenti.setObjectName("pushButton")

        self.listasoci = QtWidgets.QPushButton(gestioneOrganizzazione)
        self.listasoci.setGeometry(QtCore.QRect(110, 60, 171, 32))
        self.listasoci.setObjectName("pushButton_2")

        self.listautenti.clicked.connect(self.visualizzaListaUtenti)
        self.listasoci.clicked.connect(self.visualizzaListaSoci)

        self.retranslateUi(gestioneOrganizzazione)
        QtCore.QMetaObject.connectSlotsByName(gestioneOrganizzazione)

    def retranslateUi(self, gestioneOrganizzazione):
        _translate = QtCore.QCoreApplication.translate
        gestioneOrganizzazione.setWindowTitle(_translate("gestioneOrganizzazione", "Form"))
        self.listautenti.setText(_translate("gestioneOrganizzazione", "Visualizza Lista Utenti"))
        self.listasoci.setText(_translate("gestioneOrganizzazione", "Visualizza Lista Soci"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gestioneOrganizzazione = QtWidgets.QWidget()
    ui = Ui_gestioneOrganizzazione()
    ui.setupUi(gestioneOrganizzazione)
    gestioneOrganizzazione.show()
    sys.exit(app.exec_())
