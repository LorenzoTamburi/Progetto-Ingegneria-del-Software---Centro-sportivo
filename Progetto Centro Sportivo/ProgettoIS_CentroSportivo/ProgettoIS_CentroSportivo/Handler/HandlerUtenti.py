# Questa classe si occupa della gestione degli utenti del centro sportivo.
# Fornisce metodi per inserire, modificare e controllare le informazioni sugli utenti.
# Inoltre, gestisce il login e il logout degli utenti e la creazione di nuovi tesseramenti

from ProgettoIS_CentroSportivo.Model.Utente import Utente

class HandlerUtenti():

    admin = Utente("Amministratore"," "," "," ","admin","admin")
    admin.isAdmin = True
    utente1 = Utente("Jacopo", "Tarulli", " ", " ", "asd", "asd")
    utente2 = Utente("Lorenzo", "Tamburi", " ", " ", "asd2", "asd2")
    collectionUtenti = []
    collectionUtenti.append(utente1)
    collectionUtenti.append(utente2)
    collectionUtenti.append(admin)
    loginEffettuato = False
    contaUtenti = 3
    contaSoci = 0
    utenteConnesso = None

    # metodo che permette di inserire un nuovo utente all'interno di collectionUtenti
    def inserisciUtente(Utente):
        HandlerUtenti.collectionUtenti.insert(-HandlerUtenti.contaUtenti, Utente)
        HandlerUtenti.contaUtenti += 1

    # metodo che permette di modificare le informazioni di un utente già presente in collectionUtenti
    def modificaUtente(utente,utentemodificato):
        for index, item in enumerate(HandlerUtenti.collectionUtenti):
            if(item == utente):
                if HandlerUtenti.collectionUtenti[index].tesserato:
                    utentemodificato.tesseramento = HandlerUtenti.collectionUtenti[index].tesseramento
                    utentemodificato.tesserato = True
                HandlerUtenti.collectionUtenti[index] = utentemodificato
                if(HandlerUtenti.utenteConnesso.isAdmin == False):
                    HandlerUtenti.utenteConnesso = utentemodificato

    # metodo che permette di impostare la variabile di classe
    # loginEffettuato a True, indicando che l'utente è attualmente connesso
    def setLoginEffettuato(self):
        HandlerUtenti.loginEffettuato = True

    # metodo che permette di impostare la variabile di classe utenteConnesso
    # con l'utente specificato, indicando che l'utente è attualmente connesso
    def setUtenteConnesso(utente):
        HandlerUtenti.utenteConnesso = utente

    # metodo che permette di impostare la variabile di classe loginEffettuato e
    # utenteConnesso a False e None rispettivamente, indicando che l'utente ha effettuato il logout
    def setLogoutEffettuato(self):
        HandlerUtenti.loginEffettuato = False
        HandlerUtenti.utenteConnesso = None

    # metodo che permette di creare un nuovo tesseramento
    # per l'utente connesso e di contare il numero di soci del centro sportivo
    def creaTesseramento(email, codiceFiscale):
        HandlerUtenti.contaSoci = 0
        HandlerUtenti.utenteConnesso.setTesseramento(email, codiceFiscale)
        for x in HandlerUtenti.collectionUtenti:
            if x.getTesseramento():
                HandlerUtenti.contaSoci += 1