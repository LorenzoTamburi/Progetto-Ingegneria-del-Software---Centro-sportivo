# Questa classe è progettata per gestire il backup dei dati dell'applicazione
# Fornisce un modo per salvare e caricare i dati dell'applicazione
# in modo da poter essere utilizzati in caso di perdita di dati o di problemi tecnici


import pickle
from ProgettoIS_CentroSportivo.Handler.HandlerUtenti import HandlerUtenti
from ProgettoIS_CentroSportivo.Handler.HandlerPrenotazioni import HandlerPrenotazioni

class HandlerBackup():
    # questo metodo salva i dati delle prenotazioni e degli utenti
    # utilizzando la funzione "pickle.dump" per scrivere i dati in un file binario
    def salvaDati(self):
        pickle.dump(HandlerPrenotazioni.collectionPrenotazioni,open( "backupPrenotazioni.p", "wb" ))
        pickle.dump(HandlerUtenti.collectionUtenti, open( "backupUtenti.p", "wb" ))
        print("fatto")

    # questo metodo carica i dati delle prenotazioni e degli utenti salvati nei file binari
    # creati dal metodo "salvaDati". In particolare, il metodo utilizza la funzione
    # "pickle.load" per caricare i dati dal file binario "backupPrenotazioni.p" e "backupUtenti.p"
    def caricaDati(self):
            HandlerPrenotazioni.collectionPrenotazioni = pickle.load(open( "backupPrenotazioni.p", "rb" ))
            HandlerUtenti.collectionUtenti = pickle.load(open( "backupUtenti.p", "rb" ))

