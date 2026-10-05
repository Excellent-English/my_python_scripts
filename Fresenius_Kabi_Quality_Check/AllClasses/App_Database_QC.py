import pyodbc

class Database_QC:

# funkcja nawiązująca połączenie z tabelową sqlową
    def get_connection(self):
        return pyodbc.connect(
            """
            Driver={ODBC Driver 18 for SQL Server};
            Server=tcp:sscciq.database.windows.net,1433;
            Database=SSC CIQ;
            Authentication=ActiveDirectoryIntegrated;
            """
        )

# 3 funkcje, które są uruchamiane po kliknięciu na "Save & next" button

    def change_1_to_2(self, Who_changed_from_1_to_2_or_3, Key_value_for_database, Controls_column):

        conn = self.get_connection()
        cursor = conn.cursor()

        query_to_update_from_1_to_2 = """
            UPDATE quality_check_database
            SET Verified = 2, Who_changed_from_1_to_2_or_3 = ?, When_changed_from_1_to_2_or_3 = GETDATE(), Controls = ?
            WHERE Key_value_for_database = ?
            """

        cursor.execute(
            query_to_update_from_1_to_2,
            (Who_changed_from_1_to_2_or_3, Controls_column, Key_value_for_database)
        )

        conn.commit()

        cursor.close()
        conn.close()


    def change_1_to_3(self, Who_changed_from_1_to_2_or_3, Key_value_for_database, Controls_column):

        conn = self.get_connection()
        cursor = conn.cursor()

        query_to_update_from_1_to_3 = """
            UPDATE quality_check_database
            SET Verified = 3, Who_changed_from_1_to_2_or_3 = ?, When_changed_from_1_to_2_or_3 = GETDATE(), Controls = ?
            WHERE Key_value_for_database = ?
            """

        cursor.execute(
            query_to_update_from_1_to_3,
            (Who_changed_from_1_to_2_or_3, Controls_column, Key_value_for_database)
        )

        conn.commit()

        cursor.close()
        conn.close()


    def change_2_to_4(self, Who_changed_from_2_to_4, Key_value_for_database):

        conn = self.get_connection()
        cursor = conn.cursor()

        query_to_update_from_2_to_4 = """
            UPDATE quality_check_database
            SET Verified = 4, Who_changed_from_2_to_4 = ?, When_changed_from_2_to_4 = GETDATE()
            WHERE Key_value_for_database = ?
            """

        cursor.execute(
            query_to_update_from_2_to_4,
            (Who_changed_from_2_to_4, Key_value_for_database)
        )

        conn.commit()

        cursor.close()
        conn.close()


    def change_4_to_5(self, Who_changed_from_4_to_5, Key_value_for_database):

        conn = self.get_connection()
        cursor = conn.cursor()

        query_to_update_from_4_to_5 = """
            UPDATE quality_check_database
            SET Verified = 5, Who_changed_from_4_to_5 = ?, When_changed_from_4_to_5 = GETDATE()
            WHERE Key_value_for_database = ?
            """

        cursor.execute(
            query_to_update_from_4_to_5,
            (Who_changed_from_4_to_5, Key_value_for_database)
        )

        conn.commit()

        cursor.close()
        conn.close()


# Funkcja uruchamiana za pomocą przycisku "Reject"

    def change_4_to_2(self, Who_changed_from_4_to_2, Key_value_for_database):

        conn = self.get_connection()
        cursor = conn.cursor()

        query_to_update_from_4_to_2 = """
            UPDATE quality_check_database
            SET Verified = 2, Who_changed_from_4_to_2 = ?, When_changed_from_4_to_2 = GETDATE()
            WHERE Key_value_for_database = ?
            """

        cursor.execute(
            query_to_update_from_4_to_2,
            (Who_changed_from_4_to_2, Key_value_for_database)
        )

        conn.commit()

        cursor.close()
        conn.close()



# Funkcja uruchamiana za pomocą przycisku "Error not valid"

    def change_4_to_3(self, Who_changed_from_4_to_3, Key_value_for_database):

        conn = self.get_connection()
        cursor = conn.cursor()

        query_to_update_from_4_to_3 = """
            UPDATE quality_check_database
            SET Verified = 3, Who_changed_from_4_to_3 = ?, When_changed_from_4_to_3 = GETDATE()
            WHERE Key_value_for_database = ?
            """

        cursor.execute(
            query_to_update_from_4_to_3,
            (Who_changed_from_4_to_3, Key_value_for_database)
        )

        conn.commit()

        cursor.close()
        conn.close()