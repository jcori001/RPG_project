class Item:
    def __init__(self, name, typ, desc, prop):
        self.name = name
        self.type = typ
        self.description = desc
        self.properties = prop


# Create Items
potion = Item("Potion", "potion", "Heal 250 HP", 250)
hipotion = Item("Hi-Potion", "potion", "Heals 600 HP", 600)

elixir = Item("Elixir", "elixir", "Fully restores HP/HP of one party member", 9999)
megaelixir = Item("Megaelixir", "elixir", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 300 damage to one enemy", 300)
big_one = Item("Big One", "attack", "Deals 600 damage to one enemy", 600)
