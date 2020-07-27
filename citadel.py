from rick import Rick


class Citadel(object):

    def __init__(self):
        self.__residents__ = []

    def get_all_residents(self):
        return self.__residents__

    def add_resident(self, resident):
        self.__residents__.append(resident)

    def pickle_ricks_with_morties(self):
        for resident in self.__residents__:
            if isinstance(resident, Rick):
                if resident.morty:
                    resident.is_pickle = True
