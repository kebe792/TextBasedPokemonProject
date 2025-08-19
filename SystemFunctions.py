import json

def fetch_saved_names(filename="player.json"):
    try:
        with open(filename, "r") as f:
            all_players = json.load(f)
        # Keys are the player names
        return list(all_players.keys())
    except FileNotFoundError:
        print("No save file found! Starting new game instead.")
        return []