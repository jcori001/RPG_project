class Item:
    def __init__(self, name, typ, desc, prop):
        self.name = name
        self.type = typ
        self.description = desc
        self.properties = prop


# Create Items
potion = Item("Potion", "potion", "Heal 200 HP", 200)
hipotion = Item("Hi-Potion", "potion", "Heals 500 HP", 500)

elixir = Item("Elixir", "elixir", "Fully restores HP/HP of one party member", 9999)
megaelixir = Item("Megaelixir", "elixir", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 200 damage to one enemy", 200)
h_bomb = Item("H-Bomb", "attack", "Deals 500 damage to one enemy", 500)
