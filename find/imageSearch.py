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
    """
    Formats a coordinate pair from the list of stepping stones
    :param coord: valid lat, long pair
    :return: dictionary representing the coordinate
    """
    d = dict([
        ('lat', coord[0]),
        ('lng', coord[1])])
    return d

def imageSearch(coord):
    radius = 25

    gmaps = googlemaps.Client(key=API_KEY)
    gplaces = GooglePlaces(API_KEY)

    place = format_loc(coord)
    result = []

    nearby = gplaces.nearby_search(  # call to Google Places API
                lat_lng=place,
                radius=radius,  # radius is in m
                )

    if len(nearby.places) == 0:
        raise Exception('no nearby')
    for loc in nearby.places:
        if len(loc.photos) != 0:
            photo = loc.photos[0]
            photo.get(maxheight=5000, maxwidth=5000)
            f = open('result.jpg', 'wb')
            f.write(photo.data)
            f.close()
            print('done')
            break
