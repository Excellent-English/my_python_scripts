import random

class Random_values:
    def randomly_choose_numbers(self):

        numbers = list(range(1, 13))
        wyniki = {}

        for i in range(1, 13):
            los = random.choice(numbers)
            wyniki[f"zmienna_{i}"] = los
            numbers.remove(los)

        return wyniki