from _Produkty import *

class Klienci:
    def __init__(self, age, name, surname, budget):
        self.age = age
        self.name = name
        self.surname = surname
        self.budget = budget

    def zrob_zakupy(self, piotr: Produkty, number_of_purchases: int):
        total_amount = piotr.price * number_of_purchases
        self.budget = self.budget - total_amount
        piotr.amount = piotr.amount - number_of_purchases