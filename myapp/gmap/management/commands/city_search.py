from django.core.management.base import BaseCommand, CommandError
# from gmap.models import City
# import math
from gmap.worker import CityWorker

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'City Search'

    def handle(self, *args, **options):
        lat = 41.333
        lon = 76.833
        closest_city = CityWorker().find_closest_city(latitude=lat, longitude=lon)
        print "Closest city to (%f,%f) is %s located at (%f,%f)"%( 
            lat,
            lon,
            closest_city.city,
            float(closest_city.latitude),
            float(closest_city.longitude)
            )


