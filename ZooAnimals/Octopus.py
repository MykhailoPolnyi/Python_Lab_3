from .AquariumAnimal import AquariumAnimal


class Octopus(AquariumAnimal):
    def __init__(self, weight_in_kg=0, thermoregulation=None, lifetime_in_years=0, animal_type="Not specified",
                 required_aquarium_capacity_liters=0, required_temperature=0, required_lighting_level=None,
                 color="Not specified", current_aquarium=None):
        super(Octopus, self).__init__(weight_in_kg, thermoregulation, lifetime_in_years, animal_type,
                                      required_aquarium_capacity_liters, required_temperature, required_lighting_level,
                                      current_aquarium)
        self.color = color

    def __str__(self):
        return "{prev_info}\n Color: {color}".format(prev_info=super(Octopus, self).__str__(), color=self.color)
