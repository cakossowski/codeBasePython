class Auto:

    def __init__(self, marke, modell, baujahr, farbe):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr
        self.farbe = farbe

    def change_farbe(self, neue_farbe):
        self.farbe = neue_farbe

    def change_modell(self, neues_modell):
        self.modell = neues_modell

    def change_marke(self, neue_marke):
        self.marke = neue_marke

    def informationsauszug(self):
        return f'Marke: {self.marke}, Modell: {self.modell}, Baujahr {self.baujahr}, Farbe {self.farbe}'


erstes_Auto = Auto("audi", "a4", "1990", "grün")
erstes_Auto.informationsauszug()

erstes_Auto.change_farbe('blau')
erstes_Auto.change_marke('bmw')
erstes_Auto.change_modell('M5')

print(erstes_Auto.informationsauszug())

