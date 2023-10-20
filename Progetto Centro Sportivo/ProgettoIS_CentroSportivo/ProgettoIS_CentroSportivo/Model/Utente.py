# La classe "Utente" rappresenta un utente del centro sportivo con le sue credenziali
# e generalità, e la possibilità di essere tesserati

from ProgettoIS_CentroSportivo.Model.Tesseramento import Tesseramento

class Utente:
    contatore = 1
    def __init__(self, nome, cognome, dataNascita, cellulare, password, nomeUtente):
        self.nomeUtente = nomeUtente
        self.password = password
        self.nome = nome
        self.cognome = cognome
        self.dataNascita = dataNascita
        Utente.contatore += 1
        self.ID = Utente.contatore
        self.cellulare = cellulare
        self.tesserato = False
        self.isAdmin = False

    # permette di impostare un oggetto della classe "Tesseramento" per l'utente,
    # utilizzando l'email e il codice fiscale forniti come parametri
    def setTesseramento(self, email, codiceFiscale):
        self.tesseramento = Tesseramento(email, codiceFiscale)
        self.tesserato = True

    # restituisce un valore booleano che indica se l'utente è tesserato o meno,
    # controllando il valore della variabile di istanza "tesserato"
    def getTesseramento(self):
        if self.tesserato:
            return True
        else:
            return False