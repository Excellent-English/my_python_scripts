import pyodbc
import pandas as pd

conn = pyodbc.connect(
    """
    Driver={ODBC Driver 17 for SQL Server};
    Server=tcp:sscciq.database.windows.net,1433;
    Database=SSC CIQ;
    Trusted_Connection=no;
    Authentication=ActiveDirectoryInteractive;
    UID=piotr.szczubiala@fresenius-kabi.com;
    """)

df = pd.read_sql_query("SELECT * FROM quality_check_database",conn)
print(f"Number of items: {len(df)}")
conn.close()