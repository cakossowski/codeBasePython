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


class Elektroauto(Auto):

    def __init__(self, marke, modell, baujahr, farbe, batteriestatus, reichweite):
        super().__init__(marke, modell, baujahr, farbe)
        self.batteriestatus = batteriestatus
        self.reichweite = reichweite

    def fahren(self, strecke):
        self.reichweite -= strecke
        return self.reichweite

