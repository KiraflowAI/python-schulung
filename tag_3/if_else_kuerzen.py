#Aufgabe A:
#x = 7

#if x > 0:
#    result = "positiv"
#else:
#    result = "negativ oder null"

#print(f"{x} ist {result}.")

#gekürzte version
#x = 7
#print(f"{x} ist {'positiv' if x > 0 else 'negativ'}.")



# Aufgabe B:
#gewicht = 50
#groesse = 180
#mitfahrerlaubnis = True

#if gewicht > 120 or groesse < 60:
#    mitfahrerlaubnis = False

#if mitfahrerlaubnis:
#    print(f"Du darfst mitfahren.")
#else:
#    print(f"Du darfst nicht mitfahren.")


# Schritt 1 

#gewicht = 50
#groesse = 180
#mitfahrerlaubnis = False if gewicht > 120 or groesse < 60 else True

#if mitfahrerlaubnis:
#    print(F'Du darfst mitfahren.')
#else:
#    print(f'Du darfst nicht mitfahren')

# Schritt 2

#gewicht = 50
#groesse = 180
#mitfahrerlaubnis = True if not (gewicht > 120 or groesse < 60) else False

#if mitfahrerlaubnis:
#    print(f'Du darfst mitfahren')
#else: 
#    print(f'Du darfst nicht mitfahren')

#Schritt 3

#gewicht = 50
#groesse = 50
#mitfahrerlaubnis = not(gewicht > 120 or groesse < 60)

#print(f'Du darfst {'' if mitfahrerlaubnis else 'nicht} mitfahren'}')

#Schritt 4:

# gewicht = 50
# groesse = 180

# print(f'Du darfst {'' if not(gewicht > 120 or groesse < 60) else 'nicht'} mitfahren')



# Aufgabe C: 

# temp = 10

# if temp < 0:
#     feeling = 'Gefroren'
# elif 0 <= temp < 20:
#     feeling = 'Kalt'
# elif 20 <= temp < 30:
#     feeling = 'Angenehm'
# else: 
#     feeling = 'Heiß'

# print(f'Heute ist es {feeling}')

# Gekürzt

temp = 60
feeling = 'gefroren' if temp < 0 else 'kalt' if temp < 20 else 'angenehm' if temp < 30 else 'heiß'

print(f' Heute ist es {feeling}')

