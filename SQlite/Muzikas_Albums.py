import sqlite3
conn = sqlite3.connect('music.db')
cursor = conn.cursor()
cursor.execute('''
    create table if not exists albums(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nosaukums TEXT NOT NULL,
        Makslinieks TEXT NOT NULL,
        Gads INTEGER,
        Dziesmu_skaits INTEGER
        )
''')
cursor.execute("INSERT INTO albums (Nosaukums, Makslinieks, Gads, Dziesmu_skaits) VALUES ('Abbey Road','The Beatles','1969','17')")
cursor.execute("INSERT INTO albums (Nosaukums, Makslinieks, Gads, Dziesmu_skaits) VALUES ('Dark Side of The Moon','Pink Floyd','1973','10')")
cursor.execute("INSERT INTO albums (Nosaukums, Makslinieks, Gads, Dziesmu_skaits) VALUES ('Thriller','Michael Jackson','1982','9')")
cursor.execute("INSERT INTO albums (Nosaukums, Makslinieks, Gads, Dziesmu_skaits) VALUES ('Nevermind','Nirvana','1991','12')")
cursor.execute("INSERT INTO albums (Nosaukums, Makslinieks, Gads, Dziesmu_skaits) VALUES ('Back to Black','Amy Winehouse','2006','11')")


#atlasīti visi albumi
cursor.execute("SELECT * FROM albums")
rows = cursor.fetchall()
for i in rows:
    print(i) 

#atlasīti albumi, kas izdoti pēc 1990. gada
cursor.execute("SELECT * FROM albums WHERE Gads >= 1990")
rows = cursor.fetchall()
for i in rows:
    print(i) 

#atlasīti albumi ar dziesmu skaitu virs 10
cursor.execute("SELECT * FROM albums WHERE Dziesmu_skaits >10")
rows = cursor.fetchall()
for i in rows:
    print(i) 

#atlasīti visi albumi, kuru mākslinieks ir The Beatles
cursor.execute("SELECT * FROM albums WHERE Makslinieks = 'The Beatles'")
rows = cursor.fetchall()
for i in rows:
    print(i) 

#aprēķināts vidējais dziesmu skaits albumos, kas izdoti pēc 2000. gada
cursor.execute("SELECT Dziesmu_skaits FROM albums WHERE Gads > 2000 ")
rows = cursor.fetchall()
for i in rows:
    print(i) 