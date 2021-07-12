
#Relational Database - tables and rows
#SQL language to interat with databases
#Every row gets its own ID

import sqlite3 

connection = sqlite3.connect("books.db")

cursor = connection.cursor()

#below would be fields / headers
cursor.execute("""
    CREATE TABLE IF NOT EXISTS book (
        id INTEGER PRIMARY KEY,
            title TEXT,
            pages INTEGER,
            current_page INTEGER
    )
""")
#below are the rows in the spreadsheet

# cursor.execute("""
#     INSERT INTO book VALUES (
#         0, 'A Great Book', 213, 27
#     )
# """)

# cursor.execute("""
#     INSERT INTO book VALUES (
#         1, 'Another Great Book', 222, 33
#     )
# """)

connection.commit()

rows = cursor.execute("""
    SELECT title, pages, current_page FROM book
""")

for row in rows: 
    print(row)
connection.close()