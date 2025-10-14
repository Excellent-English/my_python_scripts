try:
    points = int(input('Ile masz pkt? '))
    wiek = int(input('Ile masz lat? '))
    poziom = points / wiek
    with open('dane') as file:
        file.read()

except ValueError:
    print("Niepoprawny wiek")
    wiek = 0

except ZeroDivisionError:
    print("Wiek nie może być zerem.")

except FileNotFoundError:
    print("Plik nie został znaleziony.")

finally:
    print(f'Będziesz dorosły za {18 - wiek} lat.')