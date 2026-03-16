import sqlite3
from datetime import datetime
def add_session(subject, minutes):
    try:
        minutes = int(minutes)
    except:
        print("Invalid minutes value")
        return
    conn = sqlite3.connect("database/study.db")
    cursor = conn.cursor()
    minutes = int(minutes)
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO sessions (subject, minutes, date) VALUES (?, ?, ?)", (subject, minutes, date))
    conn.commit()
    conn.close()
def get_sessions():
    conn = sqlite3.connect("database/study.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sessions")
    sessions = cursor.fetchall()
    conn.close()
    return sessions
def get_total_minutes():
    conn = sqlite3.connect("database/study.db")
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(minutes) FROM sessions")
    total_minutes = cursor.fetchone()[0]
    conn.close()
    return total_minutes if total_minutes else 0
def get_subject_totals():
    conn = sqlite3.connect("database/study.db")
    cursor = conn.cursor()
    cursor.execute("SELECT subject, SUM(minutes) FROM sessions GROUP BY subject")
    data = cursor.fetchall()
    conn.close()
    return {subject: total for subject, total in data}
def delete_session(session_id):
    conn = sqlite3.connect("database/study.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM sessions WHERE id = ?", (session_id,))
    conn.commit()
    conn.close()
def get_recent_sessions(limit=5):
    conn = sqlite3.connect("database/study.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sessions ORDER BY date DESC LIMIT ?", (limit,))
    sessions = cursor.fetchall()
    conn.close()
    return sessions
def delete_sessions(session_ids):
    conn = sqlite3.connect("database/study.db")
    cursor = conn.cursor()
    cursor.executemany("DELETE FROM sessions WHERE id = ?", [(session_id,) for session_id in session_ids])
    conn.commit()
    conn.close()
def get_all_total_minutes():
    conn = sqlite3.connect("database/study.db")
    cursor = conn.cursor()
    cursor.execute("SELECT subject, SUM(minutes) FROM sessions GROUP BY subject")
    total = cursor.fetchone()[0]
    conn.close()
    if total is None:
        return 0
    return total