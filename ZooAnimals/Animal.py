from Enumerators.Thermoregulation import ThermoregulationType


class Animal:
    def __init__(self, weight_in_kg=0, thermoregulation=None,
                 lifetime_in_years=0, animal_type="Not specified"):
        self._weight_in_kg = weight_in_kg
        self.THERMOREGULATION = thermoregulation
        self._lifetime_in_years = lifetime_in_years
        self.ANIMAL_TYPE = animal_type

    def __str__(self):
        return "Animal\n Type: {animal_type}\n Lifetime: {lifetime} years\n\
 Weight: {weight} kg\n Thermoregulation type: {thermoregulation}".format(animal_type=self.ANIMAL_TYPE,
                                                                         lifetime=self._lifetime_in_years,
                                                                         weight=self._weight_in_kg,
                                                                         thermoregulation=self.THERMOREGULATION)

    def __repr__(self):
        return self.ANIMAL_TYPE

    @property
    def weight_in_kg(self):
        return self._weight_in_kg

    @weight_in_kg.setter
    def weight_in_kg(self, new_weight):
        self._weight_in_kg = new_weight

    @property
    def lifetime_in_years(self):
        return self._lifetime_in_years

    @lifetime_in_years.setter
    def lifetime_in_years(self, new_lifetime):
        self._lifetime_in_years = new_lifetime
