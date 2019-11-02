import json
import time
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

with open('LocationHistory.json', 'r') as fh:
    raw = json.loads(fh.read())

# use location_data as an abbreviation for location data
location_data = pd.DataFrame(raw['locations'])
del raw #free up some memory

# convert to typical units
location_data['latitudeE7'] = location_data['latitudeE7']/float(1e7) 
location_data['longitudeE7'] = location_data['longitudeE7']/float(1e7)
location_data['timestampMs'] = location_data['timestampMs'].map(lambda x: float(x)/1000) #to seconds
location_data['datetime'] = location_data.timestampMs.map(datetime.datetime.fromtimestamp)

# Rename fields based on the conversions we just did
location_data.rename(columns={'latitudeE7':'latitude', 'longitudeE7':'longitude', 'timestampMs':'timestamp'}, inplace=True)
location_data = location_data[location_data.accuracy < 1000] #Ignore locations with accuracy estimates over 1000m
location_data.reset_index(drop=True, inplace=True)

print(location_data.head())

# Convert lat-longs to address



# Only save most prominent location every day
groups = location_data.groupby(['latitude', 'longitude']).size()

#lon_by_day = day_groups['longitude'].agg(lambda x:x.value_counts().index[0])
#lat_by_day = day_groups['latitude'].agg(lambda x:x.value_counts().index[0])

print(groups.head(20))
print(groups.shape)
print(location_data.shape)
