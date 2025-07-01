# class Roboter:
#     def __init__(self, farbe):
#         self.farbe = farbe
 
# robo1 = Roboter("grün")
# print(f"Farbe des Roboters 1: {robo1.farbe}")
# robo2 = Roboter("blau")
# print(f"Farbe des Roboters 2: {robo2.farbe}")

class Person:

    def __init__(self, vorname, nachname):

        self.vorname = vorname # hier wird der rahmen gebaut 

        self.nachname = nachname

        self.fullname = vorname + " " + nachname

person1 = Person("Michael", "Blarr") # ab hier wird der ihalt übergeben

person2 = Person("Haji", "Mwadini")

print(person1)
print(person1.vorname)
 

# Beispiel Kursbotton, auf dem Kursbutton sind verschiedene Elemente zu sehen. Inhalte, zur kursübersicht, titel etc, dieser button wird als
# Klasse definiert und innerhalb dieser Klaasse bbennen wir was da steht 
# z.b. Data analyst, 12 monate, link to website 

class Person:

    def __init__(self, vorname, nachname):

        self.vorname = vorname

        self.nachname = nachname

    def fullname(self):

        return self.vorname + " " + self.nachname

p = Person("Michael", "Blarr")

p.nachname = "Glücklich"

print(p.fullname()) # Hier wird gesagt drucke p= aus in der funktion der klasse von fullname

print(Person.fullname(p)) # hier genau dasselbe nur länger
 
