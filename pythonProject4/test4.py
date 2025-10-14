emp1 = ['Kamil', 'Musiał' , 234234, 23]
emp2 = ['Kasia', 'Musio' , 121212, 56]

class Employee:
    def __init__(self)
        self.imie = 'Kamil'
        self.nazwisko = ''
        self.id = 1234
        self.holidays = 26

    def update_holidays(self, days):
        if days > 0 and days <= self.holidays:
            self.holidays -= days
        else:
            print("Niepoprawne dane, brak zmian.")

    def add_holidays(self, days):
        if days > 0:
            pswd = input("Wprowadź hasło: ")
            if pswd == "admin1":
                print(f'Dodano {days} dni urlopu ')
                print(f'Wysłano maila do pracownika {self.id}')
                self.holidays =+ days


emp1 = Employee()
print(emp1.imie)
emp1.nazwisko = ('Nowakowski')
print(emp1.nazwisko)

napis = 'mama'
print(type(napis))

emp1.add_holidays(6)
print(emp1.holidays)

emp2.update_holidays(10)