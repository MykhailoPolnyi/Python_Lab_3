from Managers.AquariumsManager import AquariumsManager
from Aquarium.Aquarium import Aquarium
from Enumerators.LightingLevel import LightingLevel
from Enumerators.SortOrder import SortOrder
from ZooAnimals.AquariumAnimal import AquariumAnimal
from operator import attrgetter
import unittest


class AquariumManagerTest(unittest.TestCase):
    def setUp(self):
        self.aquarium_test_list = \
            [
                Aquarium(400, 20, 30, [LightingLevel.BRIGHT, LightingLevel.MEDIUM]),
                Aquarium(300, 15, 30, [LightingLevel.DARK, LightingLevel.MEDIUM]),
                Aquarium(500, 24, 30, [LightingLevel.BRIGHT, LightingLevel.MEDIUM])
            ]
        self.aquarium_animals_test_list = \
            [
             AquariumAnimal(weight_in_kg=10, lifetime_in_years=5, animal_type="SwordFish",
                            current_aquarium=self.aquarium_test_list[0], required_aquarium_capacity_liters=250,
                            required_lighting_level=LightingLevel.MEDIUM, required_temperature=25),
             AquariumAnimal(weight_in_kg=200, lifetime_in_years=7, animal_type="Shark",
                            required_aquarium_capacity_liters=500, required_temperature=25,
                            required_lighting_level=LightingLevel.BRIGHT, current_aquarium=self.aquarium_test_list[1]),
             AquariumAnimal(weight_in_kg=30, lifetime_in_years=3, animal_type="Dolphin",
                            required_aquarium_capacity_liters=300, required_temperature=25,
                            required_lighting_level=LightingLevel.MEDIUM, current_aquarium=self.aquarium_test_list[2])
            ]
        self.aq_manager = AquariumsManager(self.aquarium_animals_test_list, self.aquarium_test_list)

    def test_sort_animals_by_aquarium_capacity(self, sort_order=SortOrder.ASC):
        expected_result = self.aquarium_animals_test_list.copy()
        expected_result.sort(key=attrgetter("current_aquarium.capacity_in_liters"), reverse=sort_order.value)
        self.assertEqual(self.aq_manager.sort_animal_list_by_aquarium_capacity(sort_order=sort_order), expected_result)
        self.assertEqual(self.aq_manager.sort_animal_list_by_aquarium_capacity([]), [])

    def test_sort_animals_by_aquarium_capacity_attributes(self):
        self.assertRaises(AttributeError, self.aq_manager.sort_animal_list_by_aquarium_capacity, ["Octopus", 10])
        self.assertRaises(AttributeError, self.aq_manager.sort_animal_list_by_aquarium_capacity, [], False)

    def test_change_animal_aquarium(self):
        self.aq_manager.change_animal_aquarium(
            self.aq_manager.all_aquarium_animals[1], self.aq_manager.all_aquariums[0]
        )
        self.assertEqual(self.aquarium_test_list[0].inhabitants, self.aquarium_animals_test_list[0:2])
        self.assertEqual(self.aq_manager.all_aquarium_animals[1].current_aquarium, self.aquarium_test_list[0])

    def test_aquarium_manager_accessibility(self):
        inaccessible_animal = AquariumAnimal()
        inaccessible_aq = Aquarium()
        self.assertRaises(
            ValueError, self.aq_manager.change_animal_aquarium, inaccessible_animal, self.aq_manager.all_aquariums[1]
        )
        self.assertRaises(
            ValueError, self.aq_manager.change_animal_aquarium, self.aq_manager.all_aquarium_animals[0], inaccessible_aq
        )
        self.assertRaises(
            ValueError, self.aq_manager.change_animal_aquarium, inaccessible_animal, inaccessible_aq
        )
        self.assertRaises(ValueError, self.aq_manager.request_aquarium_for_animal, inaccessible_animal)
