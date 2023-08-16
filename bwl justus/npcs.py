import random
import items_bwl_justus


class NPC:

    def __init__(self, name):
        self.name = name
        self.inventory_npc = []


def generate_pool_npcs():
    npc_pool = []
    items_pool = items_bwl_justus.generate_item_pool()
    npc_names_pool = ["Maximilian",
                      "Sophia",
                      "Alexander",
                      "Laura",
                      "Tim",
                      "Anna",
                      "Lukas",
                      "Marie",
                      "Tobias",
                      "Lisa",
                      "Florian",
                      "Julia",
                      "Sebastian",
                      "Sarah",
                      "Christian",
                      "Katharina",
                      "Jan",
                      "Lena",
                      "Fabian",
                      "Leonie",
                      "Philipp",
                      "Jana",
                      "David",
                      "Isabella",
                      "Simon",
                      "Johanna",
                      "Daniel",
                      "Emma",
                      "Benjamin",
                      "Hanna",
                      ]

    for _ in range(30):
        random_npc_name = random.choice(npc_names_pool)
        random_inventory_item = random.choice(items_pool)

        npc = NPC(random_npc_name)
        npc.inventory_npc.append(random_inventory_item)
        npc_pool.append(npc)

    return npc_pool

npc_pool = generate_pool_npcs()

def generate_random_npc():
    random_encounter_value = random.randint(1, 30)
    random_npc = npc_pool[random_encounter_value]
    print(f"""Du bist {random_npc.name} begegnet. 
    Man bietet dir [{random_npc.inventory_npc[0].name}] an, 
    es hat einen möglichen Wert von [{random_npc.inventory_npc[0].price}]""")
    return random_npc

#print(f"name: {npc_pool[10].name} inventaritem: {npc_pool[10].inventory_npc[0].name} und value item: {npc_pool[10].inventory_npc[0].price}")
