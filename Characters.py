class Character:
    def __init__(self):
        self.Team = []  # list of Pokemon objects, max 6

    def add_to_team(self, pokemon):
        if len(self.Team) >= 6:
            raise ValueError("Team is full (max 6 Pokémon).")
        self.Team.append(pokemon)