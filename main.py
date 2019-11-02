import tools
import datetime
from find.imageSearch import imageSearch
from pagify.pagify1 import pagify


def main():
    df = tools.parse_location_data('LocationHistory.json')
    start = datetime.datetime(2019,7, 1).date()
    end = datetime.datetime(2019, 7, 30).date()
    time = tools.extract_time_period(df, start, end)
    # print(time)

    paths = imageSearch(time)
    # print(paths)
    pagify(paths)


# main()