import streamlit as st               # Streamlit importieren, Framework für Web-Apps
import pandas as pd                 # Pandas importieren,  fürTabellen und Daten 
import plotly.express as px         # Plotly Express importieren für interaktive Diagramme
import requests                     # Requests importieren, um Daten von einer Internet-URL abzurufen
from datetime import datetime       # datetime importieren für Datum und Zeitfunktionen
import pytz                        # pytz importieren für Zeitzonen-Unterstützung

####################-------------------------###########################--------------------#########

# Hintergrundfarbe definieren
# Hier speichern wir CSS-Code als mehrzeiligen String
page_bg_img = '''                   
<style>                            # CSS startet hier
    .stApp {                      # stApp ist die Hauptklasse der Streamlit-App, sie umfasst die ganze Seite
        background-color: #2c3e50; /* Dunkelblaue Farbe als Hintergrund */
    }
</style>                         
'''
 # CSS Ende

####################-------------------------###########################--------------------#########

st.markdown(page_bg_img, unsafe_allow_html=True)  # Streamlit rendert das CSS, erlaubt HTML (unsafe_allow_html=True)
# page_bg_img ist eine Variable, die hier einen mehrzeiligen String (Textblock) enthält — in deinem Fall ist das ein CSS-Code-Snippet (für Design und Styling der Webseite).

# Funktion definieren, die Erdbebendaten von einer URL abruft
@st.cache_data(ttl=120)            # Streamlit speichert (cached) das Ergebnis für 120 Sekunden, um nicht bei jedem Neuladen die API zu belasten
def fetch_earthquake_data(url):   # Funktion fetch_earthquake_data nimmt eine URL als Eingabeparameter (url)
    response = requests.get(url)   # HTTP GET Anfrage an die URL, um Daten abzuholen (response ist die Antwort)
    data = response.json()         # Antwort in JSON-Format umwandeln, sodass wir es als Python-Objekt (Dictionary) nutzen können
    
    features = data['features']    # Das JSON-Objekt enthält 'features' – Liste von Erdbeben-Datensätzen
    earthquakes = []               # Leere Liste, in die wir später die aufbereiteten Erdbeben speichern
    
    for feature in features:       # Für jedes einzelne Erdbeben (feature) in der Liste
        properties = feature['properties']  # Eigenschaften (Ort, Magnitude, Zeit) auslesen
        geometry = feature['geometry']      # Geometrische Daten (Koordinaten)

# @st.cache_data(ttl=120) über deine Funktion schreibst, passiert Folgendes:

# Streamlit merkt sich das Ergebnis (Return-Wert) dieser Funktion.

# Wenn die Funktion innerhalb von 120 Sekunden nochmal mit denselben Eingabeparametern aufgerufen wird, wird das Ergebnis nicht neu berechnet, sondern direkt aus dem Cache (Zwischenspeicher) zurückgegeben.

# Das spart Zeit und Ressourcen — z.B. bei aufwendigen API-Anfragen oder komplexen Berechnungen.

# Nach 120 Sekunden wird das Ergebnis gelöscht und bei nächstem Aufruf neu berechnet.
####################-------------------------###########################--------------------#########

        # Zeit wird in UTC (koordinierte Weltzeit) umgewandelt
        utc_time = pd.to_datetime(properties['time'], unit='ms')  
        # properties['time'] ist Zeit in Millisekunden seit 1.1.1970 (Unix-Zeit)
        # pd.to_datetime wandelt das in ein Datum um
        
        # Zeit wird in lokale Zeitzone konvertiert (hier Los Angeles)
        local_time = utc_time.tz_localize('UTC').tz_convert(pytz.timezone('America/Los_Angeles'))
        
        # Füge alle wichtigen Daten in die Liste ein (als Dictionary)
        earthquakes.append({
            "place": properties['place'],      # Ort des Erdbebens, z.B. "California"
            "magnitude": properties['mag'],    # Stärke des Erdbebens
            "time_utc": utc_time,               # Zeitpunkt in UTC (Standardzeit)
            "time_local": local_time,           # Zeitpunkt in lokaler Zeit (LA)
            "latitude": geometry['coordinates'][1],  # Breitengrad (Y-Koordinate)
            "longitude": geometry['coordinates'][0]  # Längengrad (X-Koordinate)
        })
    
    return pd.DataFrame(earthquakes)   # Die Liste in einen DataFrame umwandeln, damit wir gut damit arbeiten können

# URL mit den aktuellen Erdbebendaten (letzte 30 Tage)
realtime_url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"
df = fetch_earthquake_data(realtime_url)  # Daten laden und in der Variable df (DataFrame) speichern

####################-------------------------###########################--------------------#########


# Sidebar mit zwei Buttons zum Filtern nach Stärke
with st.sidebar:                      # Alles in diesem Block erscheint in der Seitenleiste
    st.markdown("### Filter")         # Überschrift in der Sidebar
    
    # Button für starke Erdbeben, bei Klick filtere df auf Magnitude > 5
    if st.button("🔴 Starke Erdbeben innerhalb der 30 Tage"):  
        # df[df["magnitude"] > 5] heißt: filtere alle Zeilen aus df, bei denen in Spalte "magnitude" der Wert größer als 5 ist
        df = df[df["magnitude"] > 5]
    
    # Button für schwache Erdbeben, bei Klick filtere df auf Magnitude <= 5
    if st.button("🟢 Schwache Erdbeben innerhalb 30 Tage"):
        df = df[df["magnitude"] <= 5]


####################-------------------------###########################--------------------#########


# Titel der Seite
st.title("Erdbeben Monitoring")  # Groß und fett, ganz oben

# Anzahl der Erdbeben bestimmen und anzeigen
count_of_earthquakes = df.shape[0]  # .shape gibt (Anzahl Zeilen, Anzahl Spalten), [0] holt Anzahl der Zeilen (=Erdbeben)
st.text(f"In den letzten 30 Tagen gabe es insgesamt {count_of_earthquakes} Erdbeben.")

# Zwei Spalten nebeneinander anlegen
col1, col2 = st.columns(2)           # col1 und col2 sind zwei Container nebeneinander

# Frühestes Erdbeben ermitteln (Datum)
earliest_date = df.time_utc.min().date()  
# df.time_utc = Spalte mit Zeitpunkt als Timestamp (Datum+Uhrzeit)
# .min() nimmt das früheste Datum heraus
# .date() entfernt die Uhrzeit, damit nur Datum bleibt

# Datumsauswahl "Von" (Anfangsdatum) in der linken Spalte
from_date = col1.date_input(
    label="Von",                 # Text über dem Eingabefeld
    value=earliest_date,         # Standardwert (frühestes Datum)
    min_value=earliest_date,     # Kleinster wählbarer Wert
    max_value='today'            # Größter wählbarer Wert (heutiges Datum)
)

# Datumsauswahl "Bis" (Enddatum) in der rechten Spalte
end_date = col2.date_input(
    label="Bis",
    value='today',               # Standardwert: heutiges Datum
    min_value=earliest_date,
    max_value='today'
)

# Fehlerbehandlung, falls Enddatum vor Anfang liegt
if end_date < from_date:
    st.error("Startdatum darf nicht vor Enddatum liegen.")  # Rote Fehlermeldung

# DataFrame nach ausgewähltem Zeitraum filtern
df_zeitraum = df[
    (df.time_utc.dt.date >= from_date) &    # Alle Zeilen, wo Datum >= Startdatum
    (df.time_utc.dt.date <= end_date)       # UND Datum <= Enddatum
]

# Große Kachel mit Anzahl der Erdbeben im Zeitraum
st.metric("Erdbeben im Zeitraum", df_zeitraum.shape[0])  
# st.metric zeigt eine prominent hervorgehobene Zahl an

# Anzahl der Erdbeben pro Tag gruppieren und zählen
anzahl_df = df_zeitraum.groupby(df_zeitraum.time_utc.dt.date).size()
# groupby gruppiert nach Datum (.dt.date entfernt Uhrzeit)
# .size() zählt Anzahl der Einträge pro Gruppe (pro Tag)

# Balkendiagramm erstellen mit Plotly Express
fig_bar = px.bar(anzahl_df, title="Erdbebeneinträge pro Tag", color_discrete_sequence=["#14FFFB"])

fig_bar.update_layout(
    xaxis_title="Datum",           # Beschriftung X-Achse
    yaxis_title="Anzahl Erdbeben"  # Beschriftung Y-Achse
)

fig_bar.update(layout_showlegend=False)  # Legende deaktivieren, da nicht nötig

# Balkendiagramm in der App anzeigen
st.plotly_chart(fig_bar, theme="streamlit")  
# theme="streamlit" sorgt für konsistentes Aussehen


####################-------------------------###########################--------------------#########


# Interaktive Weltkarte mit Erdbebenpunkten
fig_earth = px.scatter_map(
    df_zeitraum.query("magnitude > 0"),    # Nur Erdbeben mit Magnitude größer 0 anzeigen
    lat="latitude",                        # Latitude (Breitengrad)
    lon="longitude",                      # Longitude (Längengrad)
    color="magnitude",                    # Punktfarbe entspricht Magnitude
    color_continuous_scale=px.colors.sequential.Viridis,  
    # Viridis ist ein Farbverlauf von Dunkelviolett über Gelb bis Grün
    hover_name="place",                   # Tooltip zeigt Ort an
    hover_data={"time_utc": True, "time_local": True, "magnitude": True},  
    # Weitere Daten im Tooltip anzeigen (UTC, lokal, Magnitude)
    zoom=1,                              # Zoom-Level 1 zeigt Weltkarte komplett
    height=600,                         # Höhe der Karte in Pixeln
    title="Karte mit geografischen Daten"                      # Titel der Karte
)

# Karte in der Streamlit-App anzeigen
st.plotly_chart(fig_earth)

# Aufklappbarer Bereich mit tabellarischer Ansicht der Daten
with st.expander("Daten im Zeitraum anzeigen"):
    st.dataframe(df_zeitraum)            # Zeige die Tabelle mit allen Erdbeben-Daten im Zeitraum

# Unterüberschrift für zusätzlichen Kontext
st.subheader("Tektonische Platten")

####################-------------------------###########################--------------------#########


# Bild der tektonischen Platten einbinden
#st.image("https://getech.com/wp-content/uploads/2020/09/tectonic-plates-map-world.png")
st.image("https://images.nationalgeographic.org/image/upload/t_edhub_resource_key_image/v1638892366/EducationHub/photos/tectonic-plate-map.jpg")













#### LERNNOTIZEN ####
#                       2. Funktion: Daten von Erdbeben laden

# import streamlit as st: Lädt das Streamlit-Framework, mit dem du interaktive Web-Apps bauen kannst. Ab jetzt kannst du mit st Befehle an Streamlit senden, z.B. st.title() zeigt eine Überschrift an.

# import pandas as pd: Lädt die Bibliothek Pandas, die dir hilft, Daten in Tabellenform (DataFrames) zu lesen und zu bearbeiten.

# import plotly.express as px: Importiert Plotly Express, ein Tool für interaktive Diagramme.

# import requests: Bibliothek, um HTTP-Anfragen zu machen, z.B. um Daten aus dem Internet herunterzuladen.

# from datetime import datetime: Importiert die Klasse für Datum und Zeit, z.B. um Zeiten zu manipulieren.

# import pytz: Bibliothek für Zeitzonen; hier wird damit die Zeit in die richtige Ortszeit umgerechnet.

# @st.cache_data(ttl=120): Das ist ein sogenannter Decorator. Er sorgt dafür, dass Streamlit die Funktion cached (speichert), damit sie nicht bei jedem Aufruf neu ausgeführt wird. ttl=120 heißt, der Cache wird nach 120 Sekunden erneuert.

# def fetch_earthquake_data(url):: Definiert eine Funktion namens fetch_earthquake_data, die eine URL als Eingabe bekommt und Daten von dort lädt.

# response = requests.get(url): Holt die Daten von der Webseite (HTTP GET Request).

# data = response.json(): Wandelt die Antwort (im JSON-Format) in ein Python-Dictionary um.

# features = data['features']: Nimmt die Erdbeben-Daten heraus.

# earthquakes = []: Erstellt eine leere Liste, in der die Daten gesammelt werden.

# for feature in features:: Geht jede einzelne Erdbebenmeldung durch.

# properties = feature['properties']: Holt die Infos zum Erdbeben (Ort, Zeit, Stärke).

# geometry = feature['geometry']: Holt die Koordinaten (Breiten-/Längengrad).

# utc_time = pd.to_datetime(properties['time'], unit='ms'): Wandelt die Zeit von Millisekunden seit Epoch in ein Datum/Uhrzeit um.

# local_time = utc_time.tz_localize('UTC').tz_convert(pytz.timezone('America/Los_Angeles')): Konvertiert die UTC-Zeit in die Ortszeit von Los Angeles.

# earthquakes.append({...}): Fügt ein Dictionary mit den wichtigen Infos zur Liste hinzu.

# return pd.DataFrame(earthquakes): Wandelt die Liste in eine Pandas-Tabelle um und gibt sie zurück.

                            #2.  Daten laden und App-Titel anzeigen

        # realtime_url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"
        # df = fetch_earthquake_data(realtime_url)

        # st.title("Erdbeben Visualisierung")
        # Definiert die URL, wo die aktuellen Erdbebendaten liegen.

        # Ruft die Funktion auf, um die Daten zu laden und in df (DataFrame) zu speichern.

        # Zeigt den Titel „Erdbeben Visualisierung“ auf der Webseite an.

                            # 3. Anzahl der Erdbeben anzeigen

        # count_of_earthquakes = df.shape[0]
        # st.text(f"In den letzten 30 Tagen gabe es insgesamt {count_of_earthquakes} Erdbeben.")
        # df.shape[0]: Anzahl der Zeilen in der Tabelle, also wie viele Erdbeben gemeldet wurden.

        # st.text(...): Zeigt den Text auf der Webseite an, mit der Anzahl der Erdbeben.

                            # 4. Zwei Spalten für Datumsauswahl
        # col1, col2 = st.columns(2)

        # earliest_date = df.time_utc.min().date()

        # from_date = col1.date_input(label="Von", value=earliest_date, min_value=earliest_date, max_value='today')
        # end_date = col2.date_input(label="Bis", value='today', min_value=earliest_date, max_value='today')
        # st.columns(2): Teilt die Seite in zwei nebeneinanderliegende Bereiche (Spalten).

        # earliest_date: Ältestes Erdbeben-Datum aus den Daten.

        # col1.date_input(...): Datumsauswahl im ersten Bereich, mit Startwert dem frühesten Datum.

        # col2.date_input(...): Datumsauswahl im zweiten Bereich, Startwert heute.

                            # 5 Fehlerbehandlung für Datumsauswahl
        # if end_date < from_date:
        #     st.error("Startdatum darf nicht vor Enddatum liegen.")
        # Wenn das Enddatum vor dem Startdatum liegt, zeigt Streamlit eine Fehlermeldung an.

                            # 6 Filterung nach Zeitraum

# df_zeitraum = df[(df.time_utc.dt.date >= from_date) & (df.time_utc.dt.date <= end_date)]
# Filtert die Tabelle, sodass nur Erdbeben innerhalb des ausgewählten Datumsbereichs angezeigt werden.

                            # 7 Anzeige der Anzahl Erdbeben im Zeitraum

# st.metric("Erdbeben im Zeitraum", df_zeitraum.shape[0])
# Zeigt eine Metrik an mit der Anzahl der Erdbeben im ausgewählten Zeitraum.

                            # 8 Tagesweise Anzahl der Erdbeben gruppieren

# anzahl_df = df_zeitraum.groupby(df_zeitraum.time_utc.dt.date).size()
# Gruppiert die Erdbeben nach Datum und zählt die Anzahl pro Tag.

                            # 9 Balkendiagramm der täglichen Erdbeben

# fig_bar = px.bar(anzahl_df, title="Einträge pro Tag",)
# fig_bar.update(layout_showlegend=False)
# st.plotly_chart(fig_bar, theme="streamlit")
# Erstellt mit Plotly ein Balkendiagramm der täglichen Anzahl der Erdbeben.

# Versteckt die Legende.

# Zeigt das Diagramm in Streamlit an.


                            # 10  Karte mit Erdbeben-Standorten (Scatter Map)

# fig_earth = px.scatter_map(
#     df_zeitraum.query("magnitude > 0"),
#     lat="latitude",
#     lon="longitude",
#     color="magnitude",
#     hover_name="place",
#     hover_data={"time_utc": True, "time_local": True, "magnitude": True},
#     zoom=1,
#     height=600,
#     title="Geomap"
# )
# st.plotly_chart(fig_earth)
# Zeigt eine Karte mit Punkten für jedes Erdbeben (nur Magnitude > 0).

# Punkte färben sich je nach Stärke.

# Zeigt beim Drüberfahren mit der Maus Ort, Zeit und Stärke.

# Zoomstufe und Größe der Karte sind definiert.

# Karte wird in Streamlit angezeigt.

                        # 11 Tabelle mit Erdbeben-Daten einklappbar anzeigen

# with st.expander("Daten im Zeitraum anzeigen"):
#     st.dataframe(df_zeitraum)
# Zeigt eine einklappbare Tabelle mit den Erdbeben-Daten im gewählten Zeitraum.


                         # 12 Unterüberschrift und Bild (tektonische Platten)

# st.subheader("Tektonische Platten")
# st.image("https://getech.com/wp-content/uploads/2020/09/tectonic-plates-map-world.png")
# Zeigt eine kleine Überschrift.

# Lädt und zeigt ein Bild von tektonischen Platten.

# Importe bringen dir alle nötigen Funktionen und Bibliotheken.

# Funktion fetch_earthquake_data holt die Daten, verarbeitet sie und wandelt sie in eine Tabelle.

# Streamlit-Kommandos zeigen Titel, Texte, Tabellen, Eingabefelder und Diagramme an.

# Filter und Fehlerchecks sorgen dafür, dass nur gewünschte Daten angezeigt werden und Eingaben sinnvoll sind.

# Plotly-Diagramme visualisieren die Daten interaktiv auf der Webseite.