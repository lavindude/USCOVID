import json
import http.client
import sqlite3
import time
from pgdb import connect
import urllib.request, urllib.parse, urllib.error
import psycopg2
from datetime import date
import datetime

stateData = urllib.request.urlopen('https://covidtracking.com/api/v1/states/current.json').read()
jsonStateData = json.loads(stateData)

#create a database
#conn1 = sqlite3.connect('usInfo.sqlite')
conn1 = connect(database='davdlic7h5pev6', host='ec2-50-16-198-4.compute-1.amazonaws.com', user='okuihecsskhgrn', password='63ef2d42c5f65365bb37c5c391a37a9329c29cd9f757c1e0d8a58c595164be50')
cur = conn1.cursor()

# cur.execute('DROP TABLE IF EXISTS Covid')
# cur.execute('''
# CREATE TABLE Covid (state_data_id SERIAL, date DATE, state_id SERIAL, code TEXT, positive INTEGER, 
# recovered INTEGER, deaths INTEGER, positiveincrease INTEGER, deathincrease INTEGER, positivedivpop NUMERIC, 

# FOREIGN KEY(state_id) REFERENCES states (state_id)

# );
# ''')

#list of states
states = open('listOfStates.txt').read()
jsonStates = json.loads(states)

#coordinates for every state/region
stateCoords = open('stateCoords.txt').read()
jsonCoords = json.loads(stateCoords)

# rows = cur.execute('SELECT COUNT(*) FROM date')

# date = ''
# for item in jsonStateData:
#     dateOriginal = item['date']
#     date = dateOriginal
#     query = 'INSERT INTO date (date) VALUES (%s)'
#     insert_tuple = (date)

#     cur.execute(query, insert_tuple)

#     break

# dateid = cur.execute('SELECT date_id FROM date WHERE date=' + date)
stateid = 1
for item in jsonStateData:
    # date = item['date']
    today = date.today()
    code = item['state']
    if code == 'AS':
        continue
    if code == 'GU':
        continue
    if code == 'MP':
        continue
    if code == 'PR':
        continue
    if code == 'VI':
        continue
    if code == 'DC':
        continue
    positive = item['positive']
    recovered = item['recovered']
    deaths = item['death']
    positiveIncrease = item['positiveIncrease']
    deathincrease = item['deathIncrease']
    state = ''
    lat = 0
    lon = 0

    for item2 in jsonStates:
        if item2['abbreviation'] == code:
            state = item2['name']

    cur.execute('SELECT population FROM states WHERE state_id=%s', [stateid])
    calc = positive / cur.fetchone()[0]

    query = "INSERT INTO Covid (date, state_id, code, positive, recovered, deaths, positiveincrease, deathincrease, positivedivpop) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    insert_tuple = (today, stateid, code, positive, recovered, deaths, positiveIncrease, deathincrease, calc)

    cur.execute(query, insert_tuple)
    stateid += 1

now = datetime.datetime.now()
delTime = now - datetime.timedelta(days=13)
delTime = delTime.date()

cur.execute("DELETE FROM covid WHERE date=%s;", [delTime])

conn1.commit()

print("Parsing complete!")