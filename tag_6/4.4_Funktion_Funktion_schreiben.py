# Erstelle eine Funktion countdown, die auf der Konsole die Zahlen von 10 bis 0 ausgibt.

# Bonus 🚀 Verwende eine while- oder for-Schleife in deiner Implementierung.


def countdown():
  print(10)
  print(9)
  print(8)
  print(7)
  print(6)
  print(5)
  print(4)
  print(3)
  print(2)
  print(1)
  print(0)

countdown()


# while schleife
def countdown():
  counter = 10
  while counter > -1:
    print(counter)
    counter = counter - 1

countdown()


#for schleife
def countdown():
  for counter in range(10,-1,-1):
    print(counter)

countdown()
