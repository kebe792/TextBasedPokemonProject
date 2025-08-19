from Characters import Character
from Pokemon import Pokemon
from Bag import Bag
import json

class Player(Character):
    def __init__(self, Name: str):
        super().__init__() 
        self.Name = Name
        self.Bag = Bag()

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
            "Team": [poke.save() if poke else None for poke in self.Team]
        }

        # Write back the full JSON
        with open(filename, "w") as f:
            json.dump(all_players, f, indent=4)
        
        print(f"Player '{self.Name}' saved to {filename}")

    @classmethod
    def load(cls, filename="player.json", name=None):
        with open(filename, "r") as f:
            all_players = json.load(f)
        
        if name is None or name not in all_players:
            raise ValueError(f"Player '{name}' not found in {filename}")
        
        player_data = all_players[name]
        player = cls(name)
        player.Bag = Bag.load(player_data["Bag"])
        player.Team = [Pokemon.load(p) if p else None for p in player_data.get("Team", [])]
        
        print(f"Player '{name}' loaded from {filename}")
        return player