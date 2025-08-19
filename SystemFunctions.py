import pandas as pd
from Player import Player
from Pokemon import Pokemon
import os

def FetchSave_Data(SaveFile = "save_game.csv"):
    
    Saves = pd.read_csv(SaveFile)
    
    return Saves

def Load_Game(player, filename="save_game.csv"):
    """
    Load a player's saved team from CSV and populate player.Character.Team
    :param player: Player object whose team will be loaded
    """
    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        print("No save file found.")
        return

    try:
        saves_df = pd.read_csv(filename)
    except pd.errors.EmptyDataError:
        print("Save file is empty.")
        return

    # Filter for this player's saved team
    player_team_df = saves_df[saves_df["Name"] == player.Name]
    if player_team_df.empty:
        print(f"No save found for {player.Name}.")
        return

    # Reset the team to empty slots
    player.Character.Team = [None] * 6

    # Recreate each Pokemon object at the saved level
    for idx, row in player_team_df.iterrows():
        if row["ID"] == 0:
            continue  # skip empty slots in CSV

        poke = Pokemon.GetLeveled(row["ID"], int(row["Level"]))
        poke.hp = row["Current HP"]
        poke.xp = row.get("XP", 0)

        # Place in first available slot
        for i in range(6):
            if player.Character.Team[i] is None:
                player.Character.Team[i] = poke
                break

    print(f"Game loaded for {player.Name}!")

def Save_Game(player, filename="save_game.csv"):

        # Convert the team of Pokemon objects to a list of dicts
        team_to_save = []
        for poke in player.Character.Team:
            if poke is not None:  # skip empty slots
                team_to_save.append({
                    "Name": player.Name,       # player name
                    "Pokemon": poke.name,
                    "ID": poke.id,
                    "Level": poke.level,
                    "Max HP": poke.hp,
                    "Current HP": poke.hp,  # or track separately if needed
                    "XP": getattr(poke, "xp", 0),
                    "Attack": poke.attack,
                    "Defense": poke.defense,
                    "Speed": poke.speed,
                    "Special": poke.special,
                    "Zone": poke.zone,
                    "Total": poke.total,
                    "Average": poke.average
                })

        # Convert to DataFrame
        team_df = pd.DataFrame(team_to_save)

        # Load existing save file
        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            try:
                saves_df = pd.read_csv(filename)
            except pd.errors.EmptyDataError:
                saves_df = pd.DataFrame(columns=team_df.columns)
        else:
            saves_df = pd.DataFrame(columns=team_df.columns)

        # Remove any existing entries for this player
        saves_df = saves_df[saves_df["Name"] != player.Name]

        # Append the new team
        saves_df = pd.concat([saves_df, team_df], ignore_index=True)

        # Save back to CSV
        saves_df.to_csv(filename, index=False)
        print(f"Game saved for {player.Name}!")