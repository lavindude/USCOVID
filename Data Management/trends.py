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
conn1 = connect(database='davdlic7h5pev6', host='ec2-50-16-198-4.compute-1.amazonaws.com', user='okuihecsskhgrn', password='63ef2d42c5f65365bb37c5c391a37a9329c29cd9f757c1e0d8a58c595164be50')
cur = conn1.cursor()

#pandas database connection (used for linear regression)
engine = sqlalchemy.create_engine('postgresql://okuihecsskhgrn:63ef2d42c5f65365bb37c5c391a37a9329c29cd9f757c1e0d8a58c595164be50@ec2-50-16-198-4.compute-1.amazonaws.com/davdlic7h5pev6')
covid_data = pd.read_sql_table("covid", engine)


cur.execute('SELECT MAX(state_data_id) FROM covid;')
count = cur.fetchone()[0]


for i in range(1, 51):
    x = list()
    y = list()

    current = i
    cur.execute('SELECT positiveincrease FROM covid WHERE state_id=%s', [i])
    p_increase_data = list(cur.fetchall())

    day = 1
    for data in p_increase_data:
        x.append(day)
        y.append(data[0])
        day += 1  

    #regression, first convert to pandas series
    #################################
    x = pd.Series(x).values
    y = pd.Series(y).values
    x = x[:, np.newaxis]
    linear = linear_model.LinearRegression(fit_intercept=True)
    linear.fit(x, y)
    y_pred = linear.predict(x)
    plt.plot(x, y_pred, color='red')
    plt.scatter(x, y)
    # plt.xlabel('Day')
    # plt.ylabel('Positive Increase')
    # plt.show()

    cur.execute('SELECT state_id FROM covid WHERE state_data_id=%s', [i])
    state_id = cur.fetchone()[0]

    m = linear.coef_

    print('The slope is ', m)
    if m < 0:
        cur.execute("UPDATE states SET color='g' WHERE state_id=%s", [state_id])
        print("Green")
    elif m >= 0 and m < 50:
        cur.execute("UPDATE states SET color='y' WHERE state_id=%s", [state_id])
        print("Yellow")
    else:
        cur.execute("UPDATE states SET color='r'WHERE state_id=%s", [state_id])
        print("Red")

    continue

################################################

conn1.commit()