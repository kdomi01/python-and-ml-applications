import click
from datetime import datetime
from src.api import get_station_id, fetch_departures
from src.db import insert_station, insert_departure, db_setup

db_setup()

@click.group()
def cli():
    pass

@cli.command()
@click.argument("station_name")
@click.option("--limit", default=10, help="Number of departures to fetch")
def main(station_name, limit):
    station_id = get_station_id(station_name)
    if not station_id:
        click.echo("Station not found.")
        return

    departures = fetch_departures(station_id, limit=limit)
    if not departures.get("departures"):
        click.echo("No departures fetched.")
        return

    insert_station(station_id, station_name, datetime.now().isoformat())

    for dep in departures["departures"]:
        line = dep.get("line", {}).get("name")
        direction = dep.get("direction")
        planned = dep.get("plannedWhen")
        realtime = dep.get("when")
        delay = dep.get("delay", 0)

        insert_departure(
            station_id,
            line=line,
            direction=direction,
            planned_time=planned,
            realtime=realtime,
            delay=delay,
            fetched_at=datetime.now().isoformat()
        )

        status = f"+{delay} min delay" if delay else "on time"
        click.echo(f"{line} → {direction} | planned: {planned} | realtime: {realtime} | {status}")

    click.echo(f"\nInserted {len(departures['departures'])} departures.")

if __name__ == "__main__":
    cli()

