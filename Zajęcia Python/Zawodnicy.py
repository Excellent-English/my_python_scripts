class Zawodnicy:
    def __init__(self,idZAWODNIKA,imie,kondycja,technika,strzelec):
        self.idZAWODNIKA = idZAWODNIKA
        self.imie = imie
        self.kondycja = kondycja
        self.technika = technika
        self.strzelec = strzelec


    def porownaj(self,a,b):
        if a==b:
            return True