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
        random_encounter_value = random.randint(1, 30)
        random_npc = npc_pool[random_encounter_value]
        print(f"""Du bist {random_npc.name} begegnet. 
        Man bietet dir [{random_npc.inventory_npc[0].name}] an, 
        es hat einen möglichen Wert von [{random_npc.inventory_npc[0].price}]""")
        buy_item = input("Möchtest du diesen Gegenstand kaufen? [Ja oder Nein]")
        if buy_item.lower() == "ja":
            new_player.buy_item(random_npc)

    def get_status(self):
        return f"Du hast aktuell folgende Items im Inventar: {self.inventory_player} und {self.money} EUR in der Tasche"

    def check_weekday(self):
        print(f"Heute ist {self.pool_weekday[self.current_day_index]}")

    def proceed_next_day(self):
        profit = 0
        item_count = 0
        for item in self.inventory_player:
            profit += 100
            item_count += 1

        print(f"""
            Du hast folgende Items im Inventar gehabt: {self.inventory_player}, es landet alles bei Ebay Kleinanzeigen
            Für die {item_count} Gegenstände bekommst du {profit} EUR!
            """)

        self.current_day_index = (self.current_day_index + 1) % 7

        print(f"Heute ist {self.pool_weekday[self.current_day_index]}")


new_player = Player(1000)
npc_pool = npcs.generate_pool_npcs()

new_player.encounter_npc()