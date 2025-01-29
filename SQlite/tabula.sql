CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);
INSERT INTO students (name, surname, email)
VALUES ('Reinis', 'Kurpnieks', 'reinis@programmesana2.lv'),
        ('Rinals', 'Kalns', 'rinals@programmesana2.lv'),
        ('Renāte', 'Kundziņa', 'renate@programmesana2.lv');