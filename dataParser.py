import json
import http.client
import sqlite3
import time
import pymysql
import urllib.request, urllib.parse, urllib.error
import psycopg2

stateData = urllib.request.urlopen('https://covidtracking.com/api/v1/states/current.json').read()
jsonStateData = json.loads(stateData)

#create a database
#conn1 = sqlite3.connect('usInfo.sqlite')
conn1 = pymysql.connect(host='localhost',
    user='lavindu',
    password='lavi',
    db='covid',
    #charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)
cur = conn1.cursor()

cur.execute('DROP TABLE IF EXISTS Covid')
cur.execute('''
CREATE TABLE Covid (date INTEGER, state TEXT, code TEXT, positive INTEGER, negative INTEGER,
hospitalNow INTEGER, hospitalTotal INTEGER, recovered INTEGER, deaths INTEGER,
lat NUMERIC, lon NUMERIC)''')

#list of states
states = open('listOfStates.txt').read()
jsonStates = json.loads(states)

#coordinates for every state/region
stateCoords = open('stateCoords.txt').read()
jsonCoords = json.loads(stateCoords)

for item in jsonStateData:
    date = item['date']
    code = item['state']
    positive = item['positive']
    negative = item['negative']
    hospitalNow = item['hospitalizedCurrently']
    hospitalTotal = item['hospitalizedCumulative']
    recovered = item['recovered']
    deaths = item['death']
    state = ''
    lat = 0
    lon = 0

    for item2 in jsonStates:
        if item2['abbreviation'] == code:
            state = item2['name']

    for item3 in jsonCoords:
        if item3['state'] == state:
            lat = item3['latitude']
            lon = item3['longitude']

    # cur.execute('''
    # INSERT INTO Covid (date, state, code, positive, negative, hospitalNow, hospitalTotal,
    # recovered, deaths, lat, lon) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
    # (date, state, code, positive, negative, hospitalNow, hospitalTotal, recovered, deaths, lat, lon))

    query = "INSERT INTO Covid (date, state, code, positive, negative, hospitalNow, hospitalTotal, recovered, deaths, lat, lon) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    insert_tuple = (date, state, code, positive, negative, hospitalNow, hospitalTotal, recovered, deaths, lat, lon)

    cur.execute(query, insert_tuple)

conn1.commit()