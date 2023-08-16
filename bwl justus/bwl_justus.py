import random
import items_bwl_justus
import npcs

class Player:

    def __init__(self, money):
        self.money = money
        self.inventory_player = []
        self.pool_weekday = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
        self.current_day_index = -1
        self.buy_limit_today = 0

    def buy_item(self, npc):
        print(f"Du hast {npc.inventory_npc[0].name}")

    def sell_inventory(self):
        print("Inventory has been sold")

    def encounter_npc(self):
        random_npc = npcs.generate_random_npc()
        buy_item = input("Möchtest du diesen Gegenstand kaufen? [Ja oder Nein]")
        if buy_item.lower() == "ja":
            new_player.inventory_player.append(random_npc.inventory_npc[0].name)
            print(new_player.inventory_player[0])


    def get_status(self):
        return f"Du hast aktuell folgende Items im Inventar: {self.inventory_player} und {self.money} EUR in der Tasche"

    def check_weekday(self):
        print(f"Heute ist {self.pool_weekday[self.current_day_index]}")

    def proceed_next_day(self):
        profit = 0
        item_count = 0
        for item in self.inventory_player:
            profit +=
            item_count += 1

        print(f"""
            Du hast folgende Items im Inventar gehabt: {self.inventory_player}, es landet alles bei Ebay Kleinanzeigen
            Für die {item_count} Gegenstände bekommst du {profit} EUR!
            """)

        self.current_day_index = (self.current_day_index + 1) % 7

        print(f"Heute ist {self.pool_weekday[self.current_day_index]}")


new_player = Player(1000)
npc_pool = npcs.npc_pool

new_player.encounter_npc()


# kommentar zum git testen
# mehr kommentare zum testen
