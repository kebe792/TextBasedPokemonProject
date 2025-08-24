from PokeBalls import Pokeball, UltraBall, GreatBall, MasterBall

class City:
    def __init__(self, name: str,level_range=(1,5)):
        self.name = name
        self.connections = []
        self.level_range = level_range
                # Shop inventory with costs (default cost = 0 for now)
        self.shop_inventory = {
            "Pokeball": {"class": Pokeball, "cost": 0},
            "GreatBall": {"class": GreatBall, "cost": 0},
            "UltraBall": {"class": UltraBall, "cost": 0},
            "MasterBall": {"class": MasterBall, "cost": 0},
        }

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
    
    def display_shop_items(self):
        return "\n".join(
            f"{i}. {name} - ${data['cost']}"
            for i, (name, data) in enumerate(self.shop_inventory.items(), 1)
        )


    def buy_ball(self, player, ball_name: str, quantity: int = 1):
        if ball_name not in self.shop_inventory:
            return f"{ball_name} is not sold in {self.name}."

        ball_info = self.shop_inventory[ball_name]
        ball_class = ball_info["class"]
        cost = ball_info["cost"]

        # for now, no money system (cost = 0 always)
        for _ in range(quantity):
            player.bag.add_item(ball_class(), 1)

        return f"{player.name} bought {quantity} {ball_name}(s) for {cost * quantity} coins."