from Characters import Character
import pandas as pd
import os

class Player:
    def __init__(self, Name: str):
        self.Name = Name
        self.Character = Character()

    def show_team(self):
        print(self.Character.Team)

    def show_team(self):
        print(self.Character.Team)

    def Save_Game(self, filename="save_game.csv"):
        """
        Saves the player's team to a CSV file.
        Overwrites any existing entries for this player.
        Each Pokémon is stored as a separate row for readability.
        """
        # Prepare the player's team DataFrame with an extra column for the Name
        team_to_save = self.Character.Team.copy()
        team_to_save.insert(0, "Name", self.Name)

        # Load existing save file if it exists and is not empty
        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            try:
                saves_df = pd.read_csv(filename)
            except pd.errors.EmptyDataError:
                # File exists but is empty, create new DataFrame
                saves_df = pd.DataFrame(columns=team_to_save.columns)
        else:
            # File does not exist or is empty, start fresh
            saves_df = pd.DataFrame(columns=team_to_save.columns)

        # Remove any existing entries for this player
        saves_df = saves_df[saves_df["Name"] != self.Name]

        # Append the new team
        saves_df = pd.concat([saves_df, team_to_save], ignore_index=True)

        # Save back to CSV
        saves_df.to_csv(filename, index=False)
        print(f"Game saved for {self.Name}!")