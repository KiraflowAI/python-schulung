#Wir haben kennengelernt, dass man bei Layout-Elemente in Streamlit mit dem with Keyword verwenden kann. Man kann diese Layoutelemente jedoch auch in einer Variablen speichern und ohne das with neue Elemente diesem hinzufügen. Schaue dazu das folgende Beispiel an:

# import streamlit as st

# tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

# # Variante mit "with"
# with tab1:
#     st.write("You are in Tab 1")

# # Variante ohne "with"    
# tab2.write("You are in Tab 2")

# Für welche anderen Layoutelemente ist dies auch möglich? Erstelle eine Liste mit Beispielen.

# Wann ist welche Variante besser geeignet?

                    # Diese Schreibweise ist auch möglich für z.B.:

                    # expander
                    # sidebar
                    # columns
                    # container


import streamlit as st

exp = st.expander("Details")
exp.write("Einige zusätzliche Informationen")

sidebar = st.sidebar
sidebar.write("Inhalt in der Sidebar")

col1, col2 = st.columns(2)
col1.write("In Spalte 1")
col2.write("In Spalte 2")

container = st.container()
container.write("In einem Container")



            # with-Variante:

            # Klarere visuelle Struktur im Code, besonders bei verschachtelten Elementen

            # Ideal für kurze Abschnitte

            # Objektbasierte Variante:

            # Flexibel bei dynamischen Zugriffen (z. B. innerhalb von Schleifen oder Funktionen)

            # Nützlich bei mehrfacher Wiederverwendung oder späterem Füllen (z. B. st.empty())

            # Fazit: Beide Varianten sind gleichwertig verwendbar. Die Entscheidung hängt von der Lesbarkeit und vom Anwendungsfall ab.