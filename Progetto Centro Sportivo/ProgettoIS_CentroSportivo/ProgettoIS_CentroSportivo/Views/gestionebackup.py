# classe che rappresenta l'interfaccia grafica per la gestione del backup dei dati dell'applicazione
# e permette di salvare e caricare i dati da un file di backup

from PyQt5 import QtCore, QtWidgets
from ProgettoIS_CentroSportivo.Handler.HandlerBackup import HandlerBackup

class Ui_gestionebackup(object):

    # metodo che utilizza la classe "HandlerBackup" per eseguire l'operazione di salvataggio
    # dei dati dell'applicazione in un file di backup
    def saveBackup(self):
        HandlerBackup.salvaDati(self)

    # metodo che utilizza la classe "HandlerBackup" per eseguire l'operazione di caricamento
    # dei dati dell'applicazione in un file di backup
    def loadBackup(self):
        HandlerBackup.caricaDati(self)

    def setupUi(self, gestionebackup):
        gestionebackup.setObjectName("gestionebackup")
        gestionebackup.resize(400, 146)

        self.buttonBox = QtWidgets.QDialogButtonBox(gestionebackup)
        self.buttonBox.setGeometry(QtCore.QRect(290, 20, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName("buttonBox")

        self.save = QtWidgets.QPushButton(gestionebackup)
        self.save.setGeometry(QtCore.QRect(20, 30, 113, 32))
        self.save.setObjectName("save")

        self.load = QtWidgets.QPushButton(gestionebackup)
        self.load.setGeometry(QtCore.QRect(20, 80, 113, 32))
        self.load.setObjectName("load")

        self.retranslateUi(gestionebackup)
        self.buttonBox.rejected.connect(gestionebackup.reject)
        self.save.clicked.connect(self.saveBackup)
        self.load.clicked.connect(self.loadBackup)
        QtCore.QMetaObject.connectSlotsByName(gestionebackup)

    def retranslateUi(self, gestionebackup):
        _translate = QtCore.QCoreApplication.translate
        gestionebackup.setWindowTitle(_translate("gestionebackup", "Dialog"))
        self.save.setText(_translate("gestionebackup", "Salva backup"))
        self.load.setText(_translate("gestionebackup", "Carica backup"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gestionebackup = QtWidgets.QDialog()
    ui = Ui_gestionebackup()
    ui.setupUi(gestionebackup)
    gestionebackup.show()
    sys.exit(app.exec_())
