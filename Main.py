from Player import Player
from Pokemon import Pokemon
import SystemFunctions
from Enemy import Enemy
import random
import PokeBalls

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
            starter_pokemon = Pokemon.GetLeveled(starter_id,level=1)
            player.add_to_team(starter_pokemon)
        else:
            print("Invalid selection! Please enter 1, 2, or 3.")

    else:
        try:
            Saves = SystemFunctions.fetch_saved_names()
            # Saved_Names = Saves["Name"]
        except FileNotFoundError:
            print("No save file found! Starting new game instead.")
        
        print("Please select Save:")
        for i, name in enumerate(Saves, 1):
            print(f"{i}. {name}")

        choice_num = input("> ")

        # Validate input
        try:
            choice_num = int(choice_num)
            if 1 <= choice_num <= len(Saves):
                Choice = Saves[choice_num - 1]
                print(f"You selected: {Choice}")
            else:
                print("Invalid selection.")
                Choice = None
        except ValueError:
            print("Please enter a number.")
            Choice = None
        try:
            # player_saves = Saves[Saves["Name"] == Choice]
            player = Player.load(name=Choice)
            # SystemFunctions.Load_Game(player)
        except Exception as e:
            print(f"Error loading save: {e}")

    # player.Character.add_to_team(Pokemon.GetLeveled(poke_id=150, level=50))
    player.show_team()
    player.check_level_up()
    player.show_team()

    TrialEnemy = Enemy()
    TrialEnemy.add_to_team(Pokemon.GetLeveled(poke_id=random.randint(1, 151),level=random.randint(1, 50)))
    # SystemFunctions.Save_Game(player)
    print(f"Name:{TrialEnemy.Name}, Pokemon: {TrialEnemy.Team[0]}")

    player.Bag.add_item(item=PokeBalls.Pokeball(), quantity=10)
    player.Bag.add_item(item=PokeBalls.GreatBall(), quantity=5)

    player.save()
    player.Bag.show_contents()
    # player.Character.Team[0] = Pokemon.GetLeveled(poke_id=player.Character.Team[0].id,level=player.Character.Team[0].level +1)

if __name__ == "__main__":
    main()