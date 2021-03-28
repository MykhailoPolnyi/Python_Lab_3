from Enumerators.SortOrder import SortOrder
from operator import attrgetter


class ZooManager:
    def __init__(self, all_animals: list = None):
        self.__all_animals = all_animals

    @property
    def all_animals(self):
        return self.__all_animals

    @all_animals.setter
    def all_animals(self, new_animals_list: list):
        self.__all_animals = new_animals_list.copy()

    def sort_list_by_animal_type(self, animal_list=None, sort_order=SortOrder.ASC):
        if animal_list is None:
            animal_list = self.__all_animals
        animal_list.sort(key=attrgetter('ANIMAL_TYPE'), reverse=bool(sort_order.value))
        return animal_list

    def get_all_animals_over_5yo(self, animal_list=None, list_sort_order=SortOrder.ASC):
        if animal_list is None:
            animal_list = self.__all_animals.copy()
        animal_list.sort(key=attrgetter('lifetime_in_years'))
        first_animal_over5yo_index = len(animal_list)
        for animal in animal_list:
            if animal.lifetime_in_years >= 5:
                first_animal_over5yo_index = animal_list.index(animal)
                break
        all_animals_over_5yo = animal_list[first_animal_over5yo_index:].copy()
        del animal_list
        self.sort_list_by_animal_type(all_animals_over_5yo, list_sort_order)
        return all_animals_over_5yo
