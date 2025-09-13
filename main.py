import sqlite3

conn=sqlite3.connect('test.db')
cursor=conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS students (id INT, surname TEXT, name TEXT,'
               'birthday INT, gendor TEXT, faculty TEXT)')

# cursor.execute("INSERT INTO students (id, surname, name,"
#                "birthday, gendor, faculty) VALUES ( 0, 'Ismoil', 'BF')")
# cursor.execute("INSERT INTO students (id, surname, name,"
#                "birthday, gendor, faculty) VALUES ( 1, 'Islom', 'CF')")
# cursor.execute("INSERT INTO students (id, surname, name,"
#                "birthday, gendor, faculty) VALUES ( 2, 'Xasan', 'CF')")
# cursor.execute("INSERT INTO students (id, surname, name,"
#                "birthday, gendor, faculty) VALUES ( 3, 'Ibrohim',  'CF')")
# cursor.execute("INSERT INTO students (id, surname, name,"
#                "birthday, gendor, faculty) VALUES ( 4, 'Nigina', 'Davronova', 'BF')")
#
# cursor.execute('''SELECT * FROM students''')
# result=cursor.fetchall()
# print(result)
#
#
cursor.execute('''SELECT * FROM students WHERE grades > 4''')

rows=cursor.fetchall()
for row in rows:
    print(row)
#
#
# cursor.execute('''SELECT * FROM students ORDER BY name''')
#
# result=cursor.fetchall()
# print(result)
#

conn.commit()
print('hello')

