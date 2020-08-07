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

x = covid_data['deathincrease'].values
x = x[:, np.newaxis]
y = covid_data['positiveincrease'].values

linear = linear_model.LinearRegression(fit_intercept= True)

linear.fit(x, y)

y_pred = linear.predict(x)
plt.plot(x, y_pred, color='red')
plt.scatter(x, y)
plt.xlabel('Death Increase')
plt.ylabel('Positive Increase')
plt.show()


conn1.commit()