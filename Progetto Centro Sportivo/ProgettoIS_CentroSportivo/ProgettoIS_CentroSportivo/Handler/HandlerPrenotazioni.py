# La classe "HandlerPrenotazioni" gestisce le prenotazioni dei campi da calcio a 5 e a 7
# all'interno di un centro sportivo. Dispone di metodi per inserire, eliminare
# e cercare prenotazioni all'interno di collectionPrenotazioni utilizzando oggetti
# della classe "Campo" e della classe "Utente"


from ProgettoIS_CentroSportivo.Model.Campo import Campo
import datetime
from ProgettoIS_CentroSportivo.Model.Prenotazione import Prenotazione
from ProgettoIS_CentroSportivo.Model.Utente import Utente
from ProgettoIS_CentroSportivo.Handler.HandlerUtenti import HandlerUtenti

class HandlerPrenotazioni():
    giorno = datetime.date.today().timetuple().tm_yday
    inverno = range(80, 264)
    if giorno in inverno:
        riscaldamento = False
    else:
        riscaldamento = True
    # campo indoor
    campo5_1 = Campo(True, "PVC - Indoor", "Calcio a 5")
    # campi con copertura variabile a seconda della stagione
    campo5_2 = Campo(riscaldamento, "Sintetico - Indoor/Outdoor", "Calcio a 5")
    campo7_1 = Campo(riscaldamento, "Sintetico - Indoor/Outdoor", "Calcio a 7")
    # campo all'aperto
    campo5_3 = Campo(False, "Sintetico - Outdoor", "Calcio a 5")
    campo7_2 = Campo(False, "Sintetico - Outdoor", "Calcio a 7")

    utente = Utente("Jacopo", " ", " ", " ", " ", " ")
    collectionPrenotazioni = []

    #inserisce una nuova prenotazione in collectionPrenotazioni
    def inserisciPrenotazione(data, riga, colonna, idUtente):

        if (riga == 0): orario = "08:30"
        if (riga == 1): orario = "10:00"
        if (riga == 2): orario = "11:30"
        if (riga == 3): orario = "13:00"
        if (riga == 4): orario = "14:30"
        if (riga == 5): orario = "16:00"
        if (riga == 6): orario = "17:30"
        if (riga == 7): orario = "19:00"
        if (riga == 8): orario = "20:30"
        if (riga == 9): orario = "22:00"

        if (colonna == 0): campo = HandlerPrenotazioni.campo5_1
        if (colonna == 1): campo = HandlerPrenotazioni.campo5_2
        if (colonna == 2): campo = HandlerPrenotazioni.campo7_1
        if (colonna == 3): campo = HandlerPrenotazioni.campo5_3
        if (colonna == 4): campo = HandlerPrenotazioni.campo7_2

        if(HandlerUtenti.utenteConnesso.isAdmin == False):
            prenotazione = Prenotazione(data, orario, campo, HandlerUtenti.utenteConnesso)
        else: prenotazione = Prenotazione(data, orario, campo, HandlerUtenti.collectionUtenti[idUtente])
        HandlerPrenotazioni.collectionPrenotazioni.append(prenotazione)

    #elimina una prenotazione in collectionPrenotazioni
    def eliminaPrenotazione(data, riga, colonna):
        prenotazione = HandlerPrenotazioni.cercaPrenotazione(data, riga, colonna)
        if(prenotazione != None):
            HandlerPrenotazioni.collectionPrenotazioni.remove(prenotazione)
            return True
        else:
            return False

    # cerca una prenotazione nella collectionPrenotazioni corrispondente alla data, riga e colonna specificate
    # Restituisce la prenotazione trovata o None se non esiste una corrispondenza
    def cercaPrenotazione(data, riga, colonna):

        if (riga == 0): orario = "08:30"
        if (riga == 1): orario = "10:00"
        if (riga == 2): orario = "11:30"
        if (riga == 3): orario = "13:00"
        if (riga == 4): orario = "14:30"
        if (riga == 5): orario = "16:00"
        if (riga == 6): orario = "17:30"
        if (riga == 7): orario = "19:00"
        if (riga == 8): orario = "20:30"
        if (riga == 9): orario = "22:00"

        if (colonna == 0): campo = HandlerPrenotazioni.campo5_1
        if (colonna == 1): campo = HandlerPrenotazioni.campo5_2
        if (colonna == 2): campo = HandlerPrenotazioni.campo7_1
        if (colonna == 3): campo = HandlerPrenotazioni.campo5_3
        if (colonna == 4): campo = HandlerPrenotazioni.campo7_2

        for x in HandlerPrenotazioni.collectionPrenotazioni:
            if(x.data == data
                    and x.oraInizio == orario
                    and str(x.campo.tipoCampo) == campo.tipoCampo
                    and (str(x.utente.nome) == HandlerUtenti.utenteConnesso.nome
                         or HandlerUtenti.utenteConnesso.isAdmin == True)
            ):
                return x
            else:
                pass