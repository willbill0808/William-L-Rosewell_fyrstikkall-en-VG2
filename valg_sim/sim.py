import random

list = [["AP", 0, 0, 0, 28.2], ["SV", 0, 0, 0, 5.5], ["Høyre", 0, 0, 0, 14.6], ["MDG", 0, 0, 0, 4.7], ["FRP", 0, 0, 0, 23.9], ["SP", 0, 0, 0, 5.6], ["Rødt", 0, 0, 0, 5.3], ["KRF", 0, 0, 0, 4.2], ["Venstre", 0, 0, 0, 3.6], ["Annet", 0, 0, 0, 4.4], 0]

length = len(list) - 1

f = open("demofile.txt", "rt")

#bestemmer hva sjangsen for hvert parti å bli valgt er 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
weights = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

for x in range(length):
    weights[x] = list[x][4]
    numbers[x] = x + 1

#spør om du vil se loggen eller starte en ny simulation

def innit():
    y = True
    while y == True:
        print(" ")

        print("vil du starte simulationen, eller se på loggen, svar 1 eller 2")
        stemmere = input("")
        try:
            stemmere = int(stemmere)
            y = False
        except:
            print("må være et tall" )
    
    if stemmere == 1:
        start()
    else:
        fileHandeling()


#starten av simulationen, spør hvor mange stemmere som skal bli beregnet

def start():

    y = True
    while y == True:
        print(" ")

        print("hvor mange skal stemme, includert deg")
        stemmere = input("")
        try:
            stemmere = int(stemmere)
            y = False
        except:
            print("må være et tall" )

    for x in range(length): #denne delen skriver ut alle partiene, og viser hva du må skrive for å stemme det du vil
            txt = f"{x + 1}. {list[x][0]}"
            print(txt)
    stem(stemmere)

#spør hvilke parti som skal bli stemt og passer på at bruker inputen er en int verdi




def stem(stemmere):
    
    y = True

    while y == True:
        stemme = input("stem med tall : ")
        try:
            stemme = float(stemme)
            y = False
        except:
            print("må være et tall.")


    if stemme > length: #passer på at verdien er et gyldig tall
        txt = f"dette tallet er for høyt, {length} er maxen"
        print(txt)
        stem(stemmere)

    elif stemme <= 0:
        txt = f"tallet må være høyere enn null"
        print(txt)
        stem(stemmere)

    
    stem2(stemme, stemmere)

#generer de andre valgene basert på sjangsene

def stem2(stemme, stemmere):

    for x in range(length): #her legger den faktisk til brukeren sin verdi
        if x + 1 == stemme:
            list[x][1] = list[x][1] + 1


    for x in range(stemmere -1): #her kommer den på et tilfeldig tall basert på sjansene 
        stemme = random.choices(numbers, weights=weights, k=1)[0]

        for x in range(length): #legger verdiene inn i systemmet
            if x + 1 == stemme:
                list[x][1] = list[x][1] + 1


    for x in range(length): #finner verdiene i prosent
        prosent = list[x][1] / stemmere * 100

        list[x][2] = prosent
        list[x][3] = round(prosent, 2)

    print(" ")
    print("--------------------------------------------")

    for x in range(length):
        txt = f"\n{list[x][0]} fikk {list[x][1]} stemmer, det er {list[x][3]}%\n"
        print(txt)

    print(" ")
    print("--------------------------------------------")
    # bestemmer hvem vinneren er basert på antall 

    rangsering = sorted(range(length), key=lambda i: list[i][1])
    


    førsteP = rangsering[length - 1]

    vinner = list[førsteP][0]

    txt = f"Vinneren av dette valget er {vinner}"
    list[length] = txt

    files(list)

#legger til alt i en text fil

def files(list):

    for x in range(length):

        txt = f"\n\n{list[x][0]} fikk {list[x][1]} stemmere, som tilsvarer {list[x][3]}%\n"

        try:
            
            with open("demofile.txt", "a") as a:
                a.write(txt)

        except:

            with open("demofile.txt", "w") as w:
                w.write(txt)

    txt = f"\n{list[length]}\n -------------------------------------------->"

    with open("demofile.txt", "a") as a:
        a.write(txt)
    
    innit()

#om brukeren velger 2 på innit så leser den opp hele valg loggen

def fileHandeling():
    print(f.read())

    y = True
    while y == True:
        print(" ")

        print("har du lyst til å slette loggen")
        stemmere = input("")
        try:
            stemmere = int(stemmere)
            y = False
        except:
            print("må være et tall" )
    
    if stemmere == 1:

        with open("demofile.txt", "w") as w:
                w.write("\n")

        print("loggen ble slettet")
        
    else:
        print("loggen ble ikke slettet")

        innit()

        

    innit()

innit()