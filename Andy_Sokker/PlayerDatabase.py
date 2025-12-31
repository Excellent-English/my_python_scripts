from Player import Player
from Database import Database


class PlayerDatabase(Database):
    def create_player(self, player:Player):

        # self.get_player_from_id(player)


        with self.connect() as conn:
            c = conn.cursor()
            c.execute("""
            INSERT INTO players (
            Season, Round, ID, Name, TeamID, Age, Country, Value, Salary, Price, EndOfSale, Matches, Goals, Assists, Stamina, Speed, Technique, Passing, GK, DEF, MID, ATT
            )
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (player.Season, player.Round, player.ID, player.Name, player.TeamID, player.Age, player.Country,
            player.Value, player.Salary, player.Price, player.EndOfSale,player.Matches, player.Goals, player.Assists,
            player.Stamina, player.Speed, player.Technique, player.Passing, player.GK, player.DEF, player.MID, player.ATT))
            conn.commit()


    def get_players(self):
        with self.connect() as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM players")
            rows = c.fetchall()
            # print(rows)
            return rows


    def get_player_from_id(self, new_player:Player):
        with self.connect() as conn:
            c = conn.cursor()
            c.execute(f"SELECT Season, Round, ID FROM players WHERE ID = {new_player.ID} ORDER BY LP DESC LIMIT 1")
            row = c.fetchone()
            if row is None:
                return None, None, None

            return row
            # season, round, ID = row

            return season, round, ID


    def update_player(self):
        lp_to_update = input("Which LP should be updated?: ")
        try:
            lp_to_update = int(lp_to_update)
        except ValueError:
            print("Incorrect value!")
            return

        with self.connect() as conn:
            c = conn.cursor()
            c.execute("""
            UPDATE players
            SET Age = 18, Salary = 400, Country = 44, Stamina = 4
            WHERE LP = ?
            """,(lp_to_update,))
            conn.commit()

        print(f"Player with LP {lp_to_update} has been updated.")


    def delete_player(self):
        lp = input("Which LP should be deleted?: ")
        try:
            lp = int(lp)
        except ValueError:
            print("Incorrect value!")
            return

        with self.connect() as conn:
            c = conn.cursor()

            c.execute("SELECT * FROM players WHERE LP = ?", (lp,))
            if c.fetchone() is None:
                print(f"Player with LP: {lp} does not exist.")
                return

            # usuń zawodnika
            c.execute("DELETE FROM players WHERE LP = ?", (lp,))
            conn.commit()
            print(f"Player with LP {lp} has been deleted.")



    def upload_players_from_list(self, list_of_players: list[Player]):

        # list_of_players = [
        #     [1234, "Jakub", 123, 18, 43, 200000, 30000, 1, "2025-11-27", 5, 3, 6, 7, 10, 2, 0, 6],
        #     [1, "Jakub", 123, 20, 43, 200000, 30000, 1, "2025-11-27", 5, 3, 6, 7, 10, 2, 0, 6],
        #     [1, "Jakub", 123, 20, 45, 200000, 30000, 1, "2025-11-27", 5, 3, 6, 7, 10, 2, 0, 6],
        #     [1, "Jakub", 123, 20, 45, 300000, 30000, 1, "2025-11-27", 5, 3, 6, 7, 10, 2, 0, 6],
        #     [1, "Jakub", 123, 20, 45, 300000, 60000, 1, "2025-11-27", 5, 3, 6, 7, 10, None, 0, 6],
        #     [1, "Jakub", 123, 20, 45, 300000, 60000, 1, "2025-11-27", 5, 3, None, 7, 10, 2, 0, 6]
        # ]

        for i in range(len(list_of_players)):
            test_player = list_of_players[i]
            self.create_player(test_player)