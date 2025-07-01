from faker import Faker

fake = Faker() # Faker Instanz wird erzeugt


print('Name:', fake.name()) 
print('Adresse:', fake.address())
# Zufällige Namen und Adressen werden generiert

# virtuelle umgebung einrichten mit python -m venv


# #venv
# Ein Virtual Environment (venv) ermöglicht die Installation von Python-Paketen in einer isolierten Umgebung. Dies verhindert Abhängigkeitskonflikte zwischen verschiedenen Projekten. Jedes Projekt hat dann sozusagen seine eigene Pythoninstallation mit eigenen installierten Bibliotheken.

# 📝
# Markdown
# Um eine virtuelle Umgebung anzulegen öffne eine Konsole in deinem Projektordner und gebe in die Kommandozeile den folgenden Befehl unter Windows ein:

# python3 -m venv venv

#Dies erstellt einen Ordner namens venv. Um die virtuelle Umgebung zu starten muss das passende Skript aus diesem Ordner ausgeführt werden. Unter Windows ist dies:
#source venv/bin/activate


#Alle Pakete, die du installierst, während die Virtuelle Umgebung gestartet ist, werden nur auf diese Installiert. Ein Paket installierst du mit dem Befehl

#pip install paketname

#pip freeze > requirements.txt

#Dieser Befehl speichert alle aktuell installierten Pakete samt deren Versionen in der Datei requirements.txt.

#pip install -r requirements.txt

#Dies liest die Datei ein und installiert alle darin genannten Pakete in der jeweils aktiven Umgebung.

#Diese Befehle helfen dir dabei, Pakete zu installieren, deine Abhängigkeiten zu dokumentieren und sie auf anderen Systemen oder Umgebungen einfach wiederherzustellen.