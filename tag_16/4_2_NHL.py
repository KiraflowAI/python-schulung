# ------------------------------------------------------------
# NHL Teams Visualisierung mit Plotly (2 Diagrammtypen)
# ------------------------------------------------------------

import streamlit as st              # Streamlit importieren, damit wir Web-App bauen können
import pandas as pd                 # Pandas importieren, um Tabellen (CSV) zu laden und zu bearbeiten
import plotly.express as px         # Plotly Express importieren, um interaktive Diagramme zu erstellen

# CSV-Datei laden, die im gleichen Ordner liegt wie dieses Script
df = pd.read_csv("tag_16/teams.csv")      

# Titel der App, wird ganz oben auf der Webseite angezeigt
st.title("NHL Teams - Datenvisualisierung")  

# Spalte "Jahr" als ganze Zahlen (Integer) sicherstellen, für Filter und Diagramme
df["Jahr"] = df["Jahr"].astype(int)   

# Alle eindeutigen Teamnamen holen und alphabetisch sortieren
team_names = sorted(df["Team"].unique())    

# Mehrfachauswahl-Menü für Teams, damit Nutzer mehrere Teams auswählen können
selected_teams = st.multiselect(
    "Wähle Teamnamen aus",              # Beschriftung oberhalb des Menüs
    options = team_names,                 # Optionen sind alle Teams aus den Daten
    default = team_names[:3]              # Standardmäßig sind die ersten drei Teams ausgewählt
)

# Minimales und maximales Jahr aus den Daten ermitteln, für den Slider
min_year = df["Jahr"].min()            
max_year = df["Jahr"].max()

# Schieberegler (Slider) für die Filterung nach Zeitraum (Jahre)
year_range = st.slider(
    "Jahresbereich auswählen",          # Beschriftung für den Slider
    min_value = min_year,                  # Kleinster Wert im Slider
    max_value = max_year,                  # Größter Wert im Slider
    value = (min_year, max_year),          # Startwert: gesamter Zeitraum ausgewählt
    step = 1                              # Schrittweite des Sliders ist 1 Jahr
)

# Gefilterte Daten erstellen, nur ausgewählte Teams UND Jahre anzeigen
df_filtered = df[
    (df["Team"].isin(selected_teams)) &                 # Filter: Team ist in der Auswahl
    (df["Jahr"].between(year_range[0], year_range[1])) # Filter: Jahr liegt im gewählten Zeitraum
]

# Einklappbarer Bereich, der die gefilterten Daten in Tabellenform anzeigt
st.expander("Gefilterte Daten anzeigen").dataframe(df_filtered, use_container_width=True)

# Überschrift für die Diagrammsektion
# 1. Balkendiagramm (Gesamtsiege pro Team)

st.markdown("### Balkendiagramm: Gesamtsiege pro Team")

# Gesamtsiege pro Team summieren
siege_sum = df_filtered.groupby("Team")["Siege"].sum().reset_index()

# Prüfen, ob Daten vorhanden sind
if siege_sum.empty:
    st.info("Keine Daten für Balkendiagramm.")
else:
    # Balkendiagramm erstellen
    fig_bar = px.bar(
        siege_sum,
        x = "Team",                # X-Achse: Teamnamen
        y = "Siege",               # Y-Achse: Summe der Siege
        title="Gesamtsiege pro Team im gewählten Zeitraum",
        text="Siege"             # Werte auf den Balken anzeigen
    )
    fig_bar.update_traces(textposition='outside')  # Text über den Balken anzeigen
    st.plotly_chart(fig_bar, use_container_width=True)

# === 2. Scatter Plot (Tore gegen Niederlagen) ===

st.markdown("### Scatter Plot: Tore gegen Niederlagen")

# Prüfen, ob nach Filterung noch Daten vorhanden sind
if df_filtered.empty:
    st.info("Keine Daten für Scatter Plot.")
else:
    # Scatterplot erstellen: X = GF (Goals For), Y = Niederlagen (Losses)
    fig_scatter = px.scatter(
        df_filtered,
        x="GF",                   # X-Achse: erzielte Tore
        y="Niederlagen",          # Y-Achse: Niederlagen
        color="Team",             # Farbe der Punkte nach Team
        size="Siege",             # Größe der Punkte nach Anzahl Siege
        hover_name="Team",        # Beim Überfahren mit der Maus den Teamnamen anzeigen
        title="Zusammenhang zwischen Toren (GF) und Niederlagen"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)




