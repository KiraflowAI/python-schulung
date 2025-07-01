#xErstelle eine Funktion countdown_from(n), die auf der Konsole die Zahlen von n bis 0 ausgibt.


#Mit while:

def countdown_from(n):
  counter = n
  while counter >= 0:
    print(counter)
    counter = counter - 1

countdown_from(7)



# Mit for:

def countdown_from(n):
  for i in range(n,-1,-1):
    print(i)

countdown_from(2)