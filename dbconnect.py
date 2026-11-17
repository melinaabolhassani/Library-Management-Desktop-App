import pyodbc

def connect_db():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=LAPTOP-7U8Q1LEO\\MSSQLSERVER2;"
        "DATABASE=dblibrary;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )
    return conn

if __name__ == "__main__":
    conn = connect_db()
    print("Connected successfully!")
    conn.close()