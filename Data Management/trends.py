import json
import http.client
import sqlite3
import time
from pgdb import connect
import urllib.request, urllib.parse, urllib.error
import psycopg2
from datetime import date
import sqlalchemy

#AI libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
import numpy as np
# import mpld3

#python database connection
conn1 = connect(****)
cur = conn1.cursor()

#pandas database connection (used for linear regression)
engine = sqlalchemy.create_engine(*****)
covid_data = pd.read_sql_table("covid", engine)

cur.execute('SELECT MAX(state_data_id) FROM covid;')
count = cur.fetchone()[0]

codes = ["AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DE", "FL", "GA", "HI", 
"IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", 
"MO", "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", 
"OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VA", "VT", "WA", 
"WI", "WV", "WY"]

today = date.today()
today = str(today)
state_id = 1
for code in codes:
    x = list()
    y = list()

    cur.execute('SELECT positiveincrease FROM covid WHERE code=%s', [code])
    p_increase_data = list(cur.fetchall())

    day = 1
    for data in p_increase_data:
        x.append(day)
        y.append(data[0])
        day += 1  

    #linear regression, first convert to pandas series
    x = pd.Series(x).values
    y = pd.Series(y).values
    x = x[:, np.newaxis]
    linear = linear_model.LinearRegression(fit_intercept=True)
    linear.fit(x, y)
    y_pred = linear.predict(x)
    plt.plot(x, y_pred, color='red')
    plt.scatter(x, y)
    
    # uncomment to see graph:
    # plt.xlabel('Day')
    # plt.ylabel('Positive Increase')
    # plt.show()

    cur.execute('SELECT state_id FROM covid WHERE code=%s', [code])
    state_id = cur.fetchone()[0]

    m = linear.coef_
    
    cur.execute('SELECT positive FROM covid WHERE state_id=%s ORDER BY date DESC', [state_id])
    positive = cur.fetchone()[0]
    
    cur.execute('SELECT population FROM states WHERE state_id=%s', [state_id])
    population = cur.fetchone()[0]

    #casesDivPop score algorithm:
    posDivPop_score = positive / population
    print(posDivPop_score)

    print('The slope is ', m, 'for code =', code)
    if m > 25 and posDivPop_score > 0.01:
        cur.execute("UPDATE states SET color='r' WHERE state_id=%s", [state_id])
        print("Red")
    else:
      if m >= 0 and m < 50 and posDivPop_score > 0.007:
        cur.execute("UPDATE states SET color='y' WHERE state_id=%s", [state_id])
        print("Yellow")
      else:
        cur.execute("UPDATE states SET color='g'WHERE state_id=%s", [state_id])
        print("Green")

    state_id += 1
    continue


conn1.commit()
