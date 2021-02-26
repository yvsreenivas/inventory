# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 10:48:53 2021

@author: Windows
"""


import pandas
import sqlite3

conn = sqlite3.connect("db.sqlite3")


df = pandas.read_csv("stocks_stock1.csv")
df.to_sql("stocks_stock", conn, if_exists='append', index=False)