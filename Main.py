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
            player.Character.add_to_team(starter_pokemon,level= 1)
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
        
        print("Please select Save:")
        for i, name in enumerate(Saved_Names, 1):
            print(f"{i}. {name}")

        choice_num = input("> ")

        # Validate input
        try:
            choice_num = int(choice_num)
            if 1 <= choice_num <= len(Saved_Names):
                Choice = Saved_Names[choice_num - 1]
                print(f"You selected: {Choice}")
            else:
                print("Invalid selection.")
                Choice = None
        except ValueError:
            print("Please enter a number.")
            Choice = None
        try:
            player_saves = Saves[Saves["Name"] == Choice]
            player = Player(Choice)
            for _, row in player_saves.iterrows():
                if str(row["ID"]) == "0":
                    continue
                pokemon = Pokemon(poke_id=row["ID"])
                player.Character.add_to_team(pokemon, level=row["Level"], xp=["XP"])
        except Exception as e:
            print(f"Error loading save: {e}")
    player.show_team()





if __name__ == "__main__":
    main()