# import libraries
import requests
import pandas as pd
import datetime
from dateutil.parser import parse
import os
from twilio.rest import Client
from passwords import *

# read in data from website
airport = 'KPHX'

df = pd.read_html(f'https://flightaware.com/live/airport/{airport}/enroute')[2]

# remove stacked column levels
df.columns = df.columns.droplevel()

# exclude uninteresting planes
common_planes = [
    'B73',
    'A32',
    'CRJ'
]

# filter out cases where no departure time or aircraft type identification is given
df = df[~df.Type.fillna('None').str.contains('|'.join(common_planes))].dropna(subset=['Departure'])

# format flight data into text message
msg = '\n'.join(df['Type'] + ' - ' + 
                df['EstimatedArrival Time'].str.slice(start=4, stop=11) + ' - ' + 
                df.Origin.str.slice(start=-5, stop=-1))

# establish twilio credentials
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# send text message
client.api.account.messages.create(
    to=MY_PHONE_NUMBER,
    from_=TWILIO_PHONE_NUMBER,
    body=msg);
