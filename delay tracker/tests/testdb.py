import sqlite3
import pytest
from src.db import db_setup, insert_station, insert_departure, db_name

@pytest.fixture(scope="module", autouse=True)
def setup_db():
    db_setup()
    yield
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("DELETE FROM departures")
    c.execute("DELETE FROM stations")
    conn.commit()
    conn.close()

def test_insert_station():
    insert_station("test_id", "Test Station", "2025-08-19T14:00:00")
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT * FROM stations WHERE id = ?", ("test_id",))
    row = c.fetchone()
    conn.close()
    assert row[0] == "test_id"
    assert row[1] == "Test Station"

def test_insert_departure():
    insert_departure("test_id", "U1", "North", "2025-08-19T14:05", "2025-08-19T14:06", 60, "2025-08-19T14:07")
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT * FROM departures WHERE station_id = ?", ("test_id",))
    row = c.fetchone()
    conn.close()
    assert row[1] == "test_id"
    assert row[2] == "U1"
    assert row[3] == "North"

