# ------------------------------------------------------------
# Streamlit App: NHL Teams Analyse – lokale CSV, mit Kommentaren
# ------------------------------------------------------------

# 1. Bibliotheken importieren
# Wir brauchen pandas für Datenverarbeitung und Streamlit für die App-Oberfläche.
import streamlit as st
import pandas as pd

# 2. CSV-Datei aus dem Projektordner einlesen
# Diese Datei enthält alle NHL-Daten und muss im selben Ordner wie dieses Skript liegen.
# Wir lesen sie in ein DataFrame (df) ein, damit wir mit den Daten arbeiten können.
df = pd.read_csv("tag_15/teams.csv")

# 3. Seitenleiste: Bereich für interaktive Filteroptionen
# Mit st.sidebar erstellen wir ein Menü links an der Seite der App.
st.sidebar.header("Filteroptionen")  # Überschrift für die Seitenleiste

# 4. Liste aller verfügbaren NHL-Teams erzeugen
# Wir holen uns alle eindeutigen Einträge aus der Spalte "Team", sortieren sie alphabetisch.
# Diese Liste verwenden wir später als Auswahloptionen im Multiselect-Feld.
team_names = sorted(df["Team"].unique())

# 5. Multiselect-Feld zur Auswahl mehrerer Teams
# Hier erstellen wir ein Auswahlfeld, mit dem der Nutzer mehrere Teams gleichzeitig auswählen kann.
# Die Methode st.sidebar.multiselect() erzeugt ein Dropdown-Menü mit Checkboxen.
# Die zurückgegebenen Werte (die ausgewählten Teams) speichern wir in der Variable selected_teams,
# weil wir sie später für die Filterung der Tabelle benötigen.
selected_teams = st.sidebar.multiselect(
    "Wähle Teamnamen:",    # Label über dem Auswahlfeld
    options=team_names,    # Liste aller auswählbaren Teams
    default=team_names     # Standard: alle Teams sind vorausgewählt, damit Tabelle nicht leer ist
)

# 6. Jahresbereich per Slider filtern
# Der Nutzer kann hier einen Bereich von Jahren auswählen (z. B. 1990 bis 2010).
# Wir holen uns dafür automatisch das kleinste und größte Jahr aus der Spalte "Jahr".
# Der Rückgabewert ist ein Tupel (z. B. (1995, 2005)), das wir später im Filter verwenden.
year_range = st.sidebar.slider(
    "Jahresbereich filtern",              # Label im UI
    int(df["Jahr"].min()),                # minimale Jahreszahl in den Daten
    int(df["Jahr"].max()),                # maximale Jahreszahl in den Daten
    (int(df["Jahr"].min()), int(df["Jahr"].max()))  # Default-Wert: alles ausgewählt
)

# 7. Daten filtern nach Teamnamen und Jahr
# Wir nutzen die Variable selected_teams (Liste der vom Nutzer gewählten Teams)
# und den year_range (untere und obere Jahresgrenze), um nur die passenden Zeilen zu zeigen.
# Die Methode .isin() prüft, ob der Teamname in der gewählten Liste enthalten ist.
# Die Methode .between() prüft, ob das Jahr zwischen start und end liegt.
df_filtered = df[
    (df["Team"].isin(selected_teams)) &                  # Teamname ist in der Auswahl
    (df["Jahr"].between(year_range[0], year_range[1]))   # Jahr liegt im gewählten Bereich
]

# 8. Ausgabe im Hauptbereich der App
# Hier zeigen wir der Nutzerin/dem Nutzer die gefilterten Ergebnisse in Tabellenform.
st.title("NHL Teams")           # Titel der Seite
st.dataframe(df_filtered)       # Tabelle mit den gefilterten Daten anzeigen




# LERNNOTIZEN 

# import streamlit as st
# → Lädt die Streamlit-Bibliothek für UI-Elemente wie Buttons, Filter etc.

# import pandas as pd
# → Lädt pandas für Datenanalyse, Tabellenstruktur & CSV-Verarbeitung

# df = pd.read_csv("teams.csv")
# → Liest eine lokale CSV-Datei ein und speichert sie im DataFrame df

# st.sidebar.header("...")
# → Erzeugt eine Überschrift im linken Seitenbereich der App

# st.sidebar.multiselect(...)
# → Zeigt ein Dropdown mit Checkboxen zur Mehrfachauswahl
# → Rückgabe: Liste der ausgewählten Optionen → speichern wir in selected_teams

# df["Team"].isin(selected_teams)
# → Prüft, ob der Teamname in der gewählten Liste enthalten ist

# df["Jahr"].between(x, y)
# → Prüft, ob ein Jahr zwischen x und y liegt

# st.sidebar.slider(...)
# → Erzeugt einen Schieberegler für einen Zahlenbereich (hier: Jahresfilter)

# st.dataframe(df_filtered)
# → Zeigt eine scrollbare, schön formatierte Tabelle mit den gefilterten Daten

# Warum brauchen wir Variablen wie selected_teams oder year_range?
# → Weil der Benutzer etwas auswählt – und wir diese Auswahl speichern müssen,
#    um später damit weiterzuarbeiten (z. B. Filter anwenden).