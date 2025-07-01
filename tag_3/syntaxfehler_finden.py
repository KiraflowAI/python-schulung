print("Willkommen zu deinem Abenteuer!")
print("Du befindest dich an einer Kreuzung im Wald.")
richtung = input("Möchtest du nach links oder rechts gehen? (links/rechts): ")

if richtung == "links":  # SyntaxError: Fehlender Doppelpunkt am Ende der Zeile
    print("\nDu gehst nach links und siehst einen Fluss.")
    aktion = input("Möchtest du den Fluss überqueren oder ihm folgen? (überqueren/folgen): ")
    if aktion == "überqueren":
        print("\nDu versuchst, den Fluss zu überqueren, aber die Strömung ist zu stark.")
        print("Du wirst mitgerissen und das Abenteuer endet hier.")
    elif aktion == "folgen":  # NameError: 'Aktion' ist nicht definiert; sollte 'aktion' sein (Groß-/Kleinschreibung beachten)
        print("\nDu folgst dem Fluss und findest ein kleines Dorf.")
        print("Die Dorfbewohner heißen dich willkommen und bieten dir Unterkunft an.")
        print("Herzlichen Glückwunsch! Du hast das Abenteuer erfolgreich abgeschlossen.")  # NameError: 'prin' ist nicht definiert; sollte 'print' sein
    else:
        print("\nUngültige Eingabe. Das Abenteuer endet hier.")
elif richtung == "rechts":  # SyntaxError: Zuweisungsoperator '=' verwendet; sollte Vergleichsoperator '==' sein
    print("\nDu gehst nach rechts und stößt auf eine Höhle.")
    aktion = input("Möchtest du die Höhle betreten oder vorbeigehen? (betreten/vorbeigehen): ")
    if aktion == "betreten":
        print("\nIn der Höhle findest du einen schlafenden Drachen.")
        aktion2 = input("Möchtest du den Drachen wecken oder leise hinausgehen? (wecken/hinausgehen): ")
        if aktion2 == "wecken":
            print("\nDer Drache erwacht und ist verärgert über die Störung.")  # IndentationError: Diese Zeile sollte eingerückt sein
            print("Du wirst vom Drachen vertrieben und das Abenteuer endet hier.")
        elif aktion2 == "hinausgehen":
            print("\nDu verlässt leise die Höhle und setzt dein Abenteuer fort.")
            print("Nach einiger Zeit findest du einen verborgenen Schatz.")
            print("Herzlichen Glückwunsch! Du hast das Abenteuer erfolgreich abgeschlossen.")
        else:
            print("\nUngültige Eingabe. Das Abenteuer endet hier.")
    elif aktion == "vorbeigehen":  # SyntaxError: 'else' kann keine Bedingung haben; sollte 'elif' sein
        print("\nDu gehst an der Höhle vorbei und gerätst in einen Hinterhalt von Räubern.")
        print("Die Räuber nehmen all deine Habseligkeiten und das Abenteuer endet hier.")
    else:
        print("\nUngültige Eingabe. Das Abenteuer endet hier.")
else:  # IndentationError: Diese Zeile ist falsch eingerückt
    print("\nUngültige Eingabe. Das Abenteuer endet hier.")
