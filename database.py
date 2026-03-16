import sqlite3


# Function to connect to the SQLite database and create table if it doesn't exist
def connect_db():

    # Connect to database file
    conn = sqlite3.connect("database/study.db")

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Create sessions table for storing study records
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sessions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject TEXT,
        minutes INTEGER,
        date TEXT
    )
    """)

    # Save changes to database
    conn.commit()

    # Close the database connection
    conn.close()
