# #Jupyter Notebooks ist eine Art interaktives Dokument, welches eine sprunghafte Bedienung ermöglicht.

# Sie wiedersprechen der sequentielle Ausführung von Python Code dadurch, dass man diesen theoretisch in beliebiger Reihen ausführen kann, also bspw. zuerst die letzten und dann erst die ersten Zeilen.

# Die Dateiendung einer solchen ist .ipynb.


#Extensions
#Für die Nutzung von Jupyter Notebooks sollte die Extension "Jupyter" installiert werden!



#Zelle
#Ein Jupyter Notebook besteht grundlegend aus zwei Zellen:

# Code-Zelle: Enthält ausführbaren Code
# Markdown-Zelle: Entält formatierten Text, Überschriften, etc.
# Aus mehreren dieser Zellen setzt sich solch ein Notebook zusammen, wobei man jede Code-Zelle individuell ausführen kann, wodurch die Reihenfolge selbstbestimmt festgelegt werden kann, aber auch Zellen mehrmals hintereinander ausgeführt werden können.

# Durch Markdown-Zellen können wir unserem Notebook Struktur verleihen, sowohl durch Überschriften, als auch durch bspw. Beschreibungen.



#DEBUGGER
# Der Debugger kann wie in py-Dateien auch in Jupyter Notebooks verwendet werden.

# Hierzu kann man bei einer Code-Zelle zu dem "Execute Cell" Butten gehen, der sich Links an der Zelle befindet, bei dem man durch "More" zu dem Debugger kommt.

# Der Debugger zeichnet sich hier dadurch aus, dass nicht nur die aktuelle Zelle ausgeführt wird, sondern auch in andere Zellen gesprungen wird, wenn bspw. eine aufgerufene Funktion sich in einer anderen befindet.




#WICHTIGE SHORTCUTS
                    # Shortcut	Funktion
                    # Shift + Enter	Zelle ausführen und zur nächsten springen
                    # Ctrl + Enter	Zelle ausführen, aber nicht wechseln
                    # Esc + A	Neue Zelle oberhalb einfügen
                    # Esc + B	Neue Zelle unterhalb einfügen
                    # Esc + M	Zelle in Markdown umwandeln
                    # Esc + Y	Zelle in Code umwandeln
                    # Esc + DD	Zelle löschen
                    # Esc + Z	Gelöschte Zelle wiederherstellen
                    # Esc + L	Zeilennummern ein-/ausblenden





#Besonderheiten von Code-Zellen
# Es gibt einige Unterschiede zu einer py-Datei. Einer hierbei ist die automatische Ausgabe der letzten, mit Code beschriebenen Zeile.

# Während wir in einer py-Datei immer einen print-Befehl benötigen, brauchen wir diesen in einer Zelle theoretisch nicht, wenn dieser in der letzten Zeile der Zelle steht.


print("Ich werde ausgegeben")



#Installation von Paketen
# Wenn mit pip Pakete installiert werden müssen, kann das über eine Zelle passieren. Dazu lässt man einfach die Zeile mit einem % beginnen, gefolgt vom pip Befehl:

#%pip install faker


