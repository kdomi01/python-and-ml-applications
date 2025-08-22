# Departure Tracker CLI

A command-line interface (CLI) to fetch and store real-time public transport departures using the BVG API.  
This project demonstrates a small end-to-end pipeline: API requests → SQLite database → CLI output.

---

## Features

- Fetch upcoming departures for a given station.
- Store station and departure data in a local SQLite database.
- Display departure details including line, direction, planned and real-time schedules, and delay.
- Simple, extensible Python project structure.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/delay-tracker-cli.git
cd delay-tracker-cli
```
2. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
# On Linux/macOS
source .venv/bin/activate
# On Windows
.venv\Scripts\activate
pip install -r requirements.txt
```

## Project Structure
```pgsql
delay-tracker-cli/
│
├── src/
│   ├── api.py          # Functions to interact with the BVG API
│   ├── db.py           # SQLite database setup and insert functions
│   ├── app.py          # CLI entry point using Click
│   └── config.py       # Configuration (API URL, DB name)
│
├── tests/
│   ├── test_db.py      # Unit tests for database functions
│   └── test_api.py     # Unit tests for API functions
│
├── requirements.txt
└── README.md
```

## Usage
Run the CLI:
```bash
python src/app.py main "Station Name" --limit 10
```
Example:
```bash
python src/app.py main "Alexanderplatz" --limit 5
```
Station Name → Name of the station to fetch departures for.

--limit → Number of upcoming departures to retrieve (default: 10).

## Database
SQLite database: bvg.db

Two tables:
1. stations → stores station ID, name, and last seen timestamp.
2. departures → stores line, direction, planned/realtime times, delay, and fetch timestamp.

## Testing
Run unit tests using pytest:
```bash
pytest tests/
```
Tests include:

1. Database insert functions (insert_station, insert_departure).
2. API interaction functions (get_station_id, fetch_departures) with mocking to ensure deterministic behavior.

## Notes
Designed for demonstration purposes; focuses on API integration, CLI, and database operations.

The project emphasizes clean structure, modularity, and testability.

