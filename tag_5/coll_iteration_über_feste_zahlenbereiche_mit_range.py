# Möchte man über einen bestimmten Zahlenraum iterieren, so verwendet man in Python die range-Funktion. Es gibt drei Möglichkeiten range aufzurufen:

Anazahl Parameter	Aufruf	                      Bedeutung                                                                 	Beispiel	            Entsprechende Liste
1   	            range(end)	                  Die Range enthält die Integer von 0 bis ausschließlich end.	                range(3)	            [0,1,2]
2	                range(start, end)	          Die Range enthält die Integer von start bis ausschließlich end.	            range(12, 15)	        [12,13,14]
3	                range(start, end, step_size)  Die Range enthält die Integer von start bis ausschließlich end.               range(3, 10, 2)	        [3,5,7,9]
                                                 und geht dabei in Schritten der Größe step_size.	