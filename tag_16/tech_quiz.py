# ------------------------------------------------------------
# 🎯 Streamlit-Quiz 
# ------------------------------------------------------------

# 📌 Wir brauchen zuerst Streamlit, um die Web-App zu bauen
import streamlit as st  # Mit diesem Befehl laden wir das Streamlit-Paket

# 🧠 Überschrift auf der Seite anzeigen
st.title("🎯 Mini-Quiz: Wie gut kennst du dich aus?")

# 🔢 Variable für Punkte – startet bei 0
score = 0  # Damit zählen wir die richtigen Antworten

# 📋 Liste für Feedback – hier merken wir uns alle Fehler
feedback = []  # Damit sagen wir später: „Welche Antwort war falsch?“

# 📦 Formular starten – das ist ein Block, in dem mehrere Fragen gesammelt werden
with st.form("quiz_form"):

    # ❓ Frage 1 – Programmiersprache
    st.markdown("### 1. Welche Sprache liebt Pandas & Zahlen?")
    q1 = st.radio("Wähle:", ["Java", "Python", "HTML"])  # Radio bedeutet: nur eine Antwort ist möglich

    # ❓ Frage 2 – Rechnen
    st.markdown("### 2. Was ergibt 3 * 3 + 1?")
    q2 = st.number_input("Antwort:", min_value=0, max_value=100, step=1)  # Eingabefeld für Zahlen

    # ❓ Frage 3 – Webdesign
    st.markdown("### 3. Was gehört zur Webentwicklung?")
    q3 = st.selectbox("Wähle:", ["NumPy", "CSS", "Pandas", "Scikit-learn"])  # Aufklappmenü

    # ❓ Frage 4 – Kilobyte-Wissen
    st.markdown("### 4. Wie viele Bytes hat 1 Kilobyte?")
    q4 = st.radio("Wähle:", ["1000", "1024", "512"])

    # ❓ Frage 5 – Was kann KI?
    st.markdown("### 5. Was macht eine KI?")
    q5 = st.selectbox("Wähle:", [
        "Sie denkt wie ein Mensch.",
        "Sie kann aus Daten lernen.",
        "Sie ist ein Roboter mit Armen."
    ])

    # 🧩 Bonusfrage freischalten – aber nur, wenn CSS bei Frage 3 gewählt wurde
    bonus = ""
    if q3 == "CSS":
        with st.expander("🎁 Bonusfrage freigeschaltet!"):
            bonus = st.radio("Was bedeutet CSS?", [
                "Creative Style Sheets",
                "Cascading Style Sheets",
                "Computer Styling System"
            ])

    # ✅ Button zum Abschicken der Antworten
    submitted = st.form_submit_button("🚀 Auswerten")

# 🧾 Jetzt prüfen wir, ob jemand den Button gedrückt hat
if submitted:

    # ✅ Frage 1 prüfen
    if q1 == "Python":
        score += 1
    else:
        feedback.append("❌ Frage 1: Richtige Antwort wäre **Python** gewesen.")

    # ✅ Frage 2 prüfen
    if q2 == 10:
        score += 1
    else:
        feedback.append("❌ Frage 2: 3 * 3 + 1 = **10**.")

    # ✅ Frage 3 prüfen
    if q3 == "CSS":
        score += 1
    else:
        feedback.append("❌ Frage 3: Für Webdesign brauchst du **CSS**.")

    # ✅ Frage 4 prüfen
    if q4 == "1024":
        score += 1
    else:
        feedback.append("❌ Frage 4: 1 Kilobyte = **1024 Bytes**.")

    # ✅ Frage 5 prüfen
    if q5 == "Sie kann aus Daten lernen.":
        score += 1
    else:
        feedback.append("❌ Frage 5: KI lernt aus Daten, nicht denken!")

    # ✅ Bonusfrage prüfen (nur wenn CSS gewählt)
    if q3 == "CSS":
        if bonus == "Cascading Style Sheets":
            score += 1
            st.success("✅ Bonusfrage korrekt!")
        elif bonus != "":
            feedback.append("❌ Bonusfrage: CSS = **Cascading Style Sheets**.")

    # 📊 Punktestand anzeigen
    st.subheader(f"🏁 Dein Punktestand: {score}/6")

    # 🎉 Alles richtig?
    if score == 6:
        st.balloons()  # Luftballons fliegen!

        st.success("🎉 Super! Du hast ALLES richtig gemacht!")

        # 🎵 Sound bei richtig
        st.markdown("""
        <audio autoplay>
          <source src="https://www.soundjay.com/human/applause-8.mp3" type="audio/mpeg">
        </audio>
        """, unsafe_allow_html=True)

        # 🎬 Giphy bei richtig
        st.image("https://media.giphy.com/media/111ebonMs90YLu/giphy.gif", width=300)

    else:
        # 🧱 Fehler anzeigen
        st.error("Oh nein! Hier sind deine Fehler:")

        for msg in feedback:
            st.write(f"• {msg}")  # Liste aller Fehler

        # 🎵 Sound bei Fehler
        st.markdown("""
        <audio autoplay>
          <source src="https://www.soundjay.com/button/beep-07.wav" type="audio/mpeg">
        </audio>
        """, unsafe_allow_html=True)

        # 🎬 Giphy bei Fehler
        st.image("https://media.giphy.com/media/26ufdipQqU2lhNA4g/giphy.gif", width=300)



# 🔎 WAS MACHT DER CODE?

# 1. Wir starten mit `import streamlit as st` – das heißt: Wir holen uns das Werkzeug "Streamlit" und nennen es einfach "st".

# 2. `st.title("...")` zeigt einen großen Titel oben auf der Seite an. Emojis helfen, dass es spannender aussieht.

# 3. `score = 0` – Wir starten bei 0 Punkten. Jedes Mal, wenn du eine Frage richtig beantwortest, gibt es +1 Punkt.

# 4. `feedback = []` – Eine Liste, in der falsche Antworten gespeichert werden. Das hilft später beim Erklären.

# 5. `with st.form("quiz_form"):` – Ein "Formular" bedeutet: Alle Fragen sind wie auf einem Zettel und werden erst "abgegeben", wenn du auf den Button klickst.

# 6. `st.radio(...)` – Das zeigt mehrere Punkte (Radio-Buttons), von denen du einen auswählen kannst. Nur eine Antwort ist erlaubt.

# 7. `st.number_input(...)` – Hier gibst du eine Zahl ein oder klickst auf Plus/Minus.

# 8. `st.selectbox(...)` – Ein kleines Feld zum Aufklappen. Du wählst genau eine Sache aus der Liste.

# 9. `if q3 == "CSS":` – Wenn bei Frage 3 "CSS" gewählt wurde, dann...

# 10. `st.expander(...)` – Das ist wie ein kleines Klappfeld. Bonusfragen oder Zusatzinfos kann man damit verstecken.

# 11. `st.text_input(...)` – Damit kann man einen Text eintippen.

# 12. `st.form_submit_button(...)` – Der Button ganz unten. Erst wenn der gedrückt wird, geht es weiter zur Auswertung.

# 13. `if q1 == "Python": score += 1` – Wenn die Antwort stimmt, gibt es einen Punkt. Sonst kommt ein Hinweis in die Feedbackliste.

# 14. `bonus.strip().lower()` – Das macht den Text klein (also „css“ statt „CSS“) und entfernt unnötige Leerzeichen. So wird es einfacher zu vergleichen.

# 15. `st.balloons()` – Zeigt bunte Ballons, wenn du alles richtig gemacht hast.

# 16. `st.markdown("<audio autoplay>...")` – Damit spielt die Seite einen Ton ab. Es gibt Applaus bei Erfolg oder ein Piepsen bei Fehlern.

# 17. `st.image("...giphy.gif")` – Das lädt ein lustiges animiertes Bild (GIF) von einer Webseite.

# 18. `for msg in feedback:` – Für jede falsche Antwort wird die passende Erklärung gezeigt.
# """


# # 📘 LERNZUSAMMENFASSUNG:

# # - st.title(...) → Zeigt einen Seitentitel
# # - score = 0 → Zählt, wie viele Fragen richtig sind
# # - feedback = [] → Liste, in die falsche Antworten als Text kommen

# # - st.form(...) → Gruppe von Eingaben, die zusammen abgeschickt werden
# # - st.radio(...) → Eine von mehreren Optionen auswählen (Punkte)
# # - st.selectbox(...) → Dropdown-Menü für eine Auswahl

# # - st.form_submit_button(...) → Aktiviert die Auswertung bei Klick
# # - if submitted: → Alles darunter wird nur ausgeführt, wenn der Button geklickt wurde

# # - st.progress(...) → Visualisiert den Punktestand als Fortschritt (0.0 bis 1.0)
# # - st.metric(...) → Zeigt „Dein Ergebnis: X von 6“
# # - st.balloons() → Schöne Animation bei 100 % richtig
# # - st.markdown(<audio>) → Spielt Sounds ab (Beep oder Applaus)

# # - Bonusfrage wird NUR angezeigt, wenn alle Fragen richtig waren (score == 6)

# # WICHTIG:
# # Das Ganze funktioniert nur, wenn du Streamlit installiert hast:
# # → pip install streamlit
# # → Dann starten mit: streamlit run quiz.py
# # """
