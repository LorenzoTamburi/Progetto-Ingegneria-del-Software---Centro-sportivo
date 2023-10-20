#Classe che crea un oggetto di tipo Campo con 3 parametri:
# -indoor: variabile booleana che indica se il campo è al chiuso o all'aperto
# -tipoCampo: indica il tipo di terreno di gioco, sintetico o in PVC
# -sport: indica lo sport destinato a quel campo sportivo, se Calcio a 5 o a 7

class Campo:
    def __init__(self, copertura, tipoCampo, sport):
        self.copertura = copertura
        self.tipoCampo = tipoCampo
        self.sport = sport