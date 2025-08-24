# from Player import Player
# from Pokemon import Pokemon
# import SystemFunctions
# from Enemy import Enemy
# import random
# from PokeBalls import Pokeball, GreatBall, UltraBall, MasterBall
# from World import World
# import pygame

# def main():

#     world = World()    

#     NewPlayer = input(
#         "Are you a new player?\n"
#         "1 - Open Save\n"
#         "2 - New Game\n"
#         )

#     if NewPlayer == "2":
#         print("Starting new game...")
#         Name = input("Enter your name: ")
#         player = Player(Name, world.get_city("Pallet Town"))

#         starter_map = {
#         1: 1,  # 1 -> Bulbasaur
#         2: 4,  # 2 -> Charmander
#         3: 7   # 3 -> Squirtle
#         }

#         # Ask the user for input
#         choice = int(input(
#             "Please select your Starter Pokémon:\n"
#             "1 - Bulbasaur\n"
#             "2 - Charmander\n"
#             "3 - Squirtle\n"
#         ))

#         # Validate input
#         if choice in starter_map:
#             starter_id = starter_map[choice]
#             starter_pokemon = Pokemon.GetLeveled(starter_id,level=1)
#             player.add_to_team(starter_pokemon)
#         else:
#             print("Invalid selection! Please enter 1, 2, or 3.")

#     else:
#         try:
#             Saves = SystemFunctions.fetch_saved_names()
#             # Saved_Names = Saves["Name"]
#         except FileNotFoundError:
#             print("No save file found! Starting new game instead.")
        
#         print("Please select Save:")
#         for i, name in enumerate(Saves, 1):
#             print(f"{i}. {name}")

#         choice_num = input("> ")

#         # Validate input
#         try:
#             choice_num = int(choice_num)
#             if 1 <= choice_num <= len(Saves):
#                 Choice = Saves[choice_num - 1]
#                 print(f"You selected: {Choice}")
#             else:
#                 print("Invalid selection.")
#                 Choice = None
#         except ValueError:
#             print("Please enter a number.")
#             Choice = None
#         try:
            
#             player = Player.load(world, name=Choice)
#             player.show_team()
#             player.Bag.show_contents()
#         except Exception as e:
#             print(f"Error loading save: {e}")

#     # player.Character.add_to_team(Pokemon.GetLeveled(poke_id=150, level=50))
#     # player.check_level_up()
#     # TrialEnemy = Enemy()
#     # TrialEnemy.add_to_team(Pokemon.GetLeveled(poke_id=random.randint(1, 151),level=random.randint(1, 50)))
#     # print(f"Name:{TrialEnemy.Name}, Pokemon: {TrialEnemy.Team[0]}")
#     # player.Bag.add_item(item=PokeBalls.Pokeball(), quantity=10)
#     # player.save()
#     # player.Team[0] = Pokemon.GetLeveled(poke_id=player.Team[0].id,level=player.Team[0].level +1)

#     player.Bag.add_item(Pokeball(), quantity=10)
#     player.Bag.add_item(MasterBall(), quantity=10)

    # while True:
    #     print(f"\nYou are currently in {player.current_city.name}")
    #     Option = input("What would you like to do\n"
    #     "1 - Move City\n"
    #     "2 - Battle\n"
    #     "3 - Heal\n"
    #     "4 - Shop\n"
    #     "5 - Find Pokemon\n"
    #     "0 - Leave And Save\n")

    #     if Option == '1' :
    #         while True:
    #             print("Where would you like to go?")

    #             # Show connected cities
    #             connections = player.current_city.connections
    #             for i, city in enumerate(connections, start=1):
    #                 print(f"{i}. {city.name}")

    #             choice = input("0. Quit\n"
    #                            "Enter choice: ")

    #             if choice == "0":
    #                 print("Goodbye!")
    #                 break

    #             try:
    #                 idx = int(choice) - 1
    #                 if 0 <= idx < len(connections):
    #                     player.move_to(connections[idx])
    #                 else:
    #                     print("Invalid choice")
    #             except ValueError:
    #                 print("Please enter a number.")
    #     elif Option == '2':
    #         print("nothing")
    #     elif Option == '3':
    #         print("nothing")
    #     elif Option == '4':
    #         print("nothing")
    #     elif Option == '5':
    #         found_pokemon = player.current_city.find_pokemon()
    #         if not found_pokemon:
    #             input("No Pokémon appeared! Press Enter to continue.")
    #             continue

    #         pokeballs = player.Bag.list_pokeballs() 
    #         if not pokeballs:
    #             input("You have no Pokéballs! Press Enter to continue.")
    #             continue

    #         print("Do you want to try catching it?")
    #         print("1 - Yes")
    #         print("2 - No")
    #         catch_choice = input("Enter choice: ")
    #         if catch_choice != "1":
    #             print(f"You decided not to try catching {found_pokemon.name}.")
    #             continue

    #         # List available Pokéballs
    #         print("Select a Pokéball to use:")
    #         for i, (name, data) in enumerate(pokeballs.items(), start=1):
    #             print(f"{i} - {name} x{data['quantity']}")

    #         choice = input("Enter number: ")
    #         try:
    #             idx = int(choice) - 1
    #             ball_name = list(pokeballs.keys())[idx]  # get the selected ball name
    #             player.try_catch(found_pokemon, ball_name)
    #         except (ValueError, IndexError):
    #             print("Invalid choice")

    #     elif Option == '0':
    #         player.save()
    #         break

# if __name__ == "__main__":
#     main()

import pygame
import sys
import random

from Player import Player
from Pokemon import Pokemon
import SystemFunctions
from Enemy import Enemy
from PokeBalls import Pokeball, GreatBall, UltraBall, MasterBall
from World import World

# ---------- Utility Functions for Pygame UI ----------

def draw_text(screen, text, font, color, x, y, line_height=40):
    """Draw multi-line text at x, y."""
    for i, line in enumerate(text.split("\n")):
        surface = font.render(line, True, color)
        screen.blit(surface, (x, y + i * line_height))

# ---------- Main Game ----------

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pokémon Adventure")
    font = pygame.font.SysFont("Arial", 28)
    clock = pygame.time.Clock()

    BLACK, WHITE = (0, 0, 0), (255, 255, 255)

    world = World()
    player = None
    state = "new_or_load"
    message = "Are you a new player?\n1 - Open Save\n2 - New Game"

    # Store temporary inputs
    selected_option = None
    found_pokemon = None

    running = True
    while running:
        screen.fill(BLACK)
        draw_text(screen, message, font, WHITE, 50, 50)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                key = event.unicode

                # ---------- STATE: Choose new or load ----------
                if state == "new_or_load":
                    if key == "2":  # New game
                        state = "ask_name"
                        message = "Enter your name (type then press Enter):"
                        typed_name = ""
                    elif key == "1":  # Load save
                        try:
                            Saves = SystemFunctions.fetch_saved_names()
                            save_list = "\n".join([f"{i+1} - {s}" for i, s in enumerate(Saves)])
                            message = f"Select Save:\n{save_list}"
                            state = "choose_save"
                        except FileNotFoundError:
                            message = "No save file found! Restarting..."
                            state = "new_or_load"

                # ---------- STATE: Name entry ----------
                elif state == "ask_name":
                    if event.key == pygame.K_RETURN:
                        player = Player(typed_name, world.get_city("Pallet Town"))
                        state = "choose_starter"
                        message = "Choose Starter:\n1 - Bulbasaur\n2 - Charmander\n3 - Squirtle"
                    elif event.key == pygame.K_BACKSPACE:
                        typed_name = typed_name[:-1]
                        message = "Enter your name:\n" + typed_name
                    else:
                        typed_name += key
                        message = "Enter your name:\n" + typed_name

                # ---------- STATE: Starter Selection ----------
                elif state == "choose_starter":
                    starter_map = { "1": 1, "2": 4, "3": 7 }
                    if key in starter_map:
                        starter_id = starter_map[key]
                        starter_pokemon = Pokemon.GetLeveled(starter_id, level=1)
                        player.add_to_team(starter_pokemon)
                        state = "city_menu"
                        message = f"You are in {player.current_city.name}\n1 - Move City\n2 - Battle\n3 - Heal\n4 - Shop\n5 - Find Pokémon\n6 - Display Team\n0 - Save & Exit"
                    else:
                        message = "Invalid! Choose:\n1 - Bulbasaur\n2 - Charmander\n3 - Squirtle"

                # ---------- STATE: Choose Save ----------
                elif state == "choose_save":
                    try:
                        idx = int(key) - 1
                        if 0 <= idx < len(Saves):
                            Choice = Saves[idx]
                            player = Player.load(world, name=Choice)
                            player.Bag.add_item(Pokeball(), quantity=10)
                            message = f"You are in {player.current_city.name}\n1 - Move City\n2 - Battle\n3 - Heal\n4 - Shop\n5 - Find Pokémon\n6 - Display Team\n0 - Save & Exit"
                            state = "city_menu"
                    except:
                        message = "Invalid choice!"

                # ---------- STATE: City Menu ----------
                elif state == "city_menu":
                    message = f"You are in {player.current_city.name}\n1 - Move City\n2 - Battle\n3 - Heal\n4 - Shop\n5 - Find Pokémon\n6 - Display Team\n0 - Save & Exit"
                    if key == "1":
                        connections = player.current_city.connections
                        conn_list = "\n".join([f"{i+1} - {c.name}" for i, c in enumerate(connections)])
                        message = f"Where would you like to go?\n{conn_list}\n0 - Cancel"
                        state = "move_city"
                    elif key == "4":
                        # Get available shop items
                        message = player.current_city.display_shop_items()
                        message = "Which item would you like to buy?"
                        choice = key
                        message = "How many?"
                        quantity = key
                        player.current_city.buy_ball(player, choice, quantity)

                        state = "city_menu"
                    elif key == "5":
                        found_pokemon = player.current_city.find_pokemon()
                        if not found_pokemon:
                            message = "No Pokémon appeared!\n\nReturning to city menu..."
                            state = "city_menu"
                        else:
                            message = f"A wild {found_pokemon.name} appeared!\nCatch it?\n1 - Yes\n2 - No"
                            state = "catch_prompt"
                    elif key == "6":
                        message = player.show_team()
                        state = "city_menu"
                    elif key == "0":
                        player.save()
                        message = "Game Saved. Exiting..."
                        state = "exit"

                # ---------- STATE: Move City ----------
                elif state == "move_city":
                    connections = player.current_city.connections
                    if key == "0":
                        state = "city_menu"
                        message = f"You are in {player.current_city.name}\n1 - Move City\n2 - Battle\n3 - Heal\n4 - Shop\n5 - Find Pokémon\n0 - Save & Exit"
                    else:
                        try:
                            idx = int(key) - 1
                            if 0 <= idx < len(connections):
                                player.move_to(connections[idx])
                                message = f"Moved to {player.current_city.name}\n1 - Move City\n2 - Battle\n3 - Heal\n4 - Shop\n5 - Find Pokémon\n0 - Save & Exit"
                                state = "city_menu"
                        except:
                            message = "Invalid!"

                # ---------- STATE: Catch Prompt ----------
                elif state == "catch_prompt":
                    if key == "1":
                        pokeballs = player.Bag.list_pokeballs()
                        if not pokeballs:
                            message = "You have no Pokéballs!"
                            state = "city_menu"
                        else:
                            ball_list = "\n".join([f"{i+1} - {name} x{data['quantity']}" for i,(name,data) in enumerate(pokeballs.items())])
                            message = f"Choose Pokéball:\n{ball_list}"
                            state = "choose_ball"
                    else:
                        message = f"You ignored {found_pokemon.name}."
                        state = "city_menu"

                # ---------- STATE: Choose Ball ----------
                elif state == "choose_ball":
                    pokeballs = player.Bag.list_pokeballs()
                    try:
                        idx = int(key) - 1
                        ball_name = list(pokeballs.keys())[idx]
                        message = player.try_catch(found_pokemon, ball_name)
                        state = "city_menu"
                    except:
                        message = "Invalid ball choice!"


                # ---------- STATE: Exit ----------
                elif state == "exit":
                    running = False

        clock.tick(30)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()


