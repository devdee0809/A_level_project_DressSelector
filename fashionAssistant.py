import random
from random import randint
from catalogue import Catalogue


class FashionAsisstant:
    def __init__(self):
        self.load_catalogue()

    def generate_outfit(self):
        pass

    def load_catalogue(self):
        self.catalogue = Catalogue()


class RandomFashionAsisstant(FashionAsisstant):

    def __init__(self):
        super().__init__()

    def generate_outfit(self):
        self.chosen_headwear_id()
        self.chosen_tshirt_id()
        self.chosen_legwear_id()
        self.chosen_shoes_id()

    def chosen_headwear_id(self):
        hat_ids = self.catalogue.get_hat_ids()
        return random.choice(hat_ids)

    def chosen_tshirt_id(self):
        jean_ids = self.catalogue.get_jean_ids()
        return random.choice(jean_ids)

    def chosen_legwear_id(self):
        tshirt_ids = self.catalogue.get_tshirt_ids()
        return random.choice(tshirt_ids)

    def chosen_shoes_id(self):
        shoes_ids = self.catalogue.get_shoes_ids()
        return random.choice(shoes_ids)
