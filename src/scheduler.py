import requests
import datetime
import os
from dateutil.parser import parse

# find today's date
current_date = str(datetime.datetime.today().date())

# assign variables for latitude and longitude
scottsdale_latitude='33.4942'
scottsdale_longitude='-111.9261'

# api call
sunset = requests.get(f'https://api.sunrise-sunset.org/json?lat={scottsdale_latitude}&lng={scottsdale_longitude}&formatted=0&date={current_date}')

# extract UTC time
sunset = sunset.json()['results']['sunset']

# back up from sunset by 10 minutes
sunset = parse(sunset) - datetime.timedelta(hours=7, minutes=10)

# find date for tomorrow
tomorrow = str(datetime.datetime.today().date() + datetime.timedelta(days=1))

# find sunrise  time tomorrow
url=f'https://api.sunrise-sunset.org/json?lat={scottsdale_latitude}&lng={scottsdale_longitude}&formatted=0&date={tomorrow}'
print(url)
sunrise = requests.get(url)

# extract UTC time
sunrise = sunrise.json()['results']['sunrise']
sunrise = parse(sunrise) - datetime.timedelta(hours=7)

# add time to string
sunset_job = f'echo python3 "arrivals_flight_data.py" | at "{str(sunset)[11:16]}"'
sunrise_job = f'echo python3 "departures_flight_data.py" | at "{str(sunrise)[11:16]}"'

# create "at" job
os.system(sunset_job)
os.system(sunrise_job)

# display "at" jobs in que
os.system("atq")
