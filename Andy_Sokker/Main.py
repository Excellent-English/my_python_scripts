import Player
from PlayerDatabase import PlayerDatabase

def main():
    my_database = PlayerDatabase()
    my_database.create_table()
    my_player = Player.Player(374,Age=27, Salary=2400, Name="Marek", Country=22)

    print(f"Database before: {my_database.get_players()}")

    choice = input("Do you want to create, update or delete player? ")
    if choice == "create":
        my_database.create_player(my_player)
    elif choice == "update":
        my_database.update_player()
    elif choice == "delete":
        my_database.delete_player()

    print(f"Database after: {my_database.get_players()}")

main()