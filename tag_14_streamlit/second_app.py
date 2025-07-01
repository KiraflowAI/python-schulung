import streamlit as st

st.set_page_config(page_title="ZukunftsCheck", page_icon="🔍")

st.title("🔍 ZukunftsCheck – Welcher IT-Job passt zu dir?")
st.caption("Finde in 30 Sekunden heraus, welche Tech-Karriere zu dir passt – kostenlos & motivierend!")

# 💬 Eingaben
interesse = st.selectbox("Was interessiert dich am meisten?", ["Zahlen & Daten", "Menschen & Kommunikation", "Kreatives & Gestaltung", "Technik & IT"])
vorwissen = st.selectbox("Hast du schon Erfahrung im IT-Bereich?", ["Nein", "Ein bisschen", "Ja, einiges"])
ziel = st.selectbox("Was ist dir bei deinem neuen Job wichtig?", ["Gehalt", "Sicherheit", "Abwechslung", "Remote arbeiten"])

# 🚀 Button
if st.button("Zeig mir meine Zukunft!"):
    st.subheader("✨ Deine Empfehlung:")

    if interesse == "Zahlen & Daten":
        st.success("💼 **Data Analyst** – Du denkst strukturiert, hast Spaß an Auswertungen & Diagrammen. Perfekt für zukunftssichere Jobs im Büro!")
    elif interesse == "Technik & IT":
        st.success("🤖 **AI Engineer** – Künstliche Intelligenz ist die Zukunft. Mit Python & Machine Learning gestaltest du die digitale Welt mit.")
    elif interesse == "Menschen & Kommunikation":
        st.success("🧑‍🏫 **Digital Coach oder IT-Trainer** – Du lernst schnell und gibst Wissen gerne weiter? Ideal für die Schulungs- und Bildungswelt.")
    else:
        st.success("🎨 **UI/UX Design oder Content Creation** – Kreativität & Tech kombinieren? Hier bist du richtig – von Webdesign bis zu Social Media.")

    # 💡 Motivation + Call-to-Action
    st.markdown("---")
    st.info("🔑 **Wusstest du?** Diese Weiterbildungen sind oft **100 % förderbar** mit einem Bildungsgutschein vom Jobcenter.")
    st.markdown("👉 [Hier kannst du eine passende Schulung finden](https://data-plus.de) *(Beispiel-Link)*")
    st.caption("💬 Fragen? Dein KI-Coach hilft dir weiter – oder starte einfach mit deiner Weiterbildung.")

