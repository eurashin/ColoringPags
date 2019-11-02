import json
import time
import datetime
import numpy as np
import pandas as pd
import geopy.distance
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans 

NUMBER_OF_PAGES = 10
MINUTES_TO_QUALIFY = 30

def parse_location_data(filename): 
    with open(filename, 'r') as fh:
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

    return(location_data)


def extract_time_period(df, start_date, end_date):
    mask = (df['datetime'].dt.date > start_date) & (df['datetime'].dt.date <= end_date)
    df_time = df.loc[mask]
    
    # Which lat-lon did we spend enough time at to qualify as a place?
    coord_groups = df_time.groupby(['latitude', 'longitude'])
    durations = coord_groups['datetime'].max() - coord_groups['datetime'].min()
    duration_coords =  durations[durations > datetime.timedelta(minutes=MINUTES_TO_QUALIFY)].index.values
    place_coords = np.array(np.ndarray.tolist(duration_coords))

    plt.scatter(place_coords[:,0], place_coords[:,1])
    
    # Cluster the images
    k=NUMBER_OF_PAGES
    if(place_coords.shape[0] < NUMBER_OF_PAGES):
        k = place_coords.shape[0]
    KM = KMeans(n_clusters = k, max_iter = 500) 
    KM.fit(place_coords)
    centers = KM.cluster_centers_
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5);
    
    return(centers)
    

