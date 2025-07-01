alter = 70
beschaeftigt = False

if alter < 18:
    print('Sie sind minderjährig')
    if beschaeftigt:
        print('Es ist ungewöhnlich, in diesem Alter beschäftigt zu sein')
    else:
        print('Genießen Sie Ihre Jugendzeit')
elif 18 <= alter < 65:
    print('Sie sind im erwerbsfähigen Alter')
    if beschaeftigt:
        print('Vielen Dank für Ihren Beitrag zur Gesellschaft')
    else:
        print('Vielleicht sind Sie Student oder auf Jobsuche')
else:
    print('Sie sind im Ruhestand.') 
    if beschaeftigt:
        print('Es ist beeindruckend, dass Sie noch arbeiten')
    else:
        print('Genießen Sie Ihren wohlverdienten Ruhestand')



