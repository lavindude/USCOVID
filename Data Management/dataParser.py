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
conn1 = connect(***)
cur = conn1.cursor()

#list of states
states = open('listOfState.txt')
jsonStates = json.loads(states)

#coordinates for every state/region
stateCoords = open('stateCoords.txt')
jsonCoords = json.loads(stateCoords)

#insert jSON into database
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
