from .AquariumAnimal import AquariumAnimal


class Octopus(AquariumAnimal):
    def __init__(self, weight_in_kg, thermoregulation, lifetime_in_years, animal_type,
                 required_aquarium_capacity_liters, required_temperature, required_lighting_level, color,
                 current_aquarium=None):
        super(Octopus, self).__init__(weight_in_kg, thermoregulation, lifetime_in_years, animal_type,
                                      required_aquarium_capacity_liters, required_temperature, required_lighting_level,
                                      current_aquarium)
        self.color = color

    def __str__(self):
        return "{prev_info}\n Color: {color}".format(prev_info=super(Octopus, self).__str__(), color=self.color)
