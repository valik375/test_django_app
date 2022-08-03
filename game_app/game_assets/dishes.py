class Food:
    def __init__(self, name, recovery_value, price):
        self.name = name
        self.recovery_value = recovery_value
        self.price = price


class Chicken(Food):
    pass


class Bread(Food):
    pass
