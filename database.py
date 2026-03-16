import sqlite3

def connect_db():
    conn = sqlite3.connect("database/study.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sessions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject TEXT,
        minutes INTEGER,
        date TEXT
    )
    """)
    conn.commit()
    conn.close()