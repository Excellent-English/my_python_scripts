import Player
from PlayerDatabase import PlayerDatabase
from Player import Player
from Sokker import Sokker

def main():
    my_database = PlayerDatabase()
    my_database.create_table()
    # my_player = Player.Player(374,Age=27, Salary=2400, Name="Marek", Country=22)

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

    my_database = PlayerDatabase()
    my_database.create_table()

    # Tworzymy obiekt Sokker
    sokker_object = Sokker("asciutto", "harrypotter", 1, 1, "PL")

    # Tworzymy obiekt Player
    player_to_database = Player(
        ID=None, Name=None, TeamID=None, Age=None, Country=None,
        Value=None, Salary=None, Price=None, EndOfSale=None,
        Stamina=None, Speed=None, Technique=None, Passing=None,
        GK=None, DEF=None, MID=None, ATT=None
    )

    print(f"Database before: {my_database.get_players()}")

    # Pobieramy nazwę zawodnika z listy transferowej
    (season_from_transfer_list,
    round_from_transfer_list,
    ID_from_transfer_list,
    name_from_transfer_list,
    teamid_from_transfer_list,
    age_from_transfer_list,
    countryid_from_transfer_list,
    salary_from_transfer_list, price_from_transfer_list,
    value_from_transfer_list,
    endofsale_from_transfer_list,
    matches_from_tranfer_list,
    goals_from_transfer_list,
    assists_from_transfer_list,
    stamina_from_transfer_list,
    speed_from_transfer_list,
    technique_from_transfer_list,
    passing_from_transfer_list,GK_from_transfer_list,
    DEF_from_transfer_list,
    MID_from_transfer_list,
    ATT_from_transfer_list)\
    = sokker_object.go_to_transfer_list()

    # Przypisujemy nazwę do obiektu Player
    player_to_database.Season = season_from_transfer_list
    player_to_database.Round = round_from_transfer_list
    player_to_database.ID = ID_from_transfer_list
    player_to_database.Name = name_from_transfer_list
    player_to_database.TeamID = teamid_from_transfer_list
    player_to_database.Age = age_from_transfer_list
    player_to_database.Country = countryid_from_transfer_list
    player_to_database.Salary = salary_from_transfer_list
    player_to_database.Price = price_from_transfer_list
    player_to_database.Value = value_from_transfer_list
    player_to_database.EndOfSale = endofsale_from_transfer_list
    player_to_database.Matches = matches_from_tranfer_list
    player_to_database.Goals = goals_from_transfer_list
    player_to_database.Assists = assists_from_transfer_list
    player_to_database.Stamina = stamina_from_transfer_list
    player_to_database.Speed = speed_from_transfer_list
    player_to_database.Technique = technique_from_transfer_list
    player_to_database.Passing = passing_from_transfer_list
    player_to_database.GK = GK_from_transfer_list
    player_to_database.DEF = DEF_from_transfer_list
    player_to_database.MID = MID_from_transfer_list
    player_to_database.ATT = ATT_from_transfer_list

    my_database.create_player(player_to_database)
    print(f"Database after: {my_database.get_players()}")

add_player_from_transfer_list_to_database()