import streamlit as st

st.title("Medien einfügen")
st.header("Bilder")
st.subheader("Eine elektromagnetische Welle:")

st.image(
    "https://upload.wikimedia.org/wikipedia/commons/9/99/EM-Wave.gif",
    caption="Elektromagnetische Welle",
    use_container_width=True # Bei "True" wiird die volel Containerbreite verwendet
)

st.subheader("Das sichtbare Spektrum:")
# bilder hiinzufügen
st.image(
    "http://www.thermoglass.de/_sites/thermoglass/upload/images/615fc0ca95c1ddfecd813f81774e6f34_11-zareni-graf-wiki-de.png",
    caption="Sichtbare Spektrum der elektromagnetischen Welle",
    use_container_width=True
)

#Betten Videos ein (lokal oder via URL, z. B. MP4 oder YouTube-Links):
st.subheader("Animation der elektromagnetischen Welle:")
st.video("https://www.youtube.com/watch?v=aCTRjVEmeC0")

#Medien hochladen
#Ermöglicht Nutzern, eigene Dateien hochzuladen, man kann einen Filter auf Bilder, Audio oder Video setzen:
st.subheader("Video hochladen:")
uploaded = st.file_uploader("Lade eine Videodatei hoch", type=["mp4", "mov"])
if uploaded:
    st.video(uploaded)


#4. Medien downloaden
#Dieses Widget bietet die Möglichkeit, mediale Inhalte (z. B. bearbeitete Bilder oder erzeugte Audios) zum Download bereitzustellen:

st.subheader("Bild downloaden:")
st.download_button(
    label="Bild herunterladen",
    data=open("assets/test_bild.png", "rb").read(),
    file_name="mein_bild.png",
    mime="image/png"
)