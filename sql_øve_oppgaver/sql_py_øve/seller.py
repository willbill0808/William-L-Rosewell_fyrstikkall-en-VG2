import sqlite3
import datetime

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
    antall INTEGER NOT NULL,
    pris REAL
    
)
""")

leggList = [["bok", 30, 234], ["ball", 45, 455], ["pc", 1000, 167], ["tv", 500, 241]]

x = 0
for x in range(len(leggList)):
    tittel  = leggList[x][0]
    pris  = leggList[x][1]
    antall  = leggList[x][2]
    c.execute("INSERT INTO inventar (tittel, pris, antall) VALUES (?,?,?)", (tittel, pris, antall))
    kobling.commit()


date1 = datetime.datetime(2025, 10, 26)
dato1 = date1.strftime("%x")
date2 = datetime.datetime(2025, 10, 27)
dato2 = date2.strftime("%x")
date3 = datetime.datetime(2025, 10, 28)
dato3 = date3.strftime("%x")
date4 = datetime.datetime(2025, 10, 29)
dato4 = date4.strftime("%x")

salgList = [[1, dato1, 5, 30], [3, dato2, 3, 1000], [2, dato3, 8, 45], [2, dato4, 13, 45]]

x = 0
for x in range(len(salgList)):
    vare_id = salgList[x][0]
    dato = salgList[x][1]
    antall = salgList[x][2]
    pris = salgList[x][3]

    c.execute("INSERT INTO salg (vare_id, dato, antall, pris) VALUES (?,?,?,?)", (vare_id, dato, antall, pris))  
    kobling.commit()