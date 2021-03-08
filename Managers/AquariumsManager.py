from .ZooManager import ZooManager
from Aquarium.Aquarium import Aquarium
from Enumerators.SortOrder import SortOrder
from operator import attrgetter


class AquariumsManager(ZooManager):
    def __init__(self, all_aquarium_animals: list, all_aquariums: list):
        self.__all_aquarium_animals = all_aquarium_animals
        self.all_aquariums = all_aquariums

    @property
    def all_aquarium_animals(self):
        return self.__all_aquarium_animals

    @all_aquarium_animals.setter
    def all_aquarium_animals(self, new_animals_list: list):
        self.__all_aquarium_animals = new_animals_list.copy()

    def add_animals(self, new_animals: list):
        self.__all_aquarium_animals.extend(new_animals)

    def change_animal_aquarium(self, animal, new_aquarium: Aquarium):
        if animal not in self.__all_aquarium_animals:
            raise(ValueError("Current Manager can't access this animal"))
        if new_aquarium not in self.all_aquariums:
            raise(ValueError("Current Manager can't access this aquarium"))
        if animal.current_aquarium is not None:
            animal.current_aquarium.inhabitants.remove(animal)
        animal.current_aquarium = new_aquarium
        new_aquarium.inhabitants.append(animal)

    def request_aquarium_for_animal(self, chosen_animal):
        if chosen_animal not in self.__all_aquarium_animals:
            raise (ValueError("Current Manager can't access this animal"))
        requested_aquarium = Aquarium(chosen_animal.required_aquarium_capacity_in_liters,
                                      chosen_animal.required_temperature, chosen_animal.required_temperature,
                                      chosen_animal.required_lighting_level)
        return requested_aquarium

    def sort_animal_list_by_aquarium_capacity(self, sorted_list=None, sort_order=SortOrder.ASC):
        if sorted_list is None:
            sorted_list = self.__all_aquarium_animals
        sorted_list.sort(key=attrgetter('current_aquarium.capacity_in_liters'), reverse=bool(sort_order.value))
        return sorted_list
