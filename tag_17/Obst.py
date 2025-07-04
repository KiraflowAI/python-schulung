import streamlit as st                       # Streamlit importieren für Web-App
import pandas as pd                         # Pandas für Datenmanagement
import plotly.express as px                 # Plotly Express für Diagramme

# Titel der App oben
st.title("Lieblingsobst der Klasse")

# --- Datenbasis: Tabelle mit Obstsorten und Infos ---
df = pd.DataFrame({
    "Obst": ["Apfel", "Banane", "Erdbeere", "Orange", "Traube"],            # Obstsorten
    "Stimmen": [8, 5, 6, 4, 3],                                            # Stimmen pro Obst
    "Farbe": ["Grün", "Gelb", "Rot", "Orange", "Lila"],                    # Obstfarben
    "Vitamin C (mg)": [12, 9, 60, 50, 4],                                 # Vitamin C in mg
    "Herkunft": ["Deutschland", "Ecuador", "Spanien", "Italien", "Griechenland"],  # Herkunft
    "Icon": ["🍏", "🍌", "🍓", "🍊", "🍇"],                                # Emoji zu jedem Obst
})

# --- Farbzuordnung für die Balken und Kreisdiagramm ---
farben_map = {
    "Apfel": "green",       # Grün für Apfel
    "Banane": "yellow",     # Gelb für Banane
    "Erdbeere": "red",      # Rot für Erdbeere
    "Orange": "orange",     # Orange für Orange
    "Traube": "purple"      # Lila für Traube
}

# Zwei Spalten, links breit, rechts schmal
col1, col2 = st.columns([2, 1])

# --- Balkendiagramm mit festen Farben ---
fig_bar = px.bar(
    df,
    x="Obst",                                # X-Achse zeigt Obstsorten
    y="Stimmen",                             # Y-Achse zeigt Anzahl Stimmen
    color="Obst",                           # Balkenfarbe nach Obstname
    color_discrete_map=farben_map,           # Verwende Farbzuordnung
    hover_data=["Farbe", "Vitamin C (mg)", "Herkunft"],  # Hoverinfos
    title="Stimmen für Lieblingsobst"       # Titel des Diagramms
)
fig_bar.update_layout(coloraxis_showscale=False)  # Farbskala ausblenden (nicht nötig)

# Diagramm in linke Spalte einfügen mit Interaktion
selected = col1.plotly_chart(fig_bar, use_container_width=True, on_select="rerun")
# on_select="rerun" sorgt dafür, dass bei Auswahl im Diagramm die App neu ausgeführt wird

# --- Kreisdiagramm mit gleichen Farben ---
fig_pie = px.pie(
    df,
    names="Obst",                  # Segmente nach Obstsorten
    values="Stimmen",              # Segmentgröße nach Stimmen
    color="Obst",                  # Farben nach Obst
    color_discrete_map=farben_map,  # Farbzuordnung wie im Balkendiagramm
    title="Prozentuale Stimmenverteilung"
)
# Kreisdiagramm unter Balkendiagramm anzeigen
col1.plotly_chart(fig_pie, use_container_width=True)

# --- Auswahl aus dem Balkendiagramm auswerten ---
try:
    indices = [selected["selection"]["points"][0]['curve_number']]  # Indizes der ausgewählten Balken
except Exception:
    indices = []   # Falls keine Auswahl getroffen wurde

# --- Details der ausgewählten Obstsorte anzeigen ---
with col2:
    if not indices:
        # Wenn keine Auswahl, Hinweis anzeigen
        st.info("👉 Klicke auf eine Obstsorte im Diagramm, um mehr zu erfahren.")
    else:
        # Index der ausgewählten Obstsorte
        index = indices[0]
        obst = df.iloc[index]  # Daten der ausgewählten Obstsorte holen
        
        # Farbwerte für Hintergrund nach Farbe des Obsts
        bg_color_map = {
            "Grün": "#2ecc71",
            "Gelb": "#f1c40f",
            "Rot": "#e74c3c",
            "Orange": "#e67e22",
            "Lila": "#9b59b6"
        }
        bg_color = bg_color_map.get(obst.Farbe, "#cccccc")  # Standard: Grau

        # Details als farbiger Kasten (HTML)
        st.markdown(
            f"""
            <div style="background-color: {bg_color}; padding: 20px; border-radius: 15px; color: white;">
                <h3>Details zu {obst.Icon} {obst.Obst}</h3>
                <ul>
                    <li><strong>Farbe:</strong> {obst.Farbe}</li>
                    <li><strong>Vitamin C:</strong> {obst['Vitamin C (mg)']} mg</li>
                    <li><strong>Typische Herkunft:</strong> {obst.Herkunft}</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

# Lernnotizen (step-by-step Erklärung):

# 1. Importieren der Bibliotheken:
#    - streamlit: Web-App Framework, mit dem man schnell UI bauen kann
#    - pandas: Datenanalyse und Tabellen-Handling
#    - plotly.express: Einfaches Erstellen von interaktiven Diagrammen

# 2. st.title("..."): Setzt den großen Titel oben auf der Seite

# 3. Datenbasis (DataFrame df):
#    - Enthält unsere Tabelle mit Obstsorten und Infos
#    - Jede Spalte ist eine Eigenschaft: Name, Stimmen, Farbe, Vitamin C, Herkunft, Icon (Emoji)

# 4. color_map:
#    - Python-Dictionary zur Zuordnung von Obstnamen zu bestimmten Farben
#    - Damit bekommen Balken und Torten im Diagramm die gleichen Farben

# 5. st.columns([2,1]):
#    - Erstellt zwei nebeneinanderliegende Container (Spalten)
#    - Die erste Spalte ist doppelt so breit wie die zweite

# 6. px.bar(...):
#    - Erstellt ein Balkendiagramm mit den Stimmen pro Obst
#    - color="Obst" färbt jeden Balken nach Obstname mit den Farben aus color_map
#    - hover_data zeigt weitere Infos, wenn man mit der Maus über die Balken fährt
#    - title zeigt eine Überschrift im Diagramm

# 7. col1.plotly_chart(..., on_select="rerun"):
#    - Zeigt das Balkendiagramm in der linken Spalte an
#    - on_select="rerun" sorgt dafür, dass beim Klicken auf einen Balken die App neu startet,
#      wodurch die aktuelle Auswahl gelesen und rechts angezeigt werden kann

# 8. px.pie(...):
#    - Erstellt ein Kreisdiagramm mit gleicher Farbgebung und Stimmen-Verteilung
#    - Zeigt prozentuale Anteile der Stimmen pro Obst

# 9. indices = selected["selection"]["point_indices"]:
#    - Liest die Indizes der ausgewählten Balken (hier eigentlich nur einer)
#    - Wird mit try/except abgesichert, falls nichts ausgewählt wurde

# 10. Rechte Spalte mit Details:
#     - Wenn nichts ausgewählt wurde, erscheint ein Hinweistext
#     - Ansonsten wird das Obst aus dem DataFrame per Index geholt
#     - Ein farbiger Kasten wird mit HTML formatiert, passend zur Obstfarbe
#     - Dort werden die Details (Farbe, Vitamin C, Herkunft, Emoji, Name) angezeigt

# 11. unsafe_allow_html=True:
#     - Erlaubt, dass wir HTML-Tags (z.B. div mit Hintergrundfarbe) in Streamlit anzeigen können

# So kannst du eine interaktive App bauen, die:

# - Daten übersichtlich zeigt
# - Interaktiv auf Klick reagiert
# - Details dynamisch aktualisiert
# - Farben konsistent anpasst
