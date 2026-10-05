import sqlite3
import pyodbc
import pandas as pd

class Database_Admin:

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

# funkcja wyciągająca w formie listy wszystkie kraje
    def get_countries(self):
        conn = self.get_connection()

        query = """
            SELECT DISTINCT Country
            FROM quality_check_database
            WHERE Country IS NOT NULL
            ORDER BY Country
            """

        df = pd.read_sql_query(query, conn)
        return df["Country"].tolist()


# funkcja wyciągająca Monthly_posted_documents, Amount_limit oraz New_hire_percentage z tabeli
    def get_limits_based_on_selected_country_and_company_code(self, country, company_code):
        conn = self.get_connection()

        results = pd.read_sql_query(
            """
            SELECT Monthly_posted_documents, Amount_Limit, New_hire_percentage
            FROM quality_check_limits
            WHERE Country = ? AND Company_code = ? AND Line_status = 'Active'
            """,
        conn,
            params=[country, company_code]
        )
        return [
            {
                "monthly_posted_documents": row["Monthly_posted_documents"],
                "amount_limit": row["Amount_Limit"],
                "new_hire_percentage": row["New_hire_percentage"]
            }
            for _, row in results.iterrows()
        ]


    # funkcja wyciągająca w formie listy wszystkie kraje
    def get_countries_limits(self):
        conn = self.get_connection()

        query = """
            SELECT DISTINCT Country
            FROM quality_check_limits
            WHERE Country IS NOT NULL AND Line_status = 'Active'
            ORDER BY Country
            """

        df = pd.read_sql_query(query, conn)

        return df["Country"].tolist()


    # funkcja wyciągająca w formie listy wszystkie company cody
    def get_company_codes_limits(self, country):

        if not country:
            return []

        conn = self.get_connection()

        query = """
            SELECT DISTINCT Company_code
            FROM quality_check_limits
            WHERE Country = ?
            ORDER BY Company_code
            """

        df = pd.read_sql_query(
            query,
            conn,
            params=[country]
        )

        return df["Company_code"].tolist()


# -----------------------------------------------------------------------------------------------------------------------
# PEOPLE MANAGEMENT
# -----------------------------------------------------------------------------------------------------------------------

# funkcja umieszczona w people management - top right
# funkcja sprawdzająca, czy wpisany w aplikacji użytkownik istnieje w tabeli users

    def check_if_user_exists(self, typed_email_address_top_right):

        conn = self.get_connection()
        query = """
            SELECT Email_address from quality_check_users
            WHERE Email_address = ?
            """

        df = pd.read_sql_query(
            query,
            conn,
            params=[typed_email_address_top_right]
        )

        conn.close()
        return not df.empty


# ----------------------------------------------
# middle left
# ----------------------------------------------

# funkcja umieszczona w people management - middle left
# funkcja sprawdzająca czy wybrany użytkownik jest adminem

    def is_selected_employee_admin(self, typed_email_address_middle_left):

        conn = self.get_connection()
        query = """
            SELECT Admin_role from quality_check_users
            WHERE Email_address = ? AND Admin_role = 'Admin'
            """

        df = pd.read_sql_query(
            query,
            conn,
            params=[typed_email_address_middle_left]
        )

        conn.close()
        return not df.empty


# funkcja umieszczona w people management - middle left
# funkcja wyciągająca SAP ID użytkownika na podstawie wpisanego w aplikacji adresu mailowego


    def sap_id_for_selected_employee(self, typed_email_address_middle_left):

        conn = self.get_connection()

        query = """
                SELECT SAP_user from quality_check_users
                WHERE Email_address = ?
                """

        df = pd.read_sql_query(
            query,
            conn,
            params=[typed_email_address_middle_left]
        )

        conn.close()

        if df.empty:
            return None
        sap_id_of_selected_person = df.iloc[0]["SAP_user"]
        return sap_id_of_selected_person


# funkcja umieszczona w people management - middle left
# funkcja sprawdzająca czy wybrany użytkownik jest widoczny w tabeli new_joiners jako Active

    def is_selected_employee_new_joiner(self, sap_id):

        conn = self.get_connection()
        query = """
            SELECT New_joiner from quality_check_new_joiners
            WHERE New_joiner = ? AND Line_status = 'Active'
            """

        df = pd.read_sql_query(
            query,
            conn,
            params=[sap_id]
        )

        return df["New_joiner"].tolist()


# funkcja umieszczona w people management - middle left
# funkcja nadająca użytkownikowi dostęp admina

    def grant_admin_access(self, sap_id, who_changed, typed_email_address):

        conn = self.get_connection()
        cursor = conn.cursor()

        try:

            script_to_deactivate_row = """
                    UPDATE quality_check_users
                    SET Active_to = GETDATE(), Who_changed = ?
                    WHERE Email_address = ? AND Active_to IS NULL
                    """

            script_to_insert_row = """
                INSERT INTO quality_check_users
                (
                    SAP_user,
                    Email_address,
                    Admin_role,
                    Who_changed,
                    Active_from
                )
                VALUES
                (
                    ?,
                    ?,
                    'admin',
                    ?,
                    GETDATE()
                );
                """

            cursor.execute(
                script_to_deactivate_row,
                who_changed,
                typed_email_address
            )

            cursor.execute(
                script_to_insert_row,
                sap_id,
                typed_email_address,
                who_changed
            )

            conn.commit()

        except Exception:
            conn.rollback()
            raise
        finally:
            cursor.close()
            conn.close()

# funkcja umieszczona w people management - middle left
# funkcja zabierająca użytkownikowi dostęp admina

    def revoke_admin_access(self, who_changed, typed_email_address):

        conn = self.get_connection()
        cursor = conn.cursor()

        script_to_update_row = """
            UPDATE quality_check_users
            SET Admin_role = NULL, Active_to = GETDATE(), Who_changed = ?
            WHERE Email_address = ? AND Active_to IS NULL
        """

        cursor.execute(
            script_to_update_row,
            who_changed,
            typed_email_address
        )

        conn.commit()

        cursor.close()
        conn.close()


# funkcja umieszczona w people management - middle left
# funkcja wyciągająca listę krajów, w których wpisany użytkownik jest widoczny jako new joiner

    def where_user_is_added_as_new_joiner(self, sap_id):

        conn = self.get_connection()
        query = """
                SELECT Country from quality_check_new_joiners
                WHERE New_joiner = ? AND Line_status = 'Active'
                """

        df = pd.read_sql_query(
            query,
            conn,
            params=[sap_id]
        )

        print(df["Country"].tolist())
        return df["Country"].tolist()


# funkcja umieszczona w people management - middle left
# funkcja wyciągająca listę krajów, w których nie ma wpisanego użytkownika jako new joiner

    def get_countries_not_assigned_to_user(self, sap_id):

        conn = self.get_connection()
        query = """
        SELECT DISTINCT Country
        FROM quality_check_new_joiners
        WHERE Country NOT IN (
            SELECT Country
            FROM quality_check_new_joiners
            WHERE New_joiner = ? AND Line_status = 'Active'
        )
        ORDER BY Country;
        """

        df = pd.read_sql_query(
            query,
            conn,
            params=[sap_id]
        )
        conn.close()

        print(df["Country"].tolist())
        return df["Country"].tolist()



# funkcja umieszczona w people management - middle left
# funkcja dodająca nowy rekord do tabeli new joiners

    def add_new_user_as_new_joiner(self, country, sap_id, who_changed):

        conn = self.get_connection()
        cursor = conn.cursor()

        script_to_insert_new_row = """
        INSERT INTO quality_check_new_joiners
        (
            Country,
            New_joiner,
            Line_status,
            Who_changed,
            Active_from
        )
        VALUES
        (
            ?,
            ?,
            'Active',
            ?,
            GETDATE()
        );
        """

        cursor.execute(
            script_to_insert_new_row,
            country,
            sap_id,
            who_changed
        )
        conn.commit()

        cursor.close()
        conn.close()


# funkcja umieszczona w people management - middle left
# funkcja wyłączająca rolę new joinera dla wybranego usera i wybranego kraju

    def deactivate_new_joiner_from_certain_country(self, who_changed, sap_id, country):

        conn = self.get_connection()
        cursor = conn.cursor()

        script_to_update_row = """
                UPDATE quality_check_new_joiners
                SET Line_status = 'Inactive', Who_changed = ?, Active_to = GETDATE()
                WHERE New_joiner = ? AND Country = ? AND Line_status = 'Active'
                """

        cursor.execute(
            script_to_update_row,
            who_changed,
            sap_id,
            country
        )
        conn.commit()

        cursor.close()
        conn.close()



# funkcja umieszczona w people management - middle right
# funkcja dodająca nowego użytkownika do tabeli users

    def create_user_if_does_not_exist_new_line(self, sap_user, email_address, admin_role, who_changed):

        conn = self.get_connection()
        cursor = conn.cursor()

        script_to_insert_new_row = """
        INSERT INTO quality_check_users
        (
            SAP_user,
            Email_address,
            Admin_role,
            Active_from,
            Who_changed
        )
        VALUES
        (
            ?,
            ?,
            ?,
            GETDATE(),
            ?
        );
        """

        cursor.execute(
            script_to_insert_new_row,
            sap_user,
            email_address,
            admin_role,
            who_changed
        )
        conn.commit()

        cursor.close()
        conn.close()


# funkcja umieszczona w people management - middle right
# gdy user jest dodawany do tabeli users, z automatu puszczana jest funkcja dodająca go do tabeli new joiners (kiedy w aplikacji wybrane jest "Yes" przy "New joiner?"

    def create_user_if_does_not_exist_as_new_joiner(self, country, sap_id, who_changed):

        conn = self.get_connection()
        cursor = conn.cursor()

        script_to_insert_new_row = """
            INSERT INTO quality_check_new_joiners
            (
                Country,
                New_joiner,
                Line_status,
                Who_changed,
                Active_from
            )
            VALUES
            (
                ?,
                ?,
                'Active',
                ?,
                GETDATE()
            );
            """

        cursor.execute(
            script_to_insert_new_row,
            country,
            sap_id,
            who_changed
        )
        conn.commit()

        cursor.close()
        conn.close()


# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------

# funkcja umieszczona w people management
# funkcja wyciągająca w formie listy wszystkie company cody
    def get_users_who_posted_but_are_not_visible(self):

        conn = self.get_connection()
        query = """
            SELECT DISTINCT qcd.User_name
            FROM dbo.quality_check_database qcd
            LEFT JOIN dbo.quality_check_users qcu
                ON qcd.User_name = qcu.SAP_user
            WHERE qcu.SAP_user IS NULL AND qcd.User_name IS NOT NULL;
            """

        df = pd.read_sql_query(
            query,
            conn
        )

        return df["User_name"].tolist()


# funkcja umieszczona w people management - bottom left
# funkcja wprowadzająca nowego usera do tabeli users, który wcześniej postował faktury

    def create_user_who_posted_invoices(self, selected_sap_id, typed_email_address):

        conn = self.get_connection()
        cursor = conn.cursor()

        script_to_insert_new_row = """
                INSERT INTO quality_check_users
                (
                    SAP_user,
                    Email_address,
                    Active_from
                )
                VALUES
                (
                    ?,
                    ?,
                    GETDATE()
                );
                """

        cursor.execute(
            script_to_insert_new_row,
            typed_email_address,
            selected_sap_id
        )
        conn.commit()

        cursor.close()
        conn.close()


# funkcja umieszczona w people management - bottom right
# funkcja wyciągająca w formie listy wszystkie company cody
    def get_users_from_users_with_no_email(self):

        conn = self.get_connection()
        query = """
            SELECT SAP_user from quality_check_users
            WHERE Email_address IS NULL AND Active_to IS NULL
            """

        df = pd.read_sql_query(
            query,
            conn
        )

        return df["SAP_user"].tolist()


# funkcja umieszczona w people management - bottom right
# funkcja wprowadzająca adres mailowy dla usera o podanym SAP ID

    def update_user_with_sap_id_but_no_email(self, selected_sap_id, typed_email_address):

        conn = self.get_connection()
        cursor = conn.cursor()

        script_to_update_row = """
                UPDATE quality_check_users
                SET Email_address = ?
                WHERE SAP_user = ?
                """

        cursor.execute(
            script_to_update_row,
            typed_email_address,
            selected_sap_id
        )
        conn.commit()

        cursor.close()
        conn.close()





# -----------------------------------------------------------------------------------------------------------------------
# LIMIT MANAGEMENT
# -----------------------------------------------------------------------------------------------------------------------

# funkcja umieszczona w limit management
# funkcja zmieniająca limity w wyszukanym wcześniej country i company codzie + dodaje nowy wiersz w tabeli

    def update_row_with_limits(self, logged_user, country, company_code,
                               new_monthly_posted_documents, new_amount_limit, new_new_hire_percentage):

        conn = self.get_connection()
        cursor = conn.cursor()


        script_to_deactivate_row = """
        UPDATE quality_check_limits
        SET
            Line_status = 'Inactive',
            Who_changed = ?,
            Active_to = GETDATE()
        WHERE Country = ? AND Company_code = ? AND Line_status = 'Active';
        """


        script_to_insert_new_row = """
        INSERT INTO quality_check_limits
        (
            Country,
            Company_code,
            Monthly_posted_documents,
            Amount_limit,
            New_hire_percentage,
            Line_status,
            Who_changed,
            Active_from,
            Active_to
        )
        VALUES
        (
            ?,
            ?,
            ?,
            ?,
            ?,
            'Active',
            ?,
            GETDATE(),
            NULL
        );
        """

        cursor.execute(
            script_to_deactivate_row,
            logged_user,
            country,
            company_code
        )

        cursor.execute(
            script_to_insert_new_row,
            country,
            company_code,
            new_monthly_posted_documents,
            new_amount_limit,
            new_new_hire_percentage,
            logged_user
        )
        conn.commit()

        cursor.close()
        conn.close()




# funkcja umieszczona w limit management
# funkcja tworząca nowy kraj z wartościami

    def create_new_country_and_company_code(self, logged_user, country, company_code,
                               new_monthly_posted_documents, new_amount_limit, new_new_hire_percentage):

        conn = self.get_connection()
        cursor = conn.cursor()

        script_to_insert_new_row = """
            INSERT INTO quality_check_limits
            (
                Country,
                Company_code,
                Monthly_posted_documents,
                Amount_limit,
                New_hire_percentage,
                Line_status,
                Who_changed,
                Active_from,
                Active_to
            )
            VALUES
            (
                ?,
                ?,
                ?,
                ?,
                ?,
                'Active',
                ?,
                GETDATE(),
                NULL
            );
            """

        cursor.execute(


        script_to_insert_new_row,
        country,
        company_code,
        new_monthly_posted_documents,
        new_amount_limit,
        new_new_hire_percentage,
        logged_user
        )
        conn.commit()

        cursor.close()
        conn.close()