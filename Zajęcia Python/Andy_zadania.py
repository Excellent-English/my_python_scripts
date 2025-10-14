def zadanie1():
    name = input("Podaj swoje imię: ")
    print("Cześć ", name)


def zadanie2():
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))
    print("Suma to:", a + b)


def zadanie3():
    x = int(input("Podaj liczbę: "))
    if x % 2 == 0:
        print("Liczba jest parzysta")
    else:
        print("Liczba jest nieparzysta")


def zadanie4():
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    if a > b and a > c:
        print("Największa to:", a)
    elif b > a and b > c:
        print("Największa to:", b)
    else:
        print("Największa to:", c)


def zadanie5():
    text = input("Podaj tekst: ")
    reversed = text.reverse()
    print("Odwrócony tekst:", reversed)
    # reversed_text = text[::-1]


def zadanie6():
    for i in range(1, 10):
        print(i)


def zadanie7():
    numbers = [2, 4, 6, 8, 10]
    avg = sum(numbers) / len(numbers)
    print("Średnia:", avg)


def zadanie8():
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))
    op = input("Podaj operację (+, -, *, /): ")
    if op == "+":
        print(f'"Wynik: " {a+b}')
    elif op == "-":
        print(f'"Wynik: " {a-b}')
    elif op == "*":
        print(f'"Wynik: " {a*b}')
    elif op == "/":
        print(f'"Wynik: " {a/b}')
    else:
        print("Nieznana operacja")