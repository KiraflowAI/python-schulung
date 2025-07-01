# #Schreibe ein Programm, das den Benutzer zur Eingabe eines Passworts auffordert. 
# Das Passwort muss bestimmte Kriterien erfüllen 
# (z.B. mindestens 8 Zeichen lang, enthält sowohl Zahlen als auch Buchstaben). 
# Das Programm soll dem Benutzer mitteilen, ob das eingegebene Passwort gültig 
# ist oder nicht. Wenn das Passwort nicht gültig ist, soll das Programm spezifizieren, 
# welche Kriterien nicht erfüllt wurden.

# Um zu prüfen, ob ein String eine Zahl ist, kann die Methode isdigit 
# genutzt werden und um zu überprüfen, ob ein String ein Buchstabe ist, 
# kann isalpha genutzt werden:

                        # print("k".isdigit()) # False
                        # print("1".isdigit()) # True

                        # print("k".isalpha()) # True
                        # print("1".isalpha()) # False

#Mit einer for-Schleife können auch auch Strings durchlaufen werden.


password = input('Bitte gib ein Passwort ein:')

min_length_ok = len(password) >= 8      # Hier wird geprüft ob der String lang genug ist

digit_found = False
for char in password:
    if char.isdigit():
        digit_found = True
        break                           # Hier wird geprüft ob eine zahl enthalten ist.


char_found = False                      
for char in password:
    if char.isalpha():
        char_found = True
        break                          # Hier wird geprüft ob ein Buchstabe eingegeben wurde



if min_length_ok and digit_found and char_found:
    print('Password ok')
else:
    print('Password not ok')


if not min_length_ok:
    print('Es ist zu kurz')
if not digit_found:
    print('Es fehlt mindestens eine Ziffer')
if not char_found:
    print('Es fehlt mindestens ein buchstabe')


