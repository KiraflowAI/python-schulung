import streamlit as st
import time #für die Pausefunktion time.sleep() im Fortschrittsbalken.

st.markdown("""
    <style>
        body {
            background-color: #ffe6f0;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Status-Demo") # Überschrift auf der Webseite – groß und fett oben.

st.success("Alles läuft wie geplant ✅") #Zeigt eine grüne Erfolgsmeldung an.
st.warning("Achtung: Noch nicht gespeichert ⚠️") #Zeigt eine gelbe Warnung an.
st.error("Fehler: Datei nicht gefunden ❌") #Zeigt eine rote Fehlermeldung an.
st.toast("Tipp: Du kannst auch Markdown verwenden ✨")#Zeigt eine kleine Nachricht unten rechts – wie ein Mini-Pop-up.

if st.button("Party feiern"):       #Wenn du auf den Button "Party feiern" klickst, passiert etwas…
    st.balloons()                   #	…es steigen bunte Ballons als Effekt auf.

if st.button("Fortschritt anzeigen"):    #Wenn du auf den Button "Fortschritt anzeigen" klickst…
    progress = st.progress(0)            #…startet ein Fortschrittsbalken bei 0 %.
    for i in range(100):
        time.sleep(0.01)                #…startet ein Fortschrittsbalken bei 0 %.
        progress.progress(i + 1)
    st.success("Fertig!")               #Am Ende zeigt Streamlit wieder eine grüne Erfolgsmeldung an.




    ###Dieser Mini-Code demonstriert fast alle einfachen Status-Elemente von Streamlit in Aktion – 
    # perfekt zum Üben. Du kannst sie in jeder App einsetzen, wenn du Feedback, Infos oder Animationen zeigen willst.
    # Wenn du möchtest, kann ich dir daraus auch ein lustiges oder nützliches Mini-Tool basteln, z. B. 
    # eine kleine Checkliste oder einen Fortschrittsmonitor für deine KI-Projekte.
