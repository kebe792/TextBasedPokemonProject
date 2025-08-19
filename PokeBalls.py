from Item import Item

class Pokeball(Item):
    def __init__(self, name="Pokeball", catch_rate=0.4):
        super().__init__(name, description=f"A {name} used to catch Pokémon")
        self.catch_rate = catch_rate

class GreatBall(Pokeball):
    def __init__(self):
        super().__init__(name="Great Ball", catch_rate=0.6)

class UltraBall(Pokeball):
    def __init__(self):
        super().__init__(name="Ultra Ball", catch_rate=0.8)

class MasterBall(Pokeball):
    def __init__(self):
        super().__init__(name="Master Ball", catch_rate=1.0)
