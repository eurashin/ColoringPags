import googlemaps
import numpy as np
import yaml
from googleplaces import GooglePlaces
from os.path import dirname, abspath, join
import cv2
from PIL import Image


parent_path = abspath(dirname(dirname(__file__)))
file_name = abspath(join(parent_path, 'config.yaml'))

# Load config.yaml, which contains the API key
with open(file_name) as yaml_file:
    cfg = yaml.load(yaml_file)


API_KEY = cfg['google_api']['key']


def format_loc(coord):
    d = dict([
        ('lat', coord[0]),
        ('lng', coord[1])])
    return d

def imageSearch(coords):
    radius = 25
    counter = 0

    gmaps = googlemaps.Client(key=API_KEY)
    gplaces = GooglePlaces(API_KEY)

    paths = []

    for coord in coords:
        place = format_loc(coord)
        nearby = gplaces.nearby_search(  # call to Google Places API
                    lat_lng=place,
                    radius=radius,  # radius is in m
                    )

        if len(nearby.places) != 0:
            for loc in nearby.places:
                if len(loc.photos) != 0:
                    photo = loc.photos[0]
                    photo.get(maxheight=5000, maxwidth=5000)
                    fname = 'static/result' + str(counter)+ '.jpg'
                    f = open(fname, 'wb')
                    f.write(photo.data)
                    f.close()
                    paths.append(fname)
                    counter += 1
                    break

    return paths
