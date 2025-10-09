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

c.execute("""
CREATE TABLE IF NOT EXISTS salg (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vare_id TEXT NOT NULL,
    dato REAL,
    antall INTEGER NOT NULL
)
""")


def legg_til_vare():
    tittel  = input()
    pris  = input()
    antall  = input()
    c.execute("INSERT INTO inventar (tittel, pris, antall) VALUES (?,?,?)", (tittel, pris, antall))
    kobling.commit()


def salg():
    c.execute ("SELECT * FROM inventar")
    rows = c.fetchall()

    for row in rows:
        print(row)

    print("Hvilken vare vil du selge")
    want = input(":")

    c.execute(f"SELECT * FROM inventar WHERE tittel LIKE '%{want}%'")

    rows = c.fetchall()

    for row in rows:
        print(row)





inn = ""
while inn != "q":
    print("""
MENY
1. Legg til vare
2. sell en vare
q  Avslutt

    """)
    inn = input(": ")
    if inn == "1":
        legg_til_vare()

    if inn == "2":
        salg()