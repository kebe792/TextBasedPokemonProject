import pandas as pd

class Pokemon:
    def __init__(self, poke_id, csv_file="KantoPokemon.csv"):

        # Read the CSV
        df = pd.read_csv(csv_file)

        # Find the row with the given ID
        row = df[df["ID"] == poke_id]

        if not row.empty:
            row = row.iloc[0]  # get the first (and only) matching row
            self.id = row["ID"]
            self.name = row["Pokémon"]
            self.hp = row["HP"]
            self.attack = row["Attack"]
            self.defense = row["Defense"]
            self.speed = row["Speed"]
            self.special = row["Special"]
            self.zone = row["Zone"]
            self.total = row["Total"]
            self.average = row["Average"]
        else:
            raise ValueError(f"Pokémon with ID {poke_id} not found in CSV.")
