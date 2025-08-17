from Player import Player


def main():

    Name = input("Enter your name: ")
    player = Player(Name)
    print(player.Character.Team)



if __name__ == "__main__":
    main()