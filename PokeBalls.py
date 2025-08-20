from Item import Item

class Pokeball(Item):
    def __init__(self, name="Pokeball", catch_rate=1):
        super().__init__(name, description=f"A {name} used to catch Pokémon")
        self.catch_rate = catch_rate

class GreatBall(Pokeball):
    def __init__(self):
        super().__init__(name="Great Ball", catch_rate=1.5)

class UltraBall(Pokeball):
    def __init__(self):
        super().__init__(name="Ultra Ball", catch_rate=2)

class MasterBall(Pokeball):
    def __init__(self):
        super().__init__(name="Master Ball", catch_rate=1.0)
