import datetime
from astral.sun import sun
from astral import LocationInfo

def get_sunrise(latitude, longitude, date):
    # Separating the latitudes from NaN values, which are both floats, the best way is to check that NaN values do not equal themselves

    if latitude == latitude:
        loc = LocationInfo(latitude=latitude, longitude=longitude, timezone='America/Edmonton')
        s = sun(loc.observer, date=date, tzinfo = loc.timezone)
        return s['sunrise'].time()
    # Else, if it's a NaN, write 'no coordinates'
    elif latitude != latitude:
        return 'no coordinates'

# Will work only for latitudes and time of year where Sun reaches 6.0 degrees below the horizon, so there can be a true sunrise.
# I want to exclude stuff in the territories. that is the lat = 60.000

# Recommended application:
# dataframe['sunrise'] = dataframe.apply(lambda row: get_sunrise(row.latitude, row.longitude, row.date), axis=1)

## TODO fix 3rd argument syntax
def is_dawn_chant(time_of_day, sunrise, hours_from_sunrise):

    if isinstance(sunrise, datetime.time):
        time_of_day_minutes = time_of_day.hour * 60 + time_of_day.minute
        sunrise_minutes = sunrise.hour * 60 + sunrise.minute
        if 0 <= time_of_day_minutes - sunrise_minutes<= hours_from_sunrise*60:
            return True
        else:
            return False
    elif isinstance(sunrise, str):
        return 'missing sunrise time'

# Recommended application:
# data['dawn_chant'] = data.apply(lambda row: is_dawn_chant(row.time_of_day, row.sunrise), axis=1)

def get_minutes_since_sunrise(time_of_day, sunrise):
    sunrise_minutes = sunrise.hour * 60 + sunrise.minute
    time_of_day_minutes = time_of_day.hour * 60 + time_of_day.minute
    return time_of_day_minutes - sunrise_minutes

# data.apply(lambda row: sunrise.get_minutes_since_sunrise(row.time_of_day, row.sunrise), axis = 1)