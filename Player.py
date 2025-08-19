from Characters import Character
from Pokemon import Pokemon

class Player:
    def __init__(self, Name: str):
        self.Name = Name
        self.Character = Character()

    def show_team(self):
        for poke in self.Character.Team:
            print(poke)