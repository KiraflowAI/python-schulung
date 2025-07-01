# #Das folgende Programm berechnet einen Preis.

# Was erscheint hier auf der Konsole, wenn das Programm ausgeführt wird?

# Erkläre, wie sich der Preis berechnet.


# def berechne_rabbatierten_preis(preis, wochentag, alter):
#   rabatt = 0

#   if wochentag == "Sonntag" or wochentag == "Samstag":
#     rabatt = rabatt + 0.25

#   if alter > 65 or alter < 6:
#     rabatt = rabatt + 0.5

#   return preis * (1 - rabatt)


# basis_preis = 10
# heute = "Montag"
# alter_kunde = 70

# end_preis = berechne_rabbatierten_preis(basis_preis, heute, alter_kunde)
# print(end_preis)



                #mit nutzeriengabe

# def berechne_rabbatierten_preis(preis, wochentag, alter):
#     rabatt = 0

#     if wochentag == "Sonntag" or wochentag == "Samstag":
#         rabatt = rabatt + 0.25

#     if alter > 65 or alter < 6:
#         rabatt = rabatt + 0.5

#     return preis * (1 - rabatt)

# # --- Benutzer-Eingaben ---
# preis = float(input("Gib den Basispreis ein (z. B. 10): "))
# wochentag = input("Welcher Wochentag ist heute? (z. B. Montag): ").capitalize()
# alter = int(input("Wie alt ist die Kundin oder der Kunde? "))

# # --- Preis berechnen und anzeigen ---
# endpreis = berechne_rabbatierten_preis(preis, wochentag, alter)
# print("Endpreis nach Rabatt: ", round(endpreis, 2), "Euro")



            # mit nutzereingabe ohne preisbestimmung:

def berechne_preis(wochentag, alter):
    standardpreis = 10
    rabattpreis = 6

    # Entscheide: Standardpreis oder Rabattpreis
    if alter > 65 or alter < 6:
        preis = rabattpreis
    else:
        preis = standardpreis

    # Wochenendrabatt prüfen
    rabatt = 0
    if wochentag == "Samstag" or wochentag == "Sonntag":
        rabatt += 0.25

    endpreis = preis * (1 - rabatt)
    return endpreis

wochentag = input('Welcher Tag ist heute?').capitalize()
alter = int(input('Wie ald bist du?'))

# wochentag = 'Freitag'
# alter = 37

print(berechne_preis(wochentag, alter))







