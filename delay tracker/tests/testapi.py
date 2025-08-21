import pytest
from unittest.mock import patch
from src.api import get_station_id, fetch_departures

def test_get_station_id_success():
    mock_response = [{"id": "12345", "name": "MockStation"}]
    with patch("requests.get") as mocked_get:
        mocked_get.return_value.json.return_value = mock_response
        mocked_get.return_value.raise_for_status = lambda: None
        station_id = get_station_id("MockStation")
        assert station_id == "12345"

def test_fetch_departures_success():
    mock_response = {"departures": [{"line": {"name": "U1"}, "direction": "North"}]}
    with patch("requests.get") as mocked_get:
        mocked_get.return_value.json.return_value = mock_response
        mocked_get.return_value.raise_for_status = lambda: None
        departures = fetch_departures("12345", limit=1)
        assert "departures" in departures