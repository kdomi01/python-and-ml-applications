import sqlite3
from config import db_name

def db_setup():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS stations (
            id TEXT PRIMARY KEY,
            name TEXT,
            latest_seen_utc TEXT
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS departures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            station_id TEXT,
            line TEXT,
            direction TEXT,
            planned_time_utc TEXT,
            realtime_utc TEXT,
            delay_seconds INTEGER,
            fetched_at TEXT,
            FOREIGN KEY(station_id) REFERENCES stations(id)
        )
    """)
    c.execute("""
        CREATE INDEX IF NOT EXISTS idx_dep_station
        ON departures(station_id, realtime_utc)
    """)
    conn.commit()
    conn.close()

def insert_station(station_id, name, latest_seen_utc):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute(
        "INSERT OR REPLACE INTO stations (id, name, latest_seen_utc) VALUES (?, ?, ?)",
        (station_id, name, latest_seen_utc)
    )
    conn.commit()
    conn.close()

def insert_departure(station_id, line, direction, planned_time, realtime, delay, fetched_at):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("""
        INSERT INTO departures
        (station_id, line, direction, planned_time_utc, realtime_utc, delay_seconds, fetched_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (station_id, line, direction, planned_time, realtime, delay, fetched_at))
    conn.commit()
    conn.close()
