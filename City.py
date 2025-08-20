class City:
    def __init__(self, name: str,level_range=(1,5)):
        self.name = name
        self.connections = []
        self.level_range = level_range

    def connect(self, other_city):
        if other_city not in self.connections:
            self.connections.append(other_city)
            other_city.connections.append(self)

    def __repr__(self):
        return f"City({self.name})"
    
    def find_pokemon(self):
            import pandas as pd
            import random
            from Pokemon import Pokemon

            df = pd.read_csv("KantoPokemon.csv")
            zone_pokemon = df[df["City"].str.lower() == self.name.lower()]

            if zone_pokemon.empty:
                print(f"No Pokémon found in {self.name}.")
                return None

            row = zone_pokemon.sample(n=1).iloc[0]

            min_lvl, max_lvl = self.level_range
            poke_level = random.randint(min_lvl, max_lvl)

            poke = Pokemon.GetLeveled(row["ID"], level=poke_level)
            print(f"A wild {poke.name} (Lvl {poke.level}) appeared in {self.name}!")
            return poke