from PlayerDatabase import PlayerDatabase
from Player import Player
from Sokker import Sokker

def main():
    my_database = PlayerDatabase()
    my_database.create_table()

    my_player = Player(374,Age=27, Salary=2400, Name="Marek", Country=22)

    print(f"Database before: {my_database.get_players()}")

    choice = input("Do you want to create, update or delete player? ")
    if choice == "create":
        my_database.create_player(my_player)
    elif choice == "update":
        my_database.update_player()
    elif choice == "delete":
        my_database.delete_player()

    print(f"Database after: {my_database.get_players()}")

# main()



def add_player_from_transfer_list_to_database():

    # Utwórz obiekt bazy danych i tabelę

    my_database = PlayerDatabase()
    my_database.create_table()

    sokker_object = Sokker("asciutto", "harrypotter", 1, 1, "PL")

    def save_to_db(players_data_page):
        for pdata in players_data_page:
            player_to_database = Player(
                Season=pdata["Season"],
                Round=pdata["Round"],
                ID=pdata["ID"],
                Name=pdata["Name"],
                TeamID=pdata["Team_ID"],
                Age=pdata["Age"],
                Country=pdata["Country_ID"],
                Value=pdata["Value"],
                Salary=pdata["Salary"],
                Price=pdata["Price"],
                EndOfSale=pdata["EndOfSale"],
                Matches=pdata["Matches"],
                Goals=pdata["Goals"],
                Assists=pdata["Assists"],
                Stamina=pdata["Stamina"],
                Speed=pdata["Speed"],
                Technique=pdata["Technique"],
                Passing=pdata["Passing"],
                GK=pdata["GK"],
                DEF=pdata["DEF"],
                MID=pdata["MID"],
                ATT=pdata["ATT"]
            )

            season, round, ID = my_database.get_player_from_id(player_to_database)
            if player_to_database.Season == season and player_to_database.Round == round and player_to_database.ID == ID:
                continue
            else:
                my_database.create_player(player_to_database)

    # Przekazujemy callback do metody Sokker
    sokker_object.go_to_transfer_list(save_to_db)

    # print(f"Database after: {my_database.get_players()}")


add_player_from_transfer_list_to_database()




# new_player = Player(75,19,39998251,"Costel Velcu",29771,17,9,268000,3900,1,"2025-12-02 08:13",0,0,0,2,1,0,2,1,8,5,8)
# PlayerDatabase.get_player_from_id(new_player)



def main2():
    my_database = PlayerDatabase()
    my_database.create_table()

    new_player = Player(75, 19, 39998251, "Costel Velcu", 29771, 17, 9, 268000, 3900, 1, "2025-12-02 08:13", 0, 0, 0, 2,
                        1, 0, 2, 1, 8, 5, 8)
    my_database.get_player_from_id(new_player)

    print(new_player.Season)

# main2()