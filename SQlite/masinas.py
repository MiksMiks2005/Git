import sqlite3
conn = sqlite3.connect('garage.db')
cursor = conn.cursor()
cursor.execute('''
    create table if not exists auto(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Marka TEXT NOT NULL,
        Modelis TEXT NOT NULL,
        Gads INTEGER,
        Nobraukums INTEGER
        )
''')
cursor.execute("INSERT INTO auto (Marka, Modelis, Gads, Nobraukums) VALUES ('Audi', 'A4', 2018, 120000)")
cursor.execute("INSERT INTO auto (Marka, Modelis, Gads, Nobraukums) VALUES ('BMW', '320i', 2020, 50000)")
cursor.execute("INSERT INTO auto (Marka, Modelis, Gads, Nobraukums) VALUES ('Volkswagen', 'Golf', 2015, 180000)")
cursor.execute("INSERT INTO auto (Marka, Modelis, Gads, Nobraukums) VALUES ('Toyota', 'Corolla', 2022, 25000)")
cursor.execute("INSERT INTO auto (Marka, Modelis, Gads, Nobraukums) VALUES ('Mercedes-Benz', 'C-Class', 2019, 90000)")
conn.commit()
cursor.execute("SELECT * FROM auto")
rows = cursor.fetchall()
for i in rows:
    print(i) 


conn.close()