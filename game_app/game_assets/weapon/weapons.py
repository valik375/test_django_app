class Weapon:

    def __init__(self, name, damage, price):
        self.name = name
        self.damage = damage
        self.price = price

    def hit(self):
        return self.damage


class Axe(Weapon):
    pass


class Sword(Weapon):
    pass

