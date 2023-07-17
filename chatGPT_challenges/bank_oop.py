class Bankkonto:

    def __init__(self, inhaber, nummer, guthaben: float):
        self.inhaber = inhaber
        self.nummer = nummer
        self.guthaben = guthaben

    def einzahlen(self, einzahlung: float):
        self.guthaben += einzahlung
        return self.guthaben

    def abheben(self, abhebung: float):
        if self.guthaben >= abhebung:
            self.guthaben -= abhebung
            return self.guthaben
        else:
            print("Nicht genug Guthaben!")

    def anzeigen_kontostand(self):
        return f'Der aktuelle Kontostand für {self.inhaber}//{self.nummer} beträgt aktuell {self.guthaben}'


neues_Bankkonto = Bankkonto('Horst', '12345', 0)

neues_Bankkonto.einzahlen(105.12)
neues_Bankkonto.einzahlen(1000.88)

print(neues_Bankkonto.anzeigen_kontostand())

neues_Bankkonto.abheben(140)
neues_Bankkonto.abheben(500.85)

print(neues_Bankkonto.anzeigen_kontostand())
