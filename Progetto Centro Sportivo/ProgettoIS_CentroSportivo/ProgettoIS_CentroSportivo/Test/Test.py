import unittest

from ProgettoIS_CentroSportivo.Model.Utente import Utente
from ProgettoIS_CentroSportivo.Handler.HandlerUtenti import HandlerUtenti
from ProgettoIS_CentroSportivo.Handler.HandlerPrenotazioni import HandlerPrenotazioni
from ProgettoIS_CentroSportivo.Model.Prenotazione import Prenotazione


class MyTestCase(unittest.TestCase):

    def testLogin(self):
        # Controlla che gli utenti appena creati non sono amministratori di default.
        self.utente = Utente("Ivan", "prova", "08/06/1991", "333222556", "password", "asd")
        HandlerUtenti.setUtenteConnesso(self.utente)
        self.assertEqual(HandlerUtenti.utenteConnesso.isAdmin, False)

    def testPrenotazione(self):
        #Controlla che una prenotazione viene trovata con il metodo cercaPrenotazione
        #da un utente connesso non amministratore
        self.campo = HandlerPrenotazioni.campo5_1
        self.utente = Utente("Ivan", "prova", "08/06/1991", "333222556", "password", "asd")
        self.prenotazioneuno = Prenotazione("2023,5,5","10:00", self.campo, self.utente)
        HandlerPrenotazioni.collectionPrenotazioni.append(self.prenotazioneuno)
        HandlerUtenti.utenteConnesso = self.utente
        self.assertEqual(HandlerPrenotazioni.cercaPrenotazione("2023,5,5", 1, 0), self.prenotazioneuno)

    def testCopiaTesseramento(self):
        #Controlla che alla modifica di un utente venga portato il tesseramento
        self.utente = Utente("Ivan", "prova", "08/06/1991", "333222556", "password", "asd")
        self.utente.setTesseramento("prova@google.com", "PCNVNI91H08I608S", "Calcio a 5")
        HandlerUtenti.collectionUtenti.append(self.utente)
        HandlerUtenti.utenteConnesso=self.utente
        self.utentemodificato=Utente("Mario", "Franchi", "08/06/1991", "333222556", "password", "asd")
        HandlerUtenti.modificaUtente(self.utente, self.utentemodificato)
        self.assertEqual(self.utente.getTesseramento(), self.utentemodificato.getTesseramento())


if __name__ == '__main__':
    unittest.main()
