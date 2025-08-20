class Item:
    def __init__(self, name, description=""):
        self.name = name
        self.description = description

    def save(self):
        return {
            "type": self.__class__.__name__,  # store the class type
            "name": self.name,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, data):
        item_type = data.get("type", "Item")
        if item_type == "Pokeball":
            from PokeBalls import Pokeball
            return Pokeball()
        elif item_type == "GreatBall":
            from PokeBalls import GreatBall
            return GreatBall()
        elif item_type == "UltraBall":
            from PokeBalls import UltraBall
            return UltraBall()
        else:
            return cls(data["name"], data.get("description", ""))
