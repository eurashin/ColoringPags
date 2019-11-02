import tools 
import datetime

df = tools.parse_location_data('LocationHistory.json')
start = datetime.datetime(2019,7, 1).date()
end = datetime.datetime(2019, 7, 30).date()
time = tools.extract_time_period(df, start, end)
print(time.shape)
