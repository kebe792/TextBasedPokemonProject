from Characters import Character
from Pokemon import Pokemon
from Bag import Bag
import json
from City import City

class Player(Character):
    def __init__(self, Name: str, start_city: City):
        super().__init__() 
        self.Name = Name
        self.Bag = Bag()
        self.current_city = start_city

    def show_team(self):
        for poke in self.Team:
            print(poke)

    def check_level_up(self):
            for i, poke in enumerate(self.Team):
                if poke is None:
                    continue  # skip empty slots
                while poke.xp >= poke.Growth:
                    # Level up
                    poke = Pokemon.GetLeveled(poke_id=poke.id, level=poke.level + 1)
                    # Subtract XP used to level up
                    poke.xp -= poke.Growth
                # Update the team slot with the leveled Pokémon
                self.Team[i] = poke

    def save(self, filename="player.json"):
        # Load existing data
        try:
            with open(filename, "r") as f:
                all_players = json.load(f)
        except FileNotFoundError:
            all_players = {}  # no file yet, start fresh

        # Update or add this player
        all_players[self.Name] = {
            "Bag": self.Bag.save(),
            "Team": [poke.save() if poke else None for poke in self.Team],
            "Location": self.current_city.name if self.current_city else None
        }

        # Write back the full JSON
        with open(filename, "w") as f:
            json.dump(all_players, f, indent=4)
        
        print(f"Player '{self.Name}' saved to {filename}")

    @classmethod
    def load(cls, world, filename="player.json", name=None):
        import json
        
        with open(filename, "r") as f:
            all_players = json.load(f)

        if name is None or name not in all_players:
            raise ValueError(f"Player '{name}' not found in {filename}")

        player_data = all_players[name]

        # Create player without assigning city yet
        player = cls(name, start_city=None)
        player.Bag = Bag.load(player_data["Bag"])
        player.Team = [Pokemon.load(p) if p else None for p in player_data.get("Team", [])]

        # Restore location
        loc_name = player_data.get("Location")
        if loc_name:
            player.current_city = world.get_city(loc_name)

        print(f"Player '{name}' loaded at {player.current_city.name}")
        return player
    
    def move_to(self, city: City):
        if city in self.current_city.connections:
            self.current_city = city
            print(f"{self.Name} moved to {city.name}")
        else:
            print(f"You can’t move directly to {city.name} from {self.current_city.name}")

    def try_catch(self, pokemon, ball_name):
        import random

        bag_ball = self.Bag.contents.get(ball_name)
        if not bag_ball or bag_ball["quantity"] <= 0:
            print(f"You don't have any {ball_name}s!")
            return False

        # Consume one ball
        bag_ball["quantity"] -= 1

        # Simple catch formula
        # pokemon.Catch_Rate can be > 100
        # ball.catch_rate is 0-1
        if bag_ball["item"].name == "Master Ball":
            chance = 1.00
        else:
            chance = min(1.0, (pokemon.Catch_Rate / 255) * bag_ball["item"].catch_rate)

        if random.random() <= chance:
            print(f"Congratulations! You caught {pokemon.name}!")
            self.Team.append(pokemon)
            return True
        else:
            print(f"Oh no! {pokemon.name} broke free!")
            return False