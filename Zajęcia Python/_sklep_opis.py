from _Produkty import *
from _Klienci import *

Klient1 = Klienci(29,"Jan","Kowalski",5000)
Klient2 = Klienci(35,"Janek","Nowak",1000)

Produkt1 = Produkty("Jabłko",3,100)
Produkt2 = Produkty("Mandarynka",2,50)

dictionary_clients = {"Klient1":Klient1, "Klient2":Klient2}
dictionary_products = {"Produkt1":Produkt1, "Produkt2":Produkt2}

client_name = input("Który klient robi zakupy? ")
product_name = input("Który produkt został zakupiony? ")
product_amount = int(input("Ile sztuk danego produktu zostało zakupionych? "))

test_client = dictionary_clients.get(client_name)
test_product = dictionary_products.get(product_name)

print(test_client.budget)
print(test_product.price)
print(product_amount)

test_client.zrob_zakupy(test_product,product_amount)
print(test_client.budget)
print(test_product.amount)