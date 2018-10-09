# inserting rows into database table from a list
import sqlite3
conn=sqlite3.connect('data.db')
list=['rajdeep','']
conn.executemany()
# @TODO