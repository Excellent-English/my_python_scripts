# test 1 - funkcja 1 z returnem w postaci zmiennej + funkcja 2 w tym samym oknie przejmującą tę zmienną

wynik = None

# przykład 1
def okno():

    def test_1():
        wynik = 2 + 3
        return wynik

    def test_1b():
        pierwszy_wynik = test_1()
        drugi_wynik = pierwszy_wynik + 5
        print(drugi_wynik)


# przykład 2
def okno2():

    wynik = None

    def test_1():
        nonlocal wynik
        wynik = 2 + 3
        x = 2
        return x

    def test_1b():
        drugi_wynik = wynik + 5
        wynik + 1
        print(drugi_wynik)


def test_3():
    global wynik
    wynik = 2 + 4
    return wynik


# test_3()




# test 2 - funkcja 1 z 3 returnami + funkcja 2 w tym samym oknie przejmująca te zmienne


# test 3 - funkcja 1 z returnem w postaci zmiennej + funkcja 2 w OSOBNYM oknie przejmującą tę zmienną