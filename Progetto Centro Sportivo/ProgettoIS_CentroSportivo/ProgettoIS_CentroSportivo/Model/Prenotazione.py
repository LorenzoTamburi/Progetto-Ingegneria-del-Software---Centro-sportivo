# La classe "Prenotazione" rappresenta una prenotazione di un campo sportivo all'interno di un centro sportivo.
# La classe utilizza oggetti della classe "Partita" per rappresentare le partite giocate sul campo prenotato
# e oggetti della classe "Campo" per rappresentare il campo sportivo prenotato.

class Prenotazione:

   def __init__(self, data, oraInizio, campo, utente):
        self.data = data
        self.oraInizio = oraInizio
        self.campo = campo
        self.utente = utente
        self.collectionPartite = []

   # metodo che permette di aggiungere una partita al collectionPartite della prenotazione
   def aggiungiPartita(self, partita):
        self.collectionPartite.append(partita)

   # metodo che permette di modificare una partita già presente in collectionPartite della prenotazione
   def modificaPartita(self, rigapartita, partitamodificata):
        self.collectionPartite[rigapartita] = partitamodificata

   # metodo che restituisce le statistiche delle partite relative alla prenotazione,
   # calcolando la percentuale di vittorie in base ai punteggi delle partite presenti in collectionPartite
   def getStatistiche(self):
        vittorie = 0
        for partita in self.collectionPartite:
            if(partita.punteggio1 > partita.punteggio2): vittorie += 1
        if(vittorie==0):percentuale=0
        else:percentuale=vittorie/len(self.collectionPartite)*100
        #toglie i decimali inutili
        return "{:.2f}".format(percentuale)+" %"

