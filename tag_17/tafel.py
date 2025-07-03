import streamlit as st

# Initialisiere den Zähler im Session State, falls noch nicht vorhanden
if "counter" not in st.session_state:
    st.session_state.counter = 0 #session state zwischenspeicher

# Button anzeigen
if st.button("Klick mich"):
    # Wenn der Button gedrückt wird, erhöhe den Zähler im Session State
    st.session_state.counter += 1

# Zeige den aktuellen Zählerwert an
st.metric("Button geklickt", value=st.session_state.counter)

print(st.session_state)


# st.session_state
# st.session_state ist eine Art Speicher oder Datencontainer, den Streamlit bereitstellt.

# Er merkt sich Werte über mehrere Benutzeraktionen hinweg, auch wenn das Skript immer wieder neu gestartet wird (was Streamlit bei jeder Interaktion macht).

# Du kannst dort Variablen speichern, z. B. einen Zähler oder Nutzerinformationen.

# Beispiel: st.session_state.counter ist eine Variable namens counter im Session State.

# Warum wichtig?
# Ohne session_state würde jede Aktion das Skript neu starten und alle Variablen wären wieder auf Anfang. Mit session_state bleiben Werte erhalten.

# if st.button("Klick mich")
# st.button() ist eine Funktion von Streamlit, die einen Button auf der Webseite anzeigt.

# Der Text auf dem Button ist hier "Klick mich".

# Die Funktion gibt True zurück, wenn der Button gerade gedrückt wurde (also beim Klick).

# Das if davor prüft also:

# Wenn der Button geklickt wurde, dann führe den Codeblock unter if aus.

# Ansonsten wird dieser Codeblock übersprungen.

# Kurz: Das ist eine Bedingung, die prüft, ob der Nutzer den Button gedrückt hat.