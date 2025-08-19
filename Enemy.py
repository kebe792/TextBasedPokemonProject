from Characters import Character
from faker import Faker

class Enemy(Character):
    def __init__(self):
        super().__init__() 
        fake = Faker()
        self.Name = fake.first_name()