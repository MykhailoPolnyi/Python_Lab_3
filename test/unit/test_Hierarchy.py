from ZooAnimals import *
import unittest


class HierarchyTest(unittest.TestCase):
    def test_hierarchy(self):
        test_fish = Fish.Fish()
        fish_hierarchy_tree = Fish.Fish, AquariumAnimal.AquariumAnimal, Animal.Animal
        self.assertIsInstance(test_fish, fish_hierarchy_tree)
        self.assertNotIsInstance(test_fish, Octopus.Octopus)
        test_octopus = Octopus.Octopus()
        octopus_hierarchy_tree = Octopus.Octopus, AquariumAnimal.AquariumAnimal, Animal.Animal
        self.assertIsInstance(test_octopus, octopus_hierarchy_tree)
        self.assertNotIsInstance(test_octopus, Fish.Fish)
