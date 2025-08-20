from City import City


class World:
    def __init__(self):
        self.cities = {}
        self._build_world()

    def add_city(self, name: str, level_range=(1,5)) -> City:
        city = City(name, level_range=level_range)
        self.cities[name] = city
        return city

    def get_city(self, name: str) -> City:
        return self.cities.get(name)

    def _build_world(self):
        # Define cities
        pallet = self.add_city("Pallet Town", level_range=(1,5))
        viridian = self.add_city("Viridian City", level_range=(3,8))
        pewter = self.add_city("Pewter City", level_range=(5,12))
        Cerulean = self.add_city("Cerulean City", level_range=(7,15))
        Vermilion = self.add_city("Vermilion City", level_range=(10,18))
        Celadon = self.add_city("Celadon City", level_range=(12,20))
        Saffron = self.add_city("Saffron City", level_range=(15,25))
        Fuchsia = self.add_city("Fuchsia City", level_range=(18,28))
        Cinnabar = self.add_city("Cinnabar City", level_range=(20,30))

        # Define connections
        pallet.connect(viridian)
        viridian.connect(pewter)
        pewter.connect(Cerulean)
        Cerulean.connect(Vermilion)
        Vermilion.connect(Celadon)
        Celadon.connect(Saffron)
        Saffron.connect(Fuchsia)
        Fuchsia.connect(Cinnabar)