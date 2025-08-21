import requests
from config import url

def fetch_departures(station, limit=10):
    try:
        departure_url = f"{url}/stops/{station}/departures?duration={limit}"
        response = requests.get(departure_url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("API Error:", e)
        return {}

def get_station_id(name):
    try:
        station_url = f"{url}/locations?query={name}&poi=false&addresses=false"
        response = requests.get(station_url)
        response.raise_for_status()
        data = response.json()
        if not data:
            raise ValueError(f"No station id found for {name}")
        return data[0]["id"]
    except Exception as e:
        print("API Error (station search):", e)
        return None

