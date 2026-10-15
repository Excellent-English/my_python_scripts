import pyodbc

class Database_QC:

# funkcja nawiązująca połączenie z tabelową sqlową
    def get_connection(self):
        return pyodbc.connect(
            """
            Driver={ODBC Driver 18 for SQL Server};
            Server=tcp:sscciq.database.windows.net,1433;
            Database=SSC CIQ;
            Authentication=ActiveDirectoryInteractive;
            """
        )

# 3 funkcje, które są uruchamiane po kliknięciu na "Save & next" button

    def change_1_to_2(self, Who_changed_from_1_to_2_or_3, Controls_column, First_comment, Key_value_for_database):

        conn = self.get_connection()
        cursor = conn.cursor()

        query_to_update_from_1_to_2 = """
            UPDATE quality_check_database
            SET Verified = 2, Who_changed_from_1_to_2_or_3 = ?, When_changed_from_1_to_2_or_3 = GETDATE(), Controls = ?, First_comment = ?
            WHERE Key_value_for_database = ?
            """

        cursor.execute(
            query_to_update_from_1_to_2,
            (Who_changed_from_1_to_2_or_3, Controls_column, First_comment, Key_value_for_database)
        )

        conn.commit()

        cursor.close()
        conn.close()


    def change_1_to_3(self, Who_changed_from_1_to_2_or_3, Controls_column, First_comment, Key_value_for_database):

        conn = self.get_connection()
        cursor = conn.cursor()

        query_to_update_from_1_to_3 = """
            UPDATE quality_check_database
            SET Verified = 3, Who_changed_from_1_to_2_or_3 = ?, When_changed_from_1_to_2_or_3 = GETDATE(), Controls = ?, First_comment = ?
            WHERE Key_value_for_database = ?
            """

        cursor.execute(
            query_to_update_from_1_to_3,
            (Who_changed_from_1_to_2_or_3, Controls_column, First_comment, Key_value_for_database)
        )

        conn.commit()

        cursor.close()
        conn.close()


    def change_2_to_4(self, Who_changed_from_2_to_4, First_comment, Second_comment, Key_value_for_database):

        conn = self.get_connection()
        cursor = conn.cursor()

        query_to_update_from_2_to_4 = """
            UPDATE quality_check_database
            SET Verified = 4, Who_changed_from_2_to_4 = ?, When_changed_from_2_to_4 = GETDATE(), First_comment = ?, Second_comment = ?
            WHERE Key_value_for_database = ?
            """

        cursor.execute(
            query_to_update_from_2_to_4,
            (Who_changed_from_2_to_4, First_comment, Second_comment, Key_value_for_database)
        )

        conn.commit()

        cursor.close()
        conn.close()


    def change_4_to_5(self, Who_changed_from_4_to_5, First_comment, Second_comment, Key_value_for_database):

        conn = self.get_connection()
        cursor = conn.cursor()

        query_to_update_from_4_to_5 = """
            UPDATE quality_check_database
            SET Verified = 5, Who_changed_from_4_to_5 = ?, When_changed_from_4_to_5 = GETDATE(), First_comment = ?, Second_comment = ?
            WHERE Key_value_for_database = ?
            """

        cursor.execute(
            query_to_update_from_4_to_5,
            (Who_changed_from_4_to_5, First_comment, Second_comment, Key_value_for_database)
        )

        conn.commit()

        cursor.close()
        conn.close()


# Funkcja uruchamiana za pomocą przycisku "Reject"

    def change_4_to_2(self, Who_changed_from_4_to_2, First_comment, Second_comment, Key_value_for_database):

        conn = self.get_connection()
        cursor = conn.cursor()

        query_to_update_from_4_to_2 = """
            UPDATE quality_check_database
            SET Verified = 2, Who_changed_from_4_to_2 = ?, When_changed_from_4_to_2 = GETDATE(), First_comment = ?, Second_comment = ?
            WHERE Key_value_for_database = ?
            """

        cursor.execute(
            query_to_update_from_4_to_2,
            (Who_changed_from_4_to_2, First_comment, Second_comment, Key_value_for_database)
        )

        conn.commit()

        cursor.close()
        conn.close()



# Funkcja uruchamiana za pomocą przycisku "Error not valid"

    def change_4_to_3(self, Who_changed_from_4_to_3, First_comment, Second_comment, Key_value_for_database):

        conn = self.get_connection()
        cursor = conn.cursor()

        query_to_update_from_4_to_3 = """
            UPDATE quality_check_database
            SET Verified = 3, Who_changed_from_4_to_3 = ?, When_changed_from_4_to_3 = GETDATE(), First_comment = ?, Second_comment = ?
            WHERE Key_value_for_database = ?
            """

        cursor.execute(
            query_to_update_from_4_to_3,
            (Who_changed_from_4_to_3, First_comment, Second_comment, Key_value_for_database)
        )

        conn.commit()

        cursor.close()
        conn.close()


# ------------------------------------------------------------------------------------------------------------------------------------------------

# funkcja wysyłająca flagę "Yes" do itemu, który aktualnie jest przeglądany

    def block_selected_item(self, Key_value_for_database):
        conn = self.get_connection()
        cursor = conn.cursor()

        query_to_block_item = """
            UPDATE quality_check_database
            SET Item_blocked = 'Yes'
            WHERE Key_value_for_database = ?
            """

        cursor.execute(
            query_to_block_item,
            (Key_value_for_database,)
        )

        conn.commit()

        cursor.close()
        conn.close()


# funkcja odwołująca flagę "Yes" do itemu, który aktualnie jest przeglądany

    def unblock_selected_item(self, Key_value_for_database):
        conn = self.get_connection()
        cursor = conn.cursor()

        query_to_unblock_item = """
                UPDATE quality_check_database
                SET Item_blocked = Null
                WHERE Key_value_for_database = ?
                """

        cursor.execute(
            query_to_unblock_item,
            (Key_value_for_database,)
        )

        conn.commit()

        cursor.close()
        conn.close()