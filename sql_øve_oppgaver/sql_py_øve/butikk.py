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
    pris REAL
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
    
    vare_id  = want
    antall  = fjern
    c.execute("INSERT INTO salg (vare_id, dato, antall) VALUES (?,?,?)", (vare_id, dato, antall))  
    kobling.commit()

    nyMengde = mengde - fjern

    c.execute("UPDATE inventar SET antall = ? WHERE id = ?", (nyMengde, want))
    kobling.commit()

def disp():
    print("VARER")
    c.execute ("SELECT * FROM inventar")
    rows = c.fetchall()

    for row in rows:
        print(row)

def raport():
    c.execute("SELECT DISTINCT dato FROM salg")
    rows = c.fetchall()

    print("Datoer der et salg har blitt gjenomført")

    dateList = []
    x = 0
    for y in rows:
        x += 1
        emptyList = [x, y[0]]
        dateList.append(emptyList)

    print(dateList)

    print("")
    dateUse = input("hvilken dato vil du få raport fra: ")
    dateUsed = dateList[int(dateUse) - 1][1]

    print(dateUsed)

    c.execute("SELECT * FROM salg WHERE dato LIKE ?", (f"%{dateUsed}%",))
    rows = c.fetchall()

    salgList = []
    x = 0
    for y in rows:
        x += 1
        emptyList2 = [y[0], int(y[1]), y[2], y[3], y[4]]
        salgList.append(emptyList2)
        
        print(salgList)
        
    print(" ")

    x = 0
    overSikt = [[salgList[0][1]]]
    for z in salgList:
        x =+ 1
        
        y = 0
        for w in overSikt:
            if salgList[x][1] == overSikt[y][0]:
                overSikt[y].append(salgList[x][3]) #siste ting før looksmaxing





x = datetime.datetime.now()
dato = x.strftime("%x")

inn = ""
while inn != "q":
    disp()
    print("""
MENY
1. Legg til vare
2. sell en vare
3. se hele inventar
4. se dags raporten
q  Avslutt
    """)
    inn = input("Hva vil du: ")
    print("")
    if inn == "1":
        legg_til_vare()

    if inn == "2":
        salg()

    if inn == "3":
        disp()
    
    if inn == "4":
        raport()