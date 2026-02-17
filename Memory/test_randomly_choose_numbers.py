import random

numbers = [1,2,3,4,5,6,7,8,9,10,11,12]

while numbers != []:
    print(f'Obecna długość listy numbers to: {len(numbers)} znaków.')
    print(numbers)

    losowa_pozycja = random.randint(0,len(numbers)-1)
    print(f'Wylosowano liczbę znajdującą się na pozycji: {losowa_pozycja}.')
    print(f'Wylosowano liczbę: {numbers[losowa_pozycja]}')

    numbers.pop(losowa_pozycja)
    print("Usunięto wylosowaną liczbę.")
    print("Po tej akcji lista prezentuje się następująco:")
    print(numbers)
    print("---------------------------")

