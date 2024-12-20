import pyodbc

def connect_to_db():
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=DESKTOP-B6BF8GB\\MSSQLSERVERS;'
            'DATABASE=MBA_app;'
            'Trusted_Connection=yes;'
        )
        print("Connection successful")
        return conn
    except pyodbc.Error as e:
        print("Error connecting to database:", e)
        return None

if __name__ == "__main__":
    conn = connect_to_db()
    if conn:
        # Do something with the connection
        pass
