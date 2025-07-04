import streamlit as st                           # Streamlit importieren, um Web-App zu bauen
import pandas as pd                             # Pandas für Tabellen/Datenmanipulation importieren
import plotly.express as px                     # Plotly Express für interaktive Diagramme importieren

# Titel der App oben anzeigen
st.title("Lieblingsobst der Klasse")

# --- Datenbasis: Tabelle mit Obstsorten und Infos ---
df = pd.DataFrame({
    "Obst": ["Apfel", "Banane", "Erdbeere", "Orange", "Traube"],        # Liste mit Obstsorten
    "Stimmen": [8, 5, 6, 4, 3],                                        # Anzahl Stimmen je Obst
    "Farbe": ["Rot", "Gelb", "Rot", "Orange", "Violett"],              # Farbe jeder Obstsorte
    "Vitamin C (mg)": [12, 9, 60, 50, 4],                              # Vitamin C Gehalt in mg
    "Herkunft": ["Deutschland", "Ecuador", "Spanien", "Italien", "Griechenland"],  # Herkunftsländer
    "Icon": ["🍎", "🍌", "🍓", "🍊", "🍇"],                             # Emoji passend zum Obst
})

# Spaltenlayout mit zwei Spalten: linke Spalte doppelt so breit wie rechte
col1, col2 = st.columns([2, 1])

# --- Balkendiagramm mit benutzerdefinierten Farben ---
# Farbzuordnung: jedem Obst wird eine feste Farbe zugewiesen
color_map = {
    "Apfel": "green",
    "Banane": "yellow",
    "Erdbeere": "red",
    "Orange": "orange",
    "Traube": "purple"
}

# Erstelle Balkendiagramm mit Plotly Express
fig = px.bar(
    df,
    x="Obst",                            # X-Achse zeigt Obstsorten
    y="Stimmen",                        # Y-Achse zeigt Anzahl Stimmen
    hover_data=["Farbe", "Vitamin C (mg)", "Herkunft"],  # Zusätzliche Infos beim Hovern
    color="Obst",                       # Farbe abhängig von Obstsorten
    color_discrete_map=color_map,       # Unsere benutzerdefinierten Farben verwenden
    title="Stimmen für Lieblingsobst"   # Titel des Diagramms
)

# Balkendiagramm in der linken Spalte anzeigen, mit Interaktivität und Auswahlfunktion
selected = col1.plotly_chart(fig, on_select="rerun")  # on_select "rerun" sorgt für Neuladen beim Klick

# --- Kreisdiagramm für prozentuale Verteilung ---
fig_pie = px.pie(
    df,
    names="Obst",                        # Segmente werden nach Obstsorten benannt
    values="Stimmen",                   # Segmentgröße entspricht Anzahl Stimmen
    color="Obst",                      # Gleiche Farbzuordnung wie Balkendiagramm
    color_discrete_map=color_map,
    title="Prozentuale Stimmenverteilung"
)

# Kreisdiagramm direkt unter dem Balkendiagramm anzeigen (gleiche Spalte)
col1.plotly_chart(fig_pie, use_container_width=True)

# --- Auswahl im Balkendiagramm auswerten und Details in rechter Spalte anzeigen ---
indices = selected["selection"]["point_indices"]  # Index der ausgewählten Balken

with col2:
    if not indices:
        # Wenn nichts ausgewählt ist, Hinweis anzeigen
        st.info("👉 Klicke auf eine Obstsorte im Diagramm, um mehr zu erfahren.")
    else:
        # Ausgewähltes Obst anhand Index aus DataFrame holen
        obst = df.iloc[indices[0]]
        # Überschrift mit Emoji und Obstname
        st.subheader(f"Details zu {obst.Icon} {obst.Obst}")
        # Details als Markdown-Liste
        st.markdown(f"""
        - **Farbe**: {obst.Farbe}  
        - **Vitamin C**: {obst['Vitamin C (mg)']} mg  
        - **Typische Herkunft**: {obst.Herkunft}
        """)

# Lernnotizen:
# - st.title: Zeigt einen großen Titel über der gesamten App an
# - pd.DataFrame: Datenstruktur zur Tabellendarstellung (Zeilen & Spalten)
# - st.columns: Erzeugt nebeneinanderliegende Spalten in der App
# - px.bar: Erstellt ein interaktives Balkendiagramm
# - color_discrete_map: Definiert individuelle Farben für Kategorien
# - col.plotly_chart: Zeigt ein Plotly-Diagramm in der jeweiligen Spalte an
# - on_select="rerun": Löst einen Neu-Ladevorgang aus, wenn im Diagramm ausgewählt wird
# - selected["selection"]["point_indices"]: Gibt Indizes der ausgewählten Balken zurück
# - st.info: Zeigt eine Informations-Box mit Hinweis an
# - st.subheader: Zeigt eine kleinere Überschrift in der App
# - st.markdown: Zeigt formatierte Texte mit Markdown-Syntax

