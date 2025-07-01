#Erstelle ein einfaches Telefonbuch-Programm, das es dem Benutzer ermöglicht, Namen und Telefonnummern hinzuzufügen, zu suchen, zu ändern und zu löschen. Verwende ein Dictionary zur Speicherung der Daten. Das Programm soll fortlaufend laufen, bis der Benutzer sich entscheidet, es zu beenden. Achte darauf, dass es nicht bei Fehleingaben abstürzt.


#Mit key in my_dict, kann geprüft werden, ob der Schlüssel key im Dictionary my_dict vorhanden ist.


telefonbuch = {}

while True:
    aktion = input("Wähle eine Aktion: hinzufügen, suchen, ändern, löschen: ")

    
    if aktion == "hinzufügen":
        name = input("Name: ")
        if name in telefonbuch:
            print("Der Name ist bereits im Telefonbuch vorhanden. Abbruch.")
        else:
            nummer = input("Telefonnummer: ")
            telefonbuch[name] = nummer
    elif aktion == "suchen":
        name = input("Name: ")
        print(telefonbuch.get(name, "Nicht gefunden"))
    elif aktion == "ändern":
        name = input("Name: ")
        if name in telefonbuch:
            nummer = input("Neue Telefonnummer: ")
            telefonbuch[name] = nummer
        else:
            print("Name nicht im Telefonbuch. Abbruch.")
    elif aktion == "löschen":
        name = input("Name: ")
        if name in telefonbuch:
            del telefonbuch[name]
        else:
            print("Name nicht im Telefonbuch. Abbruch")

    print("Aktuelles Telefonbuch:", telefonbuch)
