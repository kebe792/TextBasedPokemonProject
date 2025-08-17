from Player import Player
from Pokemon import Pokemon
import SystemFunctions

def main():

    NewPlayer = input(
        "Are you a new player?\n"
        "1 - Open Save\n"
        "2 - New Game\n"
        )

    if NewPlayer == "2":
        print("Starting new game...")
        Name = input("Enter your name: ")
        player = Player(Name)

        starter_map = {
        1: 1,  # 1 -> Bulbasaur
        2: 4,  # 2 -> Charmander
        3: 7   # 3 -> Squirtle
        }

        # Ask the user for input
        choice = int(input(
            "Please select your Starter Pokémon:\n"
            "1 - Bulbasaur\n"
            "2 - Charmander\n"
            "3 - Squirtle\n"
        ))

        # Validate input
        if choice in starter_map:
            starter_id = starter_map[choice]
            starter_pokemon = Pokemon(starter_id)
            player.add_to_team(starter_pokemon,level= 1)
        else:
            print("Invalid selection! Please enter 1, 2, or 3.")

        # Show current team
        print("Your team:")
        print(player.show_team())
    else:
        try:
            Saves = SystemFunctions.FetchSave_Data()
            Saved_Names = Saves["Name"].unique().tolist()
        except FileNotFoundError:
            print("No save file found! Starting new game instead.")
        
        Choice = input(f"Please select Save: {Saved_Names}")
        try:
            player_saves = Saves[Saves["Name"] == Choice]
            player = Player(Choice)
            for _, row in player_saves.iterrows():
                if str(row["Pokemon"]) == "NaN":
                    continue
                pokemon = Pokemon(poke_id=row["ID"])
                player.add_to_team(pokemon, level=row["Level"])
        except Exception as e:
            print(f"Error loading save: {e}")

    player.show_team()
    Player.Save_Game(player)

if __name__ == "__main__":
    main()