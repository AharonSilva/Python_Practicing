class Rick(object):
    def __init__(self, universe):
        self.universe = universe
        self.morty = None
        self.is_pickle = False

    def assign(self, morty):
        self.morty = morty
        morty.is_assigned = True
