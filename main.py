from Enumerators import LightingLevel, Thermoregulation, SortOrder
from ZooAnimals import Fish, Octopus
from Aquarium.Aquarium import Aquarium
from Managers import ZooManager, AquariumsManager


class Test:
    def __init__(self):
        pass

    @classmethod
    def main(cls):
        aq_anim_1 = Fish.Fish(15, Thermoregulation.ThermoregulationType.COLD_BLOODED, 7, "Swordfish", 400, 20,
                              LightingLevel.LightingLevel.MEDIUM, "Grey")

        aq_anim_2 = Octopus.Octopus(8, Thermoregulation.ThermoregulationType.COLD_BLOODED, 5, "Octopus", 200, 25,
                                    LightingLevel.LightingLevel.DARK, "Red")

        aq_anim_3 = Fish.Fish(80, Thermoregulation.ThermoregulationType.COLD_BLOODED, 6, "Shark", 600, 23,
                              LightingLevel.LightingLevel.MEDIUM, "Blue")

        zoo_aquarium_1 = Aquarium(700, 15, 30, [LightingLevel.LightingLevel.MEDIUM, LightingLevel.LightingLevel.DARK])

        aq_anim_4 = Fish.Fish(3, Thermoregulation.ThermoregulationType.COLD_BLOODED, 2, "Clownfish", 250, 20,
                              LightingLevel.LightingLevel.MEDIUM, "White-orange", zoo_aquarium_1)

        zoo_aquarium_2 = Aquarium(500, 15, 25, LightingLevel.LightingLevel.MEDIUM, [aq_anim_3, aq_anim_1])

        zoo_manger_1 = ZooManager.ZooManager([aq_anim_1, aq_anim_2, aq_anim_3, aq_anim_4])

        aquariums_manager_1 = AquariumsManager.AquariumsManager([aq_anim_1, aq_anim_3], [zoo_aquarium_1, zoo_aquarium_2])

        print("ZooManager testing:")
        print(zoo_manger_1.get_all_animals_over_5yo(None, SortOrder.SortOrder.DESC))
        print(zoo_manger_1.all_animals)
        zoo_manger_1.sort_list_by_animal_type()
        print(zoo_manger_1.all_animals)

        print("\nAquariumManager testing:")
        aquariums_manager_1.add_animals([aq_anim_4, aq_anim_2])
        aquariums_manager_1.change_animal_aquarium(aq_anim_2, zoo_aquarium_1)
        print(aquariums_manager_1.all_aquarium_animals)
        print(f"\nRequired aquarium: {aquariums_manager_1.request_aquarium_for_animal(aq_anim_1).__dict__} \n")
        aquariums_manager_1.sort_animal_list_by_aquarium_capacity()
        for animal in aquariums_manager_1.all_aquarium_animals:
            print(animal.ANIMAL_TYPE, "aquarium capacity:", animal.current_aquarium.capacity_in_liters)

        print("\nAquarium testing:")
        print(zoo_aquarium_1.inhabitants)
        print(zoo_aquarium_1.supported_lighting_level)
        print(zoo_aquarium_2.__dict__)
        aquariums_manager_1.sort_animal_list_by_aquarium_capacity()


if __name__ == "__main__":
    Test.main()
