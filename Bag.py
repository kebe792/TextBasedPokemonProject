from Item import Item
from PokeBalls import Pokeball, GreatBall, UltraBall

class Bag:
    def __init__(self):
        self.contents = {}  # list to hold items

    def add_item(self, item, quantity=1):
        if item.name in self.contents:
            self.contents[item.name]["quantity"] += quantity
        else:
            self.contents[item.name] = {"item": item, "quantity": quantity}
        return f"Added {quantity} x {item.name} to the bag."

    def show_contents(self):
        print("Bag contents:")
        for item_name, info in self.contents.items():
            print(f"{item_name}: {info['quantity']}")

    def list_pokeballs(self):
        return {
            name: {
                "quantity": info["quantity"],
                "catch_rate": info["item"].catch_rate
            }
            for name, info in self.contents.items()
            if isinstance(info["item"], Pokeball) and info["quantity"] > 0
        }


    def save(self):
        return {k: {"item": v["item"].save(), "quantity": v["quantity"]}
                for k, v in self.contents.items()}
    
    @classmethod
    def load(cls, data):
        bag = cls()
        bag.contents = {k: {"item": Item.from_dict(v["item"]), "quantity": v["quantity"]}
                        for k, v in data.items()}
        return bag