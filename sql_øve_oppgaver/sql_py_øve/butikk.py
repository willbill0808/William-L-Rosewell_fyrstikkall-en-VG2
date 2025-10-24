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
    tittel  = input("Navn på vare:")
    pris  = input("Prisen på vare:")
    antall  = input("Mengde av varen:")
    c.execute("INSERT INTO inventar (tittel, pris, antall) VALUES (?,?,?)", (tittel, pris, antall))
    kobling.commit()


def salg():
    c.execute ("SELECT * FROM inventar")
    rows = c.fetchall()

    for row in rows:
        print(row)

    print("")

    want = input("Hvilken vare vil du selge:")

    c.execute("SELECT * FROM inventar WHERE id == ?", (want))

    result = c.fetchone()  
    print(result)
    Navnet = result[1]
    mengde = result[3]
    
    text = f"Du har {mengde} igjen av {Navnet}"
    print(text)
    fjern = int(input("hvor mange vil du fjerne: "))

    nyMengde = mengde - fjern

    c.execute("UPDATE inventar SET antall = ? WHERE id = ?", (nyMengde, want))
    kobling.commit()


def disp():
    c.execute ("SELECT * FROM inventar")
    rows = c.fetchall()

    for row in rows:
        print(row)



inn = ""
while inn != "q":
    print("""
MENY
1. Legg til vare
2. sell en vare
3. se hele inventar
q  Avslutt
    """)
    inn = input("hva vil du: ")
    print("")
    if inn == "1":
        legg_til_vare()

    if inn == "2":
        salg()

    if inn == "3":
        disp()