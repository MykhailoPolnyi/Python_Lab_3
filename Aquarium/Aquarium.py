class Aquarium:
    def __init__(self, capacity_in_liters=0, supported_min_temperature=0, supported_max_temperature=0,
                 supported_lighting_level=None, inhabitants=None):
        self.capacity_in_liters = capacity_in_liters
        self.supported_min_temperature = supported_min_temperature
        self.supported_max_temperature = supported_max_temperature
        self.supported_lighting_level = supported_lighting_level
        if inhabitants is None:
            self.inhabitants = []
        else:
            self.inhabitants = inhabitants
            for animal in inhabitants:
                if animal.current_aquarium is not None:
                    animal.current_aquarium.inhabitants.remove(animal)
                animal.current_aquarium = self
