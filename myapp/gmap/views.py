# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from gmap.worker import CityWorker
import json

def index(request):
    return render_to_response('gmap/index.html', {})

def route(request):
    return render_to_response('gmap/route.html', {})

def index_old(request):
    return HttpResponse("Hello, world.")

def search_city_ajax(request):
    lat = request.REQUEST.get("lat", None)
    lon = request.REQUEST.get("lon", None)
    print [lat, lon]

    try:
        lat = float(lat)
        lon = float(lon)
        closest_city = CityWorker().find_closest_city(latitude=lat, longitude=lon)
        msg = "Closest city to (%f,%f) is %s located at (%f,%f)"%( 
            lat,
            lon,
            closest_city.city,
            float(closest_city.latitude),
            float(closest_city.longitude)
            )

        closest_match = {
            'latitude': closest_city.latitude,
            'longitude': closest_city.longitude,
            'city_name': closest_city.city,
            }
        
        closest_match_json = json.dumps(closest_match)
        print closest_match_json

        # return HttpResponse(msg)
        return HttpResponse(closest_match_json, "text/html")
    except:
        return HttpResponse("Hello, world.")

import urllib
import json

def search_wikipedia_ajax(request):
    q = request.REQUEST.get("q", None)
    url = "http://en.wikipedia.org/w/api.php?action=query&titles=%s&format=json"%(
        q
        )
    f = urllib.urlopen(url)
    s = f.read()
    data = json.loads(s)
    print data
    entries = []
    for k, v in data['query']['pages'].items():
        title = v['title']
        pageid = v['pageid']
        entries.append("%s: %s"%(pageid, title))
    retval = ", ".join(entries)
    return HttpResponse(retval, "text/html")
    
    

    
