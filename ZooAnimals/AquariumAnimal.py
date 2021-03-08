from .Animal import Animal


class AquariumAnimal(Animal):
    def __init__(self, weight_in_kg, thermoregulation, lifetime_in_years, animal_type,
                 required_aquarium_capacity_liters, required_temperature, required_lighting_level,
                 current_aquarium=None):
        super(AquariumAnimal, self).__init__(weight_in_kg, thermoregulation, lifetime_in_years, animal_type)
        self.required_aquarium_capacity_in_liters = required_aquarium_capacity_liters
        self.required_temperature = required_temperature
        self.required_lighting_level = required_lighting_level
        self.current_aquarium = current_aquarium
        if current_aquarium is not None:
            current_aquarium.inhabitants.append(self)
