# import libraries
import requests
import pandas as pd
import datetime
import pytz
from dateutil import tz
from dateutil.parser import parse
import os
from twilio.rest import Client
from passwords import *

# read in data from website
airport = 'KPHX'

df = pd.read_html(f'https://flightaware.com/live/airport/{airport}/scheduled')[2]

# remove stacked column levels
df.columns = df.columns.droplevel()

# exclude uninteresting planes
common_planes = [
    'B73',
    'A32',
    'CRJ'
]

# filter out common planes
# and past departures
#df = df[~df.Type.fillna('None').str.contains('|'.join(common_planes)) &  \
 #      (df['ScheduledDeparture Time'].str.slice(start=4, stop=11).apply(lambda x: parse(x).astimezone(pytz.timezone('US/Arizona'))) >  \
#	datetime.datetime.utcnow().replace(tzinfo=pytz.utc).astimezone(pytz.timezone('US/Arizona')))]

# format flight data into text message
msg = '\n'.join(df['Type'] + ' - ' + 
                df['ScheduledDeparture Time'].str.slice(start=4, stop=11) + ' - ' + 
                df['Destination'].str.slice(start=-5, stop=-1))

# establish twilio credentials
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# send text message
client.api.account.messages.create(
    to=MY_PHONE_NUMBER,
    from_=TWILIO_PHONE_NUMBER,
    body=msg);
