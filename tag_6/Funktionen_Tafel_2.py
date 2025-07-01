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

# def brutto_preis(netto_preis, mehrwertsteuer=0.19):
#     steuer = netto_preis * mehrwertsteuer
#     gesamtpreis = netto_preis + steuer
#     result = round(gesamtpreis, 2)
#     return result

# print(brutto_preis(mehrwertsteuer=0.07, netto_preis=0.50))

# buch_netto = 17.50
# print(brutto_preis(buch_netto, 0.07))


def quadrieren(n):
    return n * n

def berechne_hypothenose(länge1, länge2):
    länge1_quadriert = quadrieren(länge1)
    länge2_quadriert = quadrieren(länge2)
    gesamtfläche = länge1_quadriert + länge2_quadriert
    return gesamtfläche ** 0.5

# print(berechne_hypothenose(6, 5) == 7.810249675906654) # 7.81
# print(berechne_hypothenose(3, 4) == 5) # 5
# print(berechne_hypothenose(4, 3) == 5) # 5
# print(berechne_hypothenose(300, 400) == 500) # 500

import unittest

class BerechneHypothenoseTest(unittest.TestCase):
    def test_hypothenos_0(self):
        self.assertEqual(
            berechne_hypothenose(3, 4),
            5
        )

    def test_hypothenos_1(self):
        self.assertEqual(berechne_hypothenose(300, 400), 500)
        
    def test_hypothenos_2(self):
        self.assertAlmostEqual(berechne_hypothenose(5, 6), 7.81, places=2)

unittest.main()

