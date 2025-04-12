import sqlite3
from datetime import datetime

DB_PATH = "./appData/rsvp_data.db"

def init_db():
    """Initialize the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rsvp (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            guest_name TEXT NOT NULL,
            guest_count INTEGER NOT NULL,
            register_time TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insert_rsvp(guest_name, guest_count):
    """Insert RSVP data into the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    register_time = datetime.utcnow().isoformat()  # Get current UTC time
    cursor.execute("""
        INSERT INTO rsvp (guest_name, guest_count, register_time)
        VALUES (?, ?, ?)
    """, (guest_name, guest_count, register_time))
    conn.commit()
    conn.close()
