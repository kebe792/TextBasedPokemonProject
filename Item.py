

class Item:
    def __init__(self, name, description=""):
        self.name = name
        self.description = description

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data.get("description"))

    def save(self):
        return {"name": self.name, "description": self.description}