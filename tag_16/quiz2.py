# ------------------------------------------------------------
#  Science & Nature Quiz 
# ------------------------------------------------------------

# Import der notwendigen Bibliotheken
import streamlit as st  # Streamlit ist das Web-Framework für interaktive Apps
import pandas as pd     # Pandas hilft beim Lesen und Verarbeiten von CSV-Tabellen
import base64           # Base64 wandelt Binärdaten (z.B. GIFs) in HTML-kompatible Strings um

# Funktion zum Abspielen von Audio-Dateien (MP3 oder WAV)
def play_audio(url):
    # Fügt ein HTML Audio-Element ein, das automatisch startet (autoplay)
    st.markdown(f"""
        <audio autoplay>
            <source src="{url}" type="audio/mpeg">
        </audio>
        """, unsafe_allow_html=True)

# Funktion zum Anzeigen eines GIF-Bildes per URL
def show_gif(url):
    # Zeigt ein Bild mit der angegebenen URL und 300 Pixel Breite
    st.image(url, width=300)

# Haupttitel der App, wird ganz oben im Browser angezeigt
st.title("🌿 Science & Nature Quiz")

# Ein ausklappbares Infokästchen mit Anleitung zur CSV-Datei
with st.expander("ℹ️ Anleitung zur CSV-Datei anzeigen"):
    # Zeige mit Markdown Text an, wie die CSV-Datei aufgebaut sein muss
    st.markdown("""
    Die CSV-Datei muss folgende Spalten enthalten:

    | frage | option0 | option1 | option2 | option3 | richtige_option | quelle |
    |-------|---------|---------|---------|---------|-----------------|--------|
    | Was ist 2 + 2? | 3 | 4 | 5 | 6 | 1 | https://example.com |

    - option0 bis option3: Vier Antwortmöglichkeiten
    - richtige_option: Index der korrekten Antwort (0-basiert)
    - quelle: Link zur akademischen Quelle (optional)
    """)

# Datei-Upload-Feld: Nutzer*innen können hier eine eigene CSV hochladen
upload = st.file_uploader("📁 Lade deine eigene CSV hoch", type="csv")

# Falls eine Datei hochgeladen wurde, versuche sie zu lesen
if upload is not None:
    try:
        df = pd.read_csv(upload)      # CSV in einen DataFrame laden
        st.success("✅ CSV erfolgreich geladen!")  # Erfolgsmeldung anzeigen
    except Exception as e:
        st.error(f"❌ Fehler beim Einlesen: {e}")  # Fehlermeldung anzeigen, wenn Lesen fehlschlägt
        st.stop()                                # Programm anhalten
else:
    # Wenn keine Datei hochgeladen, Standard-CSV laden
    st.info("ℹ️ Keine Datei hochgeladen. Standard-Quiz wird verwendet.")
    df = pd.read_csv("/Users/burcukiran/Desktop/Schulungen/python-schulung/tag_16/fragen.csv")

# Leeres Dictionary zum Speichern der Nutzerantworten vorbereiten
antworten = {}

# Quizformular starten: alle Fragen und Antwortmöglichkeiten werden angezeigt
with st.form("quiz_form"):
    # Iteriere über jede Zeile (Frage) im DataFrame
    for i, row in df.iterrows():
        frage = row["frage"]                                       # Fragetext auslesen
        options = [row[f"option{j}"] for j in range(4)]           # Vier Antwortoptionen auslesen
        antwort = st.radio(f"{i+1}. {frage}", options, key=i)     # Radiobutton zur Auswahl anzeigen
        antworten[i] = antwort                                     # Antwort unter Frageindex speichern
    submitted = st.form_submit_button("✅ Quiz abschicken")        # Button zum Absenden des Formulars

# Wenn das Formular abgeschickt wurde, die Antworten auswerten
if submitted:
    st.subheader("📊 Deine Auswertung")                           # Überschrift der Auswertung
    punkte = 0                                                  # Punkte-Startwert auf 0 setzen

    # Für jede Frage prüfen, ob Antwort korrekt ist
    for i, row in df.iterrows():
        richtige_antwort = row[f"option{int(row['richtige_option'])}"]  # Richtige Antwort auslesen
        nutzer_antwort = antworten[i]                                  # Antwort des Nutzers
        quelle = row.get("quelle", "")                                 # Akademische Quelle (wenn vorhanden)

        if nutzer_antwort == richtige_antwort:
            st.success(f"✅ {i+1}. {row['frage']}")                   # Grüne Markierung für richtig
            punkte += 1                                              # Punkte erhöhen
        else:
            st.error(f"❌ {i+1}. {row['frage']}")                     # Rote Markierung für falsch
            st.markdown(f"**Richtige Antwort:** {richtige_antwort}")  # Richtige Antwort anzeigen

        # Falls eine Quelle angegeben ist, zeige sie als klickbaren Link an
        if quelle:
            st.markdown(f"[📚 Quelle]({quelle})", unsafe_allow_html=True)

    # Gesamtpunktzahl schön anzeigen
    st.metric("🏁 Punktestand", f"{punkte}/{len(df)}")

    # Wenn alle Antworten richtig sind, zeige Erfolg-GIF und Applaus-Sound nur einmal
    if punkte == len(df):
        show_gif("https://media.giphy.com/media/111ebonMs90YLu/giphy.gif")
        play_audio("https://www.soundjay.com/human/applause-8.mp3")
        st.balloons()  # Bunte Ballons als Belohnung
    else:
        # Wenn nicht alle richtig sind, zeige Fehler-GIF und Piepton nur einmal
        show_gif("https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif")
        play_audio("https://www.soundjay.com/button/beep-07.wav")


# 🧠 Lernnotizen 

# - `import streamlit as st`: Damit importieren wir das Streamlit-Tool für unsere Web-App.
# - `import pandas as pd`: Damit lesen wir CSV-Dateien ein und können Fragen/Antworten speichern.
# - `st.title()`: Zeigt eine große Überschrift auf der Webseite.
# - `st.expander()`: Ein aufklappbarer Infobereich mit Anleitungen oder Tipps.
# - `st.download_button()`: Hier können Nutzer eine Beispieldatei herunterladen.
# - `st.file_uploader()`: Damit können Nutzer ihre eigene Datei hochladen.
# - `pd.read_csv()`: Liest CSV-Dateien Zeile für Zeile in ein DataFrame ein.
# - `df.iterrows()`: Geht Zeile für Zeile die Fragen durch.
# - `st.radio()`: Zeigt mehrere Auswahloptionen für eine Frage.
# - `st.form()`: Gruppiert mehrere Fragen in ein gemeinsames Formular.
# - `st.form_submit_button()`: Knopf, mit dem das Formular abgeschickt wird.
# - `st.success()`, `st.error()`, `st.metric()`: Zeigen Feedback und Ergebnisse an.
# - `st.markdown(f"[Link](URL)")`: Erstellt klickbare Links – z. B. zu Quellen.
# - `st.balloons()`: Zeigt eine kleine Animation mit fliegenden Ballons.
# - `<audio autoplay>`: Spielt bei Erfolg oder Misserfolg Sounds direkt ab (nur mit Direktlink möglich).


