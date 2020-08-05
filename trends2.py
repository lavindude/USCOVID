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

# rows = cur.execute("SELECT * FROM covid;")
# for item in rows:
#     state = item[2]
#     print(state)
cur.execute('SELECT COUNT(*) FROM covid;')
count = cur.fetchone()[0]

#get the trend for each state based off 10 days of data (counts backwards)
day = 10
for i in range(count, count - 50, -1):
    x = list()
    y = list()
    cur.execute('SELECT positiveincrease FROM covid WHERE state_data_id=%s', [i])
    p_increase = cur.fetchone()[0]
    x.append(1)
    y.append(p_increase)

    #regression
    x = pd.Series(x).values
    y = pd.Series(y).values
    x = x[:, np.newaxis]
    linear = linear_model.LinearRegression(fit_intercept= True)
    linear.fit(x, y)
    y_pred = linear.predict(x)
    plt.plot(x, y_pred, color='red')
    plt.scatter(x, y)
    plt.xlabel('Day')
    plt.ylabel('Positive Increase')
    plt.show()

# x = covid_data['date'].values
# x = x[:, np.newaxis]
# y = covid_data['positiveincrease'].values

# linear = linear_model.LinearRegression(fit_intercept= True)

# linear.fit(x, y)

# y_pred = linear.predict(x)
# plt.plot(x, y_pred, color='red')
# plt.scatter(x, y)
# # plt.xlabel('Death Increase')
# # plt.ylabel('Positive Increase')
# plt.show()


conn1.commit()