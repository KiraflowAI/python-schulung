
# ============================================================
# 🧠 Lernnotizen 
# ============================================================

# import streamlit as st         → lädt das Streamlit-Modul
# TITLE_EN / TITLE_DE           → Titel in Englisch & Deutsch
# POSTER_URL / TRAILER_URL      → URLs für Bild und YouTube-Trailer
# INFO = { ... }                → Dictionary für zentrale Filminfos
# CAST_MAIN = [ ... ]           → Liste der Hauptdarsteller:innen
# SUMMARY = "..."               → Zusammenfassung als mehrzeiliger Text

# with st.container():          → gruppiert Inhalte wie Bild + Titel zusammen
# st.columns([1, 2])            → teilt Seite in zwei Spalten (1:2 Verhältnis)
# st.image(...)                 → Bild anzeigen
# st.title(...)                 → große Überschrift (h1)
# st.caption(...)               → kleine graue Unterzeile
# st.metric(label, value)      → zeigt Kennzahlen (KPIs), z. B. Bewertung, Umsatz
# st.write(...)                 → zeigt Text, HTML oder DataFrame
# st.tabs([...])               → erstellt Reiter/Tabs zum Wechseln
# st.subheader(...)            → mittlere Überschrift (h2/h3)
# st.expander(...)             → aufklappbares Textfeld
# st.markdown(...)             → zeigt formatierten Markdown-Text
# st.sidebar                   → extra Bereich an der Seite mit Infos/Links






import streamlit as st  # Streamlit-Modul importieren

# ------------------------------------------------------------
# 🎬 Basis-Informationen zum Film "Avatar"
# ------------------------------------------------------------

# Titel auf Deutsch und Englisch – für Anzeige im Titelbereich
TITLE_DE = "Aufbruch nach Pandora"
TITLE_EN = "Avatar"

# Direktlink zum Posterbild (muss auf .jpg oder .png enden)
POSTER_URL = "https://m.media-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_FMjpg_UX1000_.jpg"

# YouTube-Link zum Trailer
TRAILER_URL = "https://www.youtube.com/watch?v=EYHuoBjmQQg"

# Infos zum Film als Dictionary – für zentrale Nutzung
INFO = {
    "Jahr": "2009",
    "Regie": "James Cameron",
    "Laufzeit": "162 Min.",
    "Genre": "Sci-Fi / Fantasy",
    "IMDb Rating": "7.9 / 10",
    "Budget": "237 Mio. USD",
    "Box Office": "2,9 Mrd. USD",  # wird als "Einnahmen aus Kinotickets" angezeigt
}

# Liste mit Hauptdarsteller:innen
CAST_MAIN = [
    "Sam Worthington – Jake Sully",
    "Zoe Saldana – Neytiri",
    "Sigourney Weaver – Dr. Grace Augustine",
    "Stephen Lang – Colonel Quaritch",
    "Giovanni Ribisi – Parker Selfridge",
    "Michelle Rodriguez – Trudy Chacón",
]

# Zusammenfassung als mehrzeiliger String
SUMMARY = (
    "**Avatar** spielt im Jahr 2154 auf dem Mond **Pandora**, wo Menschen "
    "den wertvollen Rohstoff Unobtanium abbauen. Der gelähmte Ex-Marine **Jake Sully** "
    "wird in ein Avatar-Programm versetzt und soll die Na'vi infiltrieren – doch seine "
    "Reise verändert alles. Der Film gilt als visuelles Meisterwerk mit tiefgreifender "
    "Natur- und Gesellschaftskritik."
)

# ------------------------------------------------------------
# 🎨 Layout: Kopfbereich mit Poster, Titel, Zahlen & Beschreibung
# ------------------------------------------------------------
with st.container():  # Container für gruppiertes Layout
    col_poster, col_title = st.columns([1, 2], gap="large")  # Zwei Spalten nebeneinander

    with col_poster:
        st.image(POSTER_URL, use_container_width=True)  # Posterbild anzeigen

    with col_title:
        st.title(f"{TITLE_EN} – {TITLE_DE}")  # Großer Titel (h1)
        st.caption(INFO["Jahr"] + " | " + INFO["Laufzeit"] + " | Regie: " + INFO["Regie"])  # Kleine Unterzeile

        # Drei Kennzahlen (Metriken) nebeneinander anzeigen
        m1, m2, m3 = st.columns(3)
        m1.metric("IMDb Rating", INFO["IMDb Rating"])  # Bewertung
        m2.metric("Budget", INFO["Budget"])            # Produktionskosten
        m3.metric("Einnahmen aus Kinotickets", INFO["Box Office"])  # Umsätze

        st.write(SUMMARY)  # Textbeschreibung ausgeben

# ------------------------------------------------------------
# 📂 Tabs: Überblick | Hauptcast | Media
# ------------------------------------------------------------
overview_tab, cast_tab, media_tab = st.tabs(["Überblick", "Hauptcast", "Media"])

# ➤ Tab 1: Überblick
with overview_tab:
    st.subheader("Kurze Zusammenfassung")
    st.write(SUMMARY)

    # Klappbox für Zusatzinfos
    with st.expander("Auszeichnungen & Highlights"):
        st.markdown("""
        * 3 **Oscars** (Beste Kamera, Beste visuelle Effekte, Bestes Szenenbild)  
        * Über 100 weitere Preise weltweit  
        * Revolutionäre 3D-Technik & Motion-Capture
        """)

# ➤ Tab 2: Hauptdarsteller
with cast_tab:
    st.subheader("Besetzung – Hauptrollen")
    st.write("\n".join([f"- {member}" for member in CAST_MAIN]))  # Zeilenweise Darstellung

# ➤ Tab 3: Trailer-Video
with media_tab:
    st.subheader("Trailer")
    st.video(TRAILER_URL)  # Video-Embed via YouTube-Link

# ------------------------------------------------------------
# 📑 Sidebar – zeigt Zusatzinfos und Links
# ------------------------------------------------------------
with st.sidebar:
    st.header("🎬 Filminfo")  # Überschrift in Sidebar
    st.metric("IMDb", INFO["IMDb Rating"])  # Wiederholung der Bewertung

    # Weitere Detailinfos
    st.markdown(f"*Regie:* {INFO['Regie']}")
    st.markdown(f"*Genre:* {INFO['Genre']}")
    st.markdown(f"*Jahr:* {INFO['Jahr']}")

    # Externe Links
    st.header("🔗 Externe Links")
    st.markdown("""
    * [IMDb-Seite](https://www.imdb.com/title/tt0499549/)
    * [Wikipedia (de)](https://de.wikipedia.org/wiki/Avatar_–_Aufbruch_nach_Pandora)
    """)

