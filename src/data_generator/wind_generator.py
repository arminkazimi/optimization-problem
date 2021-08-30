from meteostat import Point, Daily
from datetime import datetime, timedelta, time, date


class WindGenerator:
    def __init__(self, from_date, to_date, lat, long, resolution):
        self.from_date = datetime.strptime(from_date, '%Y-%m-%d')
        self.to_date = datetime.strptime(to_date, '%Y-%m-%d')
        self.lat = lat
        self.long = long
        self.resolution = resolution

    def generator(self):
        location_point = Point(lat=self.lat, lon=self.long)

        data = Daily(location_point, self.from_date, self.to_date)
        data = data.fetch()
        return data
