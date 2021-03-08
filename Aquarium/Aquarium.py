class Aquarium:
    def __init__(self, capacity_in_liters, supported_min_temperature, supported_max_temperature,
                 supported_lighting_level, inhabitants=None):
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
