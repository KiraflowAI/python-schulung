#Instanzattribute
# Bisher haben wir uns mit dem einfachsten Fall einer Klasse beschäftigt und auch einige solcher Klassen erstellt. Jetzt wollen wir einen Schritt weiter gehen und unseren Objekten gewisse Eigenschaften geben.
# Als allererstes Beispiel hatten wir die Klasse Car:

                    # class Car():
                    #     pass

#Diese soll für uns eine Blaupause für Autos sein. Um im ersten Anlauf einige Autos unterscheiden zu können, fügen wir der Klasse sogenannte Instanzattribute für die Eigenschaften Marke, Farbe und Türanzahl hinzu.
#Dies könnte im Anschluss folgendermaßen aussehen:


# class Car():
    
#     def __init__(self, brand, color, door_num):
#         self.brand = brand          # Automarke
#         self.color = color          # Farbe des Autos
#         self.door_num = door_num    # Türanzahl

# car_1 = Car()

# Wir können feststellen, dass sich eine Instanz nicht mehr so einfach erstellen lässt wie zuvor. Die ausgegebene Fehlermeldung sagt uns, dass 3 Argumente fehlen:
#     TypeError: Car.__init__() missing 3 required positional arguments: 'brand', 'color', and 'door_num'
# Diese sind, wie man bereits vermuten kann, unsere neu hinzugefügten Instanzattribute, welche wir beim Initialisieren mit angeben müssen:


# class Car():
    
#     def __init__(self, brand, color, door_num):
#         self.brand = brand          # Automarke
#         self.color = color          # Farbe des Autos
#         self.door_num = door_num    # Türanzahl

# car_1 = Car("VW", "black", 4)


# Nun haben wir eine Instanz der Klasse Car, welche nun auch drei Instanzattribute besitzt, oder einfach gesagt: Ein Auto mit drei Eigenschaften.
# Aber wie kommen wir nun an diese heran?
# Die Syntax hierbei hat Ähnlichkeiten zu Ordnerpfaden, allerdings anders als dort mit Schrägstrichen benutzen wir hier Punkte:

class Car():
    
    def __init__(self, brand, color, door_num):
        self.brand = brand          # Automarke
        self.color = color          # Farbe des Autos
        self.door_num = door_num    # Türanzahl

car_1 = Car("VW", "black", 4)

print(car_1.brand)
print(car_1.color)
print(car_1.door_num)

#Ausgabe: 
# VW
# black
# 4

# Wir greifen quasi auf die Instanz und anschließende eine Ebene tiefer auf das Attribut zu.
# Wie lassen sich aber solche Instanzattribute ändern?
#Angenommen wir haben erst im Nachhinein festgestellt, dass bei der Anzahl der Türen der Kofferraum mitgezählt werden soll, oder die Farbe des Autos nicht Schwarz, sondern ein dunkles Blau ist, dann können wir die entsprechenden Instanzattribute einfach per Zuweisung auch wieder ändern:


class Car():
    
    def __init__(self, brand, color, door_num):
        self.brand = brand          # Automarke
        self.color = color          # Farbe des Autos
        self.door_num = door_num    # Türanzahl

car_1 = Car("VW", "black", 4)

car_1.color = "blue"
car_1.door_num = 5

print(car_1.brand)
print(car_1.color)
print(car_1.door_num)

# #VW
# blue
# 5
#Wir sehen, dass sich durch eine einfache Zuweisung ein Instanzattribut ändern lässt.

