import os


class FashionItem():
    def __init__(self, ID, size, colour, category, filename):
        self.size = size
        self.colour = colour
        self.category = category
        self.ID = ID
        self.filename = filename


class Catalogue():
    def __init__(self):
        # os.path.join('data','Hat1.jpeg')

        hat1 = FashionItem(34, 1, "White", "Hat",
                           os.path.join('data', 'Hat1.jpeg'))
        hat2 = FashionItem(35, 1, "Black", "Hat",
                           os.path.join('data', 'Hat2.jpeg'))
        hat3 = FashionItem(36, 1, "Black", "Hat",
                           os.path.join('data', 'Hat2.jpeg'))

        jean1 = FashionItem(23, 'M', "Grey", "Jeans",
                            os.path.join('data', 'Jeans1.jpeg'))
        jean2 = FashionItem(24, 'M', "Navy", "Jeans",
                            os.path.join('data', 'Jeans2.jpeg'))
        jean3 = FashionItem(25, 'M', "Silver", "Jeans",
                            os.path.join('data', 'Jeans3.jpeg'))
        jean4 = FashionItem(26, 'M', "Light Blue", "Jeans", os.path.join(
            'data', 'Jeans4.jpeg'))

        shoe1 = FashionItem(67, 9, "White", "Shoes", "data/Shoes1.jpeg")
        shoe2 = FashionItem(67, 9, "Black", "Shoes", "data/Shoes2.jpeg")
        shoe3 = FashionItem(67, 9, "Checkered", "Shoes", "data/Shoes3.jpeg")

        tshirt1 = FashionItem(72, 'S', "Brown", "Tshirt", "data/Tshirt1.jpeg")
        tshirt2 = FashionItem(73, 'S', "Grey", "Tshirt", "data/Tshirt2.jpeg")
        tshirt3 = FashionItem(74, 'S', "Brown", "Tshirt", "data/Tshirt3.jpeg")

        self.hat_items = [hat1, hat2, hat3]
        self.jean_items = [jean1, jean2, jean3, jean4]
        self.shoe_items = [shoe1, shoe2, shoe3]
        self.tshirt_items = [tshirt1, tshirt2, tshirt3]

    # methods for item ids

    def get_hat_ids(self):
        return [hat.ID for hat in self.hat_items]

    def get_jeans_ids(self):
        return [jean.ID for jean in self.jeans_items]

    def get_shoes_ids(self):
        return [shoe.ID for shoe in self.shoes_items]

    def get_tshirt_ids(self):
        return [tshirt.ID for tshirt in self.tshirt_items]

    # methods for item filenames

    def get_hats_filenames(self):
        return [hat.filename for hat in self.hat_items]

    def get_jean_filenames(self):
        return [jean.filename for jean in self.jean_items]

    def get_tshirt_filenames(self):
        return [tshirt.filename for tshirt in self.tshirt_items]

    def get_shoe_filenames(self):
        return [shoe.filename for shoe in self.shoe_items]
