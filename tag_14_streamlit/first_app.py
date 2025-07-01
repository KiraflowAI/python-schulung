import streamlit as st
import pandas as pd

st.markdown("""
## 🌍 Du willst – wie ich – mehr als nur einen Job.

### Du willst etwas, das bleibt.  
Etwas, das Sinn ergibt.  
Etwas, das Zukunft hat.

Vielleicht spürst du – wie ich – dass die Welt sich verändert.  
Dass KI kommt. Und nicht wieder geht.  
Und du fragst dich: *Was mach ich jetzt damit?*

---

## 🤖 KI ist schon da. Die Frage ist: Was tun wir damit?

Du könntest sagen:  
„Das ist mir zu viel. Zu technisch. Zu schnell.“

Oder du könntest sagen:  
„Ich will das verstehen. Ich will mitgestalten.“

Denn KI verändert längst unser Leben:  
Wie wir arbeiten. Wie wir lernen. Wie wir entscheiden.

Die Frage ist nicht mehr *ob*.  
Sondern: **Wie. Und von wem.**

---

## 💡 Du kannst Teil der Veränderung sein – und sie bewusst gestalten.

- 🧕 **Menschen helfen**, die keinen Zugang zu Bildung haben  
- 🏥 **Patienten unterstützen**, durch smarte Gesundheitsdaten  
- 🌱 **Nachhaltigkeit fördern**, mit effizienter Ressourcennutzung  
- 👩‍🦽 **Barrieren abbauen**, mit KI-gesteuerter Assistenz  
- 🏛 **Verwaltung entlasten**, damit Hilfe schneller ankommt  
- 🗣️ **Diskussionen versachlichen**, weil du Daten liest – nicht nur Schlagzeilen

> **Du lernst KI nicht, um ersetzt zu werden –  
du lernst, um gebraucht zu werden.**

---

## ⚖️ Und ja: KI ist auch kritisch zu sehen.

- Sie verbraucht Energie. Viel.  
- Sie ist nicht neutral – sondern so fair wie wir.  
- Sie kann manipulieren – oder aufklären.  
- Sie kann entmenschlichen – oder verbinden.

> **KI ist kein Feind. Kein Wundermittel. Kein Selbstläufer.**  
> Sie ist ein Werkzeug.  
> Und du entscheidest, *wofür du es nutzt.*

---

## 🧠 KI kann Bewusstsein fördern – wenn du sie bewusst nutzt.

Sie zeigt dir, wie du denkst.  
Was du glaubst. Und was du wirklich willst.  

Wenn du mit Daten arbeitest, wirst du sensibel für Muster.  
Für Zusammenhänge. Für Wirkung.

> Plötzlich geht’s nicht mehr nur um Tools –  
> sondern darum, **was du damit bewirken willst**.

---

## 🧭 Arbeiten, wo du willst. Und wofür du willst.

Du lernst KI nicht, um in irgendeinem Büro zu sitzen.  
Sondern um frei zu sein –  
geistig, räumlich, menschlich.

Du könntest von überall aus arbeiten.  
Aber du könntest auch **dort etwas aufbauen, wo es gebraucht wird**:

- 🍃 Digitale Lösungen für nachhaltige Projekte  
- 🐝 Automatisierung für Bio-Betriebe oder grüne Plattformen  
- 🌱 Wirkung aus einem Eco-Village heraus – lokal verbunden, digital wirksam

Denn wer KI versteht,  
kann **neue Modelle des Arbeitens und Lebens gestalten** –  
im Einklang mit Mensch, Natur und Technologie.

> **Du willst nicht nur arbeiten.  
Du willst beitragen. Bewusst. Frei. Und echt.**

---

## 📈 Warum KI-Berufe? Weil die Welt dich braucht.

""")

data = {
    "Beruf": ["Data Analyst", "Data Scientist", "AI Engineer", "KI-Trainer", "BI-Spezialist"],
    "🇩🇪 Bedarf (2025)": ["85.000+", "40.000+", "25.000+", "10.000+", "60.000+"],
    "🌍 Globaler Bedarf (2030)": ["1,5 Mio.+", "2 Mio.+", "1 Mio.+", "wachsend", "1 Mio.+"],
    "Typische Aufgaben": [
        "Daten analysieren & Dashboards bauen",
        "ML-Modelle entwickeln & testen",
        "KI-Anwendungen programmieren",
        "Modelle trainieren & Prompts schreiben",
        "BI-Reports & Visualisierungen erstellen"
    ]
}

df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)
st.caption("Quellen: Bitkom, McKinsey, OECD, WEF (2023–2025)")

st.markdown("""
---

## 🚀 Warum ich DataPlus gewählt habe?

Weil ich nicht nur Tools lernen will –  
sondern Verantwortung übernehmen.

Weil ich Technik, Menschlichkeit und Zukunft nicht trennen will.  
Sondern zusammenbringen.

Weil ich glaube:
> **Wer KI versteht, kann Gerechtigkeit, Nachhaltigkeit  
und Chancen mitgestalten – nicht nur konsumieren.**

Deshalb lerne ich nicht nur für mich.  
**Ich lerne für uns.**
""")
