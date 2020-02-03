# Copyright SuliHu sulihu@bu.edu 2020
import requests
from datetime import datetime, timedelta
import pandas as pd


class AirportWeather:
    def __init__(self, iata, duration):
        self.iata = iata
        self.duration = duration
        self.name, self.icao, self.lat, self.lon = self._lookup_airport()
        self.histories = self._get_weather()

    def _lookup_airport(self):
        name, lat, lon = None, None, None
        df = pd.read_csv('data.csv')
        for _, row in df.iterrows():
            if row['iata_code'] == self.iata:
                name = row['name']
                lat = float(row['latitude_deg'])
                lon = float(row['longitude_deg'])
                icao = row['gps_code']
                break
        return name, icao, lat, lon

    def _construct_weather(self, observation):
        properties = observation['properties']
        timestamp = properties['timestamp']
        weather = {}
        weather['description'] = properties['textDescription']
        weather['temperature'] = properties['temperature']['value']
        weather['visibility'] = properties['visibility']['value']
        return timestamp, weather

    def _get_time_diff_by_now(self, time):
        now = datetime.utcnow()
        time = datetime.strptime(time[:19], '%Y-%m-%dT%H:%M:%S')
        return now - time

    def _get_weather(self):
        query = f'https://api.weather.gov/stations/{self.icao}/observations'
        res = requests.get(query)
        res.raise_for_status()
        observations = res.json()['features']
        histories = []
        for observation in observations:
            if self._get_time_diff_by_now(
                observation['properties']['timestamp']) \
             < timedelta(hours=self.duration):
                weather = self._construct_weather(observation)
                histories.append(weather)
            else:
                break
        return histories

    def print_weather(self):
        try:
            for weather in self.histories:
                print(weather[0])
                print(
                    f"{weather[1]['description']:<20}\t"
                    f"Temperature: {round(weather[1]['temperature'],1):>4} C\t"
                    f"Visibility: {weather[1]['visibility']:>8} m")
            return('Report End')
        except Exception:
            return('Report Failed')


def main():
    iata = input('Please enter the IATA code: ').upper()
    duration = int(input('PLesese enter the time period in hours: '))
    aw = AirportWeather(iata, duration)
    aw.print_weather()


if __name__ == '__main__':
    main()
