# Funktionen

# def hochleben_lassen():
#     print("Er lebe...")
#     print("hoch!")

# hochleben_lassen()
# hochleben_lassen()
# hochleben_lassen()

# def grüßen(name):
#     print(f"Hallo {name}!")
#     print("Schön, dass du da bist.")
#     if len(name) > 10:
#         print("Das ist ja ein langer Name!")

# grüßen("Kiran")
# hochleben_lassen()
# grüßen("Larysa")
# hochleben_lassen()
# grüßen("Sebastiation")

def brutto_preis(netto_preis, mehrwertsteuer=0.19):
    steuer = netto_preis * mehrwertsteuer
    gesamtpreis = netto_preis + steuer
    result = round(gesamtpreis, 2)
    return result

print(brutto_preis(mehrwertsteuer=0.07, netto_preis=0.50))

buch_netto = 17.50
print(brutto_preis(buch_netto, 0.07))


