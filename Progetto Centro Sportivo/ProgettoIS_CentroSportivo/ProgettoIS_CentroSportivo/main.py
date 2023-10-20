from PyQt5.QtWidgets import QApplication, QWidget
from ProgettoIS_CentroSportivo.Views.home import Ui_Form

if __name__ == "__main__":
    app = QApplication([])
    window = QWidget()
    home = Ui_Form()
    home.setupUi(window)
    window.show()
    app.exec()