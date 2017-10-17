#!/usr/bin/python
import MySQLdb
import sys

sys.path.append("/skateboard/src/configuration/")
from configuration import *

if not configuration["database"]["status"]:
    sys.exit("Database init error")
db = MySQLdb.connect(host="mysql",  # your host, usually localhost
                     user="tw",  # your username
                     passwd="test",  # your password
                     db="skateboard")  # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()
sql = "CREATE TABLE `skateboard`.`variables` ( " \
      "`id` INT NOT NULL AUTO_INCREMENT , " \
      "`name` TEXT NOT NULL , " \
      "`data` TEXT NOT NULL , " \
      "PRIMARY KEY (`id`)) ENGINE = InnoDB"
sql = "CREATE TABLE `skateboard`.`errors` ( " \
      "`id` INT NOT NULL AUTO_INCREMENT , " \
      "`date` DATE NOT NULL , " \
      "`text` TEXT NOT NULL , " \
      "`status` TEXT NOT NULL , " \
      "`data` TEXT NOT NULL , " \
      "PRIMARY KEY (`id`)) ENGINE = InnoDB"
cur.execute(sql)
sql = "CREATE TABLE `skateboard`.`users` ( " \
      "`id` INT NOT NULL AUTO_INCREMENT , " \
      "`name` TEXT NOT NULL , " \
      "`status` TEXT NOT NULL , " \
      "`data` TEXT NOT NULL , " \
      "PRIMARY KEY (`id`)) ENGINE = InnoDB"
cur.execute(sql)

try:
    cur.execute("INSERT INTO `variables` (`id`, `date`, `text`, `status`) VALUES (NULL, '2017-10-15', 'test', 'test');")
    db.commit()
except SystemError:
    db.rollback()

# Use all the SQL you like
# cur.execute("SELECT * FROM test")

# print all the first cell of all the rows
# for row in cur.fetchall():
#   print(row)

db.close()
