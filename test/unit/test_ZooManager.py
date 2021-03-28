from Managers import ZooManager
from Enumerators.Thermoregulation import ThermoregulationType
from Enumerators.SortOrder import SortOrder
from ZooAnimals.Animal import Animal
from operator import attrgetter
import unittest


class ZooManagerTest(unittest.TestCase):
    def setUp(self):
        self.animals_test_list = \
            [
                Animal(200, ThermoregulationType.WARM_BLOODED, 7, "Bear"),
                Animal(5, ThermoregulationType.COLD_BLOODED, 4, "Octopus"),
                Animal(50, ThermoregulationType.WARM_BLOODED, 8, "Monkey"),
                Animal(10, ThermoregulationType.WARM_BLOODED, 9, "Fox"),
                Animal(30, ThermoregulationType.COLD_BLOODED, 3, "Shark")
            ]
        self.test_manager = ZooManager.ZooManager(self.animals_test_list.copy())

    def test_sort_by_animal_type_asc(self, sort_order=SortOrder.ASC):
        sorted_test_list = self.test_manager.all_animals.copy()
        sorted_test_list.sort(key=attrgetter("ANIMAL_TYPE"), reverse=sort_order.value)
        self.assertEqual(self.test_manager.sort_list_by_animal_type(sort_order=sort_order), sorted_test_list)
        sorted_test_list = self.animals_test_list.copy()
        sorted_test_list.sort(key=attrgetter("ANIMAL_TYPE"), reverse=sort_order.value)
        self.assertEqual(
            self.test_manager.sort_list_by_animal_type(self.animals_test_list.copy(), sort_order), sorted_test_list
        )

    def test_sort_by_animal_type_attributes(self):
        """Test of attributes in sort_by_animal_type function"""
        """Check whether Attribute error will be raised if animal_list contains non-Animal objects"""
        self.assertRaises(AttributeError, self.test_manager.sort_list_by_animal_type, [self.animals_test_list[0], 10])
        self.assertRaises(AttributeError, self.test_manager.sort_list_by_animal_type, [10, 20, 14])
        """Check whether AttributeError will be raised if type(sort_order) is not SortOrder"""
        self.assertRaises(AttributeError, self.test_manager.sort_list_by_animal_type, self.animals_test_list, False)

    def test_get_all_animals_over_5yo_return(self):
        expected_result_list = []
        for animal in self.animals_test_list:
            if animal.lifetime_in_years >= 5:
                expected_result_list.append(animal)
        expected_result_list.sort(key=attrgetter("ANIMAL_TYPE"))
        self.assertEqual(expected_result_list, self.test_manager.get_all_animals_over_5yo())

    def test_get_all_animals_over_5yo_attributes(self):
        self.assertRaises(AttributeError, self.test_manager.get_all_animals_over_5yo, ["Bear", "Bee", "Behemoth"])
        bad_array_example = [
            {"ANIMAL_TYPE": "Bear", "lifetime_in_years": 7},
            {"ANIMAL_TYPE": "Bee", "lifetime_in_years": 0.05},
            {"ANIMAL_TYPE": "Behemoth", "lifetime_in_years": 11}
        ]
        self.assertRaises(AttributeError, self.test_manager.get_all_animals_over_5yo, bad_array_example)
