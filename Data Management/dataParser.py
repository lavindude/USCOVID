import json
import http.client
import sqlite3
import time
from pgdb import Connection
import urllib.request, urllib.parse, urllib.error
import psycopg2
from datetime import date
import requests
import datetime
import pandas as pd
import requests
from io import StringIO
import datetime

# outbreak forecaster: https://www.youtube.com/watch?v=_Hi6_JQesSQ

# main data
url_base = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/'

req_date = datetime.datetime.now() - datetime.timedelta(days=1)
formatted_date = req_date.strftime("%m-%d-%Y")

url = url_base + str(formatted_date) + '.csv'

data = requests.get(url).text
data = StringIO(data)
df = pd.read_csv(data)

# compare previous day's data with today's
req_date = datetime.datetime.now() - datetime.timedelta(days=2)
formatted_date = req_date.strftime("%m-%d-%Y")
url = url_base + str(formatted_date) + '.csv'

data = requests.get(url).text
data = StringIO(data)
prev_df = pd.read_csv(data)

# connect to database
conn1 = Connection(****)
cur = conn1.cursor()

# index + 1 is the id of each state in the list
states_list = ['Alaska', 'Alabama', 'Arkansas', 'Arizona', 'California', 'Colorado', 'Connecticut', 'Delaware', 
    'Florida', 'Georgia', 'Hawaii', 'Iowa', 'Idaho', 'Illinois', 'Indiana', 'Kansas', 
    'Kentucky', 'Louisiana', 'Massachusetts', 'Maryland', 'Maine', 'Michigan', 'Minnesota', 'Missouri', 'Mississippi', 
    'Montana', 'North Carolina', 'North Dakota', 'Nebraska', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'Nevada', 
    'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 
    'Tennessee', 'Texas', 'Utah', 'Virginia', 'Vermont', 'Washington', 'Wisconsin', 'West Virginia', 'Wyoming']

us_confirmed = 0 # used for total US data
us_deaths = 0

today = date.today()
for index in range(0, len(states_list)):
    selected_df = df[df['Province_State'] == states_list[index]]
    positive = int(selected_df['Confirmed'])
    deaths = int(selected_df['Deaths'])
    
    us_confirmed += positive
    us_deaths += deaths

    previous_selected_df = prev_df[prev_df['Province_State'] == states_list[index]]
    previous_positive = int(previous_selected_df['Confirmed'])
    previous_deaths = int(previous_selected_df['Deaths'])
    positiveIncrease = positive - previous_positive
    deathincrease = deaths - previous_deaths

    cur.execute('SELECT population FROM states WHERE state_id=%s', [index + 1])
    calc = positive / cur.fetchone()[0]

    query = "INSERT INTO Covid (date, state_id, positive, deaths, positiveincrease, deathincrease, positivedivpop) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    insert_tuple = (today, index + 1, positive, deaths, positiveIncrease, deathincrease, calc)

    cur.execute(query, insert_tuple)

# delete data from the database that is older than 11 days
cur.execute("DELETE FROM covid WHERE date < now() - interval '11 days';")
conn1.commit()

# Data for America as a whole
cur.execute('DELETE FROM America;')
conn1.commit()

sql = 'INSERT INTO America (date, confirmed, deaths) VALUES (%s, %s, %s);'
params = (today, us_confirmed, us_deaths)
cur.execute(sql, params)

conn1.commit()

print("Parsing complete!")
