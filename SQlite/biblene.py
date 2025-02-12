import sqlite3
conn = sqlite3.connect('library.db')
cursor = conn.cursor()
cursor.execute('''
    create table if not exists books(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nosaukums TEXT NOT NULL,
        Autors TEXT NOT NULL,
        gads INTEGER,
        zanrs TEXT NOT NULL
        )
''')
cursor.execute("INSERT INTO books (Nosaukums, Autors, gads, zanrs) VALUES ('Hobits', 'J.R.R. Tolkien', 1937, 'Fantastika')")
cursor.execute("INSERT INTO books (Nosaukums, Autors, gads, zanrs) VALUES ('1984', 'George Orwell', 1949, 'Distopija')")
cursor.execute("INSERT INTO books (Nosaukums, Autors, gads, zanrs) VALUES ('Mazais Princis', 'Antoine de Saint-Exupéry', 1943, 'Bērnu literatūra')")
cursor.execute("INSERT INTO books (Nosaukums, Autors, gads, zanrs) VALUES ('Slepkavība Orient Express', 'Agatha Christie', 1934, 'Detektīvs')")
cursor.execute("INSERT INTO books (Nosaukums, Autors, gads, zanrs) VALUES ('Alķīmiķis', 'Paulo Coelho', 1988, 'Filosofija')")
conn.commit()
cursor.execute("SELECT * FROM books WHERE gads >= 1940")
rows = cursor.fetchall()
for i in rows:
    print(i) 
cursor.execute("SELECT * FROM books WHERE Autors = 'J.R.R. Tolkien' AND 'George Orwell' ")
rows = cursor.fetchall()
for i in rows:
    print(i) 
cursor.execute("SELECT * FROM books WHERE zanrs = 'Fantastika'")
rows = cursor.fetchall()
for i in rows:
    print(i) 
cursor.execute("SELECT * FROM books WHERE gads <= 1950 ")
rows = cursor.fetchall()
for i in rows:
    print(i) 
cursor.execute("SELECT * FROM books ORDER BY gads ASC")
rows = cursor.fetchall()
for i in rows:
    print(i) 
cursor.execute("SELECT Nosaukums, MIN(gads) FROM books")
rows = cursor.fetchall()
for i in rows:
    print(i) 


conn.close()
