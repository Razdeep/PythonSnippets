# Using sqlite3
import sqlite3
conn=sqlite3.connect('Example.db')
# conn.execute('Create table student(name,address,age,mob)')
print('Table created')
conn.execute('insert into student values("Raj","ssd","sdf","adgg")')
print('Row has been inserted')
student=conn.execute('select * from student').fetchall()
print(student)