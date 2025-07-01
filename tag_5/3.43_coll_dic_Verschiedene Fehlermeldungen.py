#Schreibe Code, der die folgenden #Fehlermeldungen erzeugt:

#a.)
                    # Traceback (most recent call last):
                    #   File "c:\Users\Vikto\PycharmProjects\einfuehrung-python\something.py", line 2, in <module>
                    #     for name, fach, noten in studenten.items():
                    #         ^^^^^^^^^^^^^^^^^
                    # ValueError: not enough values to unpack (expected 3, got 2)


#a) Wenn man auf einem Dictionary items() aufruft, so muss man immer genau zwei Variablen bereithalten, nicht drei!

                            # studenten = {"Katha": {"Mathe": 1}}
                            # for name, fach, noten in studenten.items():
                            #     print(studenten)



#b.)
                        ... # ganz viele "Hallo"
                        # Hallo
                        # Hallo
                        # Hallo
                        # Hallo
                        # Hallo
                        # Hallo
                        # Hallo
                        # Hallo
                        # Traceback (most recent call last):
                        # File "c:\Users\Vikto\PycharmProjects\einfuehrung-python\something.py", line 2, in <module>
                        #     print("Hallo")
                        #     ~~~~~^^^^^^^^^
                        # KeyboardInterrupt


#b.) Der folgende Code erzeugt eine Endlosschleife. Wenn diese mit Strg+C abgebrochen wird, erscheint die gesuchte Fehlermeldung.

                        # while True:
                        #     print("Hallo")




                    # #c.) Traceback (most recent call last):
                    # File "c:\Users\Vikto\PycharmProjects\einfuehrung-python\something.py", line 1, in <module>
                    #     zahl = int(input("Gib eine Zahl ein"))
                    # ValueError: invalid literal for int() with base 10: ''



#c.)zahl = int(input("Gib eine Zahl ein"))

