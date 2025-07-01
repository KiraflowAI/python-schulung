#Im Folgenden wurde eine Klasse Car erstellt. Was genau __init__ und self hierbei machen werden wir uns später noch anschauen. Wir können sehen, dass einige Instanzattribute hinzugefügt wurden: die Marke, die Farbe und die Anzahl an Türen. Versuche vorherzusagen welche print Ausgabe zu einer Fehlermeldung führt und welche nicht. Teste sie einzelnd!

class Car():
    def __init__(self, brand, color, door_num):
        self.brand = brand
        self.color = color
        self.door_num = door_num

car = Car("VW", "black", 4)

# Tests
print(car.brand())
print(car.color)
print(Car.door_num)
print(car.model)


# Es muss jeder print() Befehl einzelnt ausgeführt werden, da sonst nur die aller erste Fehlermeldung erscheint und nicht alle.

# car.brand() führt hier zu einer Fehlermeldung, da an Attribute keine Klammern gehören.
# Mit Klammern wird Python signalisiert dass es sich um ein Objekt wie bspw. eine Funktion handelt.

# car.color wird ordnungsgemäß ausgeführt und gibt entsprechend black aus.

# Car.door_num führt hier zu einer Fehlermeldung, da Car groß geschrieben ist und somit nicht versucht wird auf das Instanzattribut von car zuzugreifen, sondern auf das der Klasse Car, welches ein solches Attribut nicht hat.

# car.model führt zu einer Fehlermeldung, da es kein Instanzattribut model gibt.


class Car():

    def __init__(self, brand, color, door_num):
        self.brand = brand
        self.color = color
        self.door_num = door_num

car = Car("VW", "black", 4)

# Tests
print(car.brand())              # TypeError: 'str' object is not callable
print(car.color)                
print(Car.door_num)             # AttributeError: type object 'Car' has no attribute 'door_num'
print(car.model)                # AttributeError: 'Car' object has no attribute 'model'
