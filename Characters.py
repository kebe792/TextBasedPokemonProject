# import pandas as pd

# class Character:
#     def __init__(self):

#         # Explicitly set up team DataFrame with 6 slots
#         self.Team = pd.DataFrame({
#             "Pokemon": ["" for _ in range(6)],
#             "ID": [0 for _ in range(6)],
#             "Level": [0 for _ in range(6)],
#             "Max HP": [0 for _ in range(6)],
#             "Current HP": [0 for _ in range(6)],
#             "XP": [0 for _ in range(6)],
#             "Attack": [0 for _ in range(6)],
#             "Defense": [0 for _ in range(6)],
#             "Speed": [0 for _ in range(6)],
#             "Special": [0 for _ in range(6)],
#             "Zone": ["" for _ in range(6)],
#             "Total": [0 for _ in range(6)],
#             "Average": [0.0 for _ in range(6)]
#         })

#     def add_to_team(self, pokemon, level=1, CurrentHP=0, CurrentXP=0, slot=None):
#         if slot is None:  
#             # Find first empty slot
#             empty_slots = self.Team[self.Team["ID"] == 0].index
#             if len(empty_slots) == 0:
#                 raise ValueError("Team is full (max 6 Pokémon).")
#             slot = empty_slots[0]

#         # Insert Pokémon data into the given slot
#         self.Team.loc[slot] = {
#             "Pokemon": pokemon.name,
#             "ID": pokemon.id,
#             "Level": level,
#             "Max HP": pokemon.hp,
#             "Current HP": CurrentHP,
#             "XP": CurrentXP,
#             "Attack": pokemon.attack,
#             "Defense": pokemon.defense,
#             "Speed": pokemon.speed,
#             "Special": pokemon.special,
#             "Zone": pokemon.zone,
#             "Total": pokemon.total,
#             "Average": pokemon.average
#         }

#         print(f"{pokemon.name} added to the team in slot {slot+1}!")


class Character:
    def __init__(self):
        self.Team = []  # list of Pokemon objects, max 6

    def add_to_team(self, pokemon):
        if len(self.Team) >= 6:
            raise ValueError("Team is full (max 6 Pokémon).")
        self.Team.append(pokemon)