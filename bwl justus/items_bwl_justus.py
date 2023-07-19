import random


class Item:

    def __init__(self, name, price):
        self.name = name
        self.price = price


def generate_item_pool():
    items_pool = []

    item_names_pool = ["Alte Matheklausuren-Sammlung",
                       "Wirtschaftslexikon aus den 90ern",
                       "Premium Energy-Drink Vorratspackung",
                       "Starbucks Jahresabo",
                       "Vintage Taschenrechner",
                       "Gebrauchtes Polohemd",
                       "Signiertes Steve Jobs Poster",
                       "BWL für Dummies Buch",
                       "Stapel alter WiWi-Fachzeitschriften",
                       "Abgelaufene Mensa-Gutscheine",
                       "Stressball in Euro-Form",
                       "Limitierte Edition 'The Wolf of Wall Street' DVD",
                       "Justus' abgelegte Seminarunterlagen",
                       "Exklusives Start-Up T-Shirt",
                       "Flasche feinsten Club Mate",
                       "Originales Konferenz Namensschild",
                       "Gebrauchte Powerbank",
                       "Verschollene Aktienanteile",
                       "Überlebenspack für Prüfungsphase",
                       "Handsigniertes Warren Buffet Bild",
                       "Edle Aktentasche mit Kaffeeflecken",
                       "Überlebensgroßes Bitcoin-Poster",
                       "Abgekaute Bleistifte",
                       "Laptop mit leerem Akku",
                       "Überteuerte Lernhilfen",
                       "Kryptowährungs Starter-Kit",
                       "Coffee-to-Go Becher Pyramide",
                       "Zerknitterter Business-Plan",
                       "Erfolgsgarantierender Glücksbringer",
                       "Wirtschaftsweiser Kaffeebecher"]

    for _ in range(30):
        random_item_name = random.choice(item_names_pool)
        random_item_price = random.randint(1, 100) * 10
        item = Item(random_item_name, random_item_price)
        items_pool.append(item)

    return items_pool


