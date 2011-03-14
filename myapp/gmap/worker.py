import math
from gmap.models import City
class CityWorker:
    def distance(self, city=None, latitude=None, longitude=None):
        if city is None or latitude is None or longitude is None:
            return None

        c_lat = float(city.latitude)
        c_lon = float(city.longitude)

        diff_lat = latitude - c_lat
        diff_lon = longitude - c_lon
        distance = math.sqrt(diff_lat*diff_lat + diff_lon*diff_lon)

        return distance

    def find_closest_city(self, latitude=None, longitude=None):
        lat = latitude
        lon = longitude

        cities = City.objects.all()

        city = cities[0]
        min_distance = self.distance(city=city, latitude=lat, longitude=lon)

        closest_city = city
        
        for city in cities[0:]:
            d = self.distance( city, latitude=lat, longitude=lon)
            if d < min_distance:
                min_distance = d
                print min_distance, city.city
                closest_city = city

        return closest_city

