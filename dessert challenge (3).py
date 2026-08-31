desserts = ["Kuchen", "Muffin", "Zimtschnecke", "Puddingknote", "Cakepop"]
versuche = 3
gewonnen = False

while versuche >= 1:
    gewonnen = False
    dessert = input("Welches Dessert möchtest du?")

    for eintrag in desserts:
        if dessert == eintrag:
            gewonnen = True
            print("Gefunden!🍰")
    

    if gewonnen:
        print("Ja,", dessert, "ist vorhanden")
        break
    else:
        print(dessert, "ist nicht vorhanden")
        versuche = versuche - 1
        print("Du hast noch" , versuche , "Versuche")
    if versuche == 1:
        print("Du hast noch 1 Versuch")
    if versuche == 0:
        print("Game Over")