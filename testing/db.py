#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="mysql",  # your host, usually localhost
                     user="tw",  # your username
                     passwd="test",  # your password
                     db="dbdatabase")  # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM test")

# print all the first cell of all the rows
for row in cur.fetchall():
    print(row)

db.close()
