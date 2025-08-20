from Player import Player
from Pokemon import Pokemon
import SystemFunctions
from Enemy import Enemy
import random
from PokeBalls import Pokeball, GreatBall, UltraBall, MasterBall
from World import World

def main():

    world = World()    

    NewPlayer = input(
        "Are you a new player?\n"
        "1 - Open Save\n"
        "2 - New Game\n"
        )

    if NewPlayer == "2":
        print("Starting new game...")
        Name = input("Enter your name: ")
        player = Player(Name, world.get_city("Pallet Town"))

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
            
            player = Player.load(world, name=Choice)
            player.show_team()
            player.Bag.show_contents()
        except Exception as e:
            print(f"Error loading save: {e}")

    # player.Character.add_to_team(Pokemon.GetLeveled(poke_id=150, level=50))
    # player.check_level_up()
    # TrialEnemy = Enemy()
    # TrialEnemy.add_to_team(Pokemon.GetLeveled(poke_id=random.randint(1, 151),level=random.randint(1, 50)))
    # print(f"Name:{TrialEnemy.Name}, Pokemon: {TrialEnemy.Team[0]}")
    # player.Bag.add_item(item=PokeBalls.Pokeball(), quantity=10)
    # player.save()
    # player.Team[0] = Pokemon.GetLeveled(poke_id=player.Team[0].id,level=player.Team[0].level +1)

    player.Bag.add_item(Pokeball(), quantity=10)
    player.Bag.add_item(MasterBall(), quantity=10)

    while True:
        print(f"\nYou are currently in {player.current_city.name}")
        Option = input("What would you like to do\n"
        "1 - Move City\n"
        "2 - Battle\n"
        "3 - Heal\n"
        "4 - Shop\n"
        "5 - Find Pokemon\n"
        "0 - Leave And Save\n")

        if Option == '1' :
            while True:
                print("Where would you like to go?")

                # Show connected cities
                connections = player.current_city.connections
                for i, city in enumerate(connections, start=1):
                    print(f"{i}. {city.name}")

                choice = input("0. Quit\n"
                               "Enter choice: ")

                if choice == "0":
                    print("Goodbye!")
                    break

                try:
                    idx = int(choice) - 1
                    if 0 <= idx < len(connections):
                        player.move_to(connections[idx])
                    else:
                        print("Invalid choice")
                except ValueError:
                    print("Please enter a number.")
        elif Option == '2':
            print("nothing")
        elif Option == '3':
            print("nothing")
        elif Option == '4':
            print("nothing")
        elif Option == '5':
            found_pokemon = player.current_city.find_pokemon()
            if not found_pokemon:
                input("No Pokémon appeared! Press Enter to continue.")
                continue

            pokeballs = player.Bag.list_pokeballs() 
            if not pokeballs:
                input("You have no Pokéballs! Press Enter to continue.")
                continue

            print("Do you want to try catching it?")
            print("1 - Yes")
            print("2 - No")
            catch_choice = input("Enter choice: ")
            if catch_choice != "1":
                print(f"You decided not to try catching {found_pokemon.name}.")
                continue

            # List available Pokéballs
            print("Select a Pokéball to use:")
            for i, (name, data) in enumerate(pokeballs.items(), start=1):
                print(f"{i} - {name} x{data['quantity']}")

            choice = input("Enter number: ")
            try:
                idx = int(choice) - 1
                ball_name = list(pokeballs.keys())[idx]  # get the selected ball name
                player.try_catch(found_pokemon, ball_name)
            except (ValueError, IndexError):
                print("Invalid choice")

        elif Option == '0':
            player.save()
            break

if __name__ == "__main__":
    main()