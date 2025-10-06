import sqlite3

kobling = sqlite3.connect("bokbutikk.db")

c = kobling.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS inventar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tittel TEXT NOT NULL,
    pris REAL,
    antall INTEGER NOT NULL
)
""")

def legg_til_vare():
    pass

inn = ""
while inn != "q":
    print("""
MENY
1. Legg til vare
q  Avslutt
    """)
    inn = input(": ")
    if inn == "1":
        legg_til_vare()