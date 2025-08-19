import pandas as pd

class Pokemon:
    def __init__(self, poke_id, csv_file="KantoPokemon.csv"):
        # Read the CSV
        df = pd.read_csv(csv_file)

        # Find the row with the given ID
        row = df[df["ID"] == poke_id]

        if row.empty:
            raise ValueError(f"Pokémon with ID {poke_id} not found in CSV.")

        row = row.iloc[0]  # single row as Series

        self.id = row["ID"]
        self.name = row["Pokémon"]
        self.zone = row["Zone"]
        self.base_hp = row["HP"]
        self.base_attack = row["Attack"]
        self.base_defense = row["Defense"]
        self.base_speed = row["Speed"]
        self.base_special = row["Special"]
        self.total = row["Total"]
        self.average = row["Average"]
        self.Base_Growth = row["Growth"]

        # Default level = 1
        self.level = 1
        self.calc_stats(self.level)

    def calc_stats(self, level):
        """Calculate stats at a given level and store in the object."""
        self.level = level
        self.hp = self.calc_hp(self.base_hp, level)
        self.attack = self.calc_other(self.base_attack, level)
        self.defense = self.calc_other(self.base_defense, level)
        self.speed = self.calc_other(self.base_speed, level)
        self.special = self.calc_other(self.base_special, level)
        self.xp = 0
        self.Growth = self.xp_to_level(level, self.Base_Growth)

    @classmethod
    def GetLeveled(cls, poke_id, level, csv_file="KantoPokemon.csv"):
        """Return a new Pokémon object at the specified level."""
        poke = cls(poke_id, csv_file=csv_file)
        poke.calc_stats(level)
        return poke

    @staticmethod
    def calc_hp(base_hp, level):
        return (2 * base_hp * level) // 100 + level + 10

    @staticmethod
    def calc_other(base_stat, level):
        return (2 * base_stat * level) // 100 + 5
    
    @staticmethod
    def xp_to_level(level, growth='medium'):
        if growth == 'fast':
            return (4 * level**3) // 5
        elif growth == 'medium':
            return level**3
        elif growth == 'slow':
            return (5 * level**3) // 4
        else:
            raise ValueError("Unknown growth type")
    
    def __str__(self):
        return f"{self.name} (Lvl {self.level}) - HP:{self.hp}, Atk:{self.attack}, Def:{self.defense}, Spd:{self.speed}, Spc:{self.special})"