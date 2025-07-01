import streamlit as st
import pandas as pd

# 1. Große Überschrift
st.title("Datenanalyse mit Streamlit")



# 2. Überschrift der zweiten Ebene
st.header("Allgemeine Grundlagen")

# 3. Überschrift der dritten Ebene
st.subheader("Der Arithmetische Mittelwert")

# 4. Einfacher Text
st.text("Datenanalyse ist ein sehr umfangreiches Thema.")

# 5. Markdown-Inhalte
mean_value_description = '''
**Was ist der arithmetische Mittelwert?**
Es handelt sich um eine wichtige statistische Kennzahl, die uns hilft,  
die zentrale Tendenz einer Gruppe von Zahlen bzw. Daten zu verstehen.

---

Das arithmetische Mittel allein gibt nur eine begrenzte Information über die Verteilung der Daten.  
Wenn verschiedene Verteilungen das gleiche arithmetische Mittel haben, bedeutet das nicht zwangsläufig,  
dass die Verteilungen ähnlich oder gleich sind.  
Sie können unterschiedliche Streuungen, Schiefe oder Formen aufweisen.

Eine allgemeine mathematische Definition sieht so aus:
'''
st.markdown(mean_value_description)

# 6. LaTeX-Ausgabe
# Manchmal möchte man eine mathematische Formel auf der UI darstellen. Dazu kann man sich der LaTeX Syntax bedienen. Wir können unterschiedliche LaTeX-Ausdrücke darstellen:
st.latex(r"""\overline{x} = \frac{1}{n}\sum_{i=1}^n x_i""")

# 7. Universelles Ausgabe-Utility mit DataFrame
#Universelles Ausgabe Utility
#Diese Funktionalität ermöglicht uns die formatierte Ausgabe unterschiedlicher Inhalte. 
# Bei der Ausgabe von DataFrames werden schöne Tabellen erstellt, es können Grafiken angezeigt werden, 
# bei Strings wird Markdown unterstützt und noch viel mehr. Diese Funktion erkennt automatisch den Datentyp und rendert entsprechend:
st.write("Die **Markdown** Syntax ist hier möglich! Aber auch [Links](https://www.markdownguide.org/basic-syntax/) werden dargestellt.")
st.text("So kann ein DataFrame in Streamlit aussehen:")
df = pd.DataFrame({"A": [10, 20, 30], "B": [40, 50, 60]})
st.write(df)

# 8. Code-Snippet
# Die Darstellung von Code wird ebenfalls unterstützt. Dabei wird für die jeweilige P
# rogrammiersprache auch Code-Highlighting unterstützt. Dadurch lassen sich auch Code-Dokumentationen sehr gut umsetzen:
st.write("So kann man den arithmetischen Mittelwert in Python berechnen:")
code_mean_value = '''numbers = [2, 4, 3]
mean_value = sum(numbers) / len(numbers)'''
st.code(code_mean_value, language="python")

# 9. Kennzahlen (Metriken)
# In Streamlit gibt es eine Funktion, welche besonders für die Darstellung von Kenzahlen bzw. Metriken geeignet ist. Damit können wir KPIs (Key Performance Indicators) effektiv darstellen. Es ist sehr nützlich bei Dashboards wo Echtzeit-Anzeigen gefordert sind wie z.B. aktuelle Temperatur, Börsenkurse...
#label: Beschriftung der Kennzahl
# value: Aktueller Wert
# delta: Veränderung gegenüber einer Referenz (Differenz).
# delta_color: Farbe für das Delta:
# normal: Standard (grün bei positiv, rot bei negativ)
# inverse: Invertiert (rot bei positiv, grün bei negativ)
# off: Keine Farbgebung

mean_A = df["A"].mean()
mean_B = df["B"].mean()

st.metric(
    label="Mittelwert von Spalte A",
    value=f"{mean_A:.2f}",
    delta=f"{mean_A - mean_B:+.2f}"
)

st.metric(
    label="Mittelwert von Spalte B",
    value=f"{mean_B:.2f}",
    delta=f"{mean_B - mean_A:+.2f}"
)

# oder so 
                                # df = pd.DataFrame({
                                #     "A": [10, 20, 30],
                                #     "B": [40, 50, 60]
                                # })
                                # mean_A = df["A"].mean()
                                # mean_B = df["B"].mean()
                                # st.metric(
                                #     label="Mittelwert von Spalte A",
                                #     value=f"{mean_A:.2f}",
                                #     delta=f"{mean_A - df['B'].mean():+.2f}"
                                # )
                                # st.metric(
                                #     label="Mittelwert von Spalte B",
                                #     value=f"{mean_B:.2f}",
                                #     delta=f"{mean_B - df['A'].mean():+.2f}"
                                # )



