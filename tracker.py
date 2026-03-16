import sqlite3
from datetime import datetime


# Add a new study session to the database
def add_session(subject, minutes):

    # Validate minutes input
    try:
        minutes = int(minutes)
    except:
        print("Invalid minutes value")
        return

    # Connect to database
    conn = sqlite3.connect("database/study.db")
    cursor = conn.cursor()

    # Get current date and time
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Insert session record
    cursor.execute(
        "INSERT INTO sessions (subject, minutes, date) VALUES (?, ?, ?)",
        (subject, minutes, date)
    )

    conn.commit()
    conn.close()


# Retrieve all study sessions
def get_sessions():
    conn = sqlite3.connect("database/study.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM sessions")
    sessions = cursor.fetchall()

    conn.close()
    return sessions


# Calculate total minutes studied
def get_total_minutes():
    conn = sqlite3.connect("database/study.db")
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(minutes) FROM sessions")
    total_minutes = cursor.fetchone()[0]

    conn.close()

    # Return 0 if there are no records
    return total_minutes if total_minutes else 0


# Get total minutes studied per subject
def get_subject_totals():
    conn = sqlite3.connect("database/study.db")
    cursor = conn.cursor()

    cursor.execute("SELECT subject, SUM(minutes) FROM sessions GROUP BY subject")
    data = cursor.fetchall()

    conn.close()

    # Convert list of tuples into dictionary
    return {subject: total for subject, total in data}


# Delete a single study session by ID
def delete_session(session_id):
    conn = sqlite3.connect("database/study.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM sessions WHERE id = ?", (session_id,))

    conn.commit()
    conn.close()


# Get most recent study sessions
def get_recent_sessions(limit=5):
    conn = sqlite3.connect("database/study.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM sessions ORDER BY date DESC LIMIT ?", (limit,)
    )
    sessions = cursor.fetchall()

    conn.close()
    return sessions


# Delete multiple sessions at once
def delete_sessions(session_ids):
    conn = sqlite3.connect("database/study.db")
    cursor = conn.cursor()

    cursor.executemany(
        "DELETE FROM sessions WHERE id = ?",
        [(session_id,) for session_id in session_ids]
    )

    conn.commit()
    conn.close()


# Get total study minutes (alternative aggregation function)
def get_all_total_minutes():
    conn = sqlite3.connect("database/study.db")
    cursor = conn.cursor()

    cursor.execute("SELECT subject, SUM(minutes) FROM sessions GROUP BY subject")
    total = cursor.fetchone()[0]

    conn.close()

    if total is None:
        return 0
    return total
