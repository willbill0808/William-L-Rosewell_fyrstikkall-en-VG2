import sqlite3

kobling = sqlite3.connect("butikk.db")

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
    tittel  = input()
    pris  = input()
    antall  = input()
    c.execute("INSERT INTO inventar (tittel, pris, antall) VALUES (?,?,?)", (tittel, pris, antall))
    kobling.commit

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