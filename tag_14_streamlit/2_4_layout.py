# Grundlegende Layouts in Streamlit
# Streamlit bietet verschiedene Mechanismen, um die App übersichtlich zu strukturieren und Inhalte gezielt anzuordnen.


# In vielen Dashboards möchte man verschiedenen Ansichten nebeneinander anbieten, da kommt st.tabs zum Einsatz:

import streamlit as st

tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.write("You are in Tab 1")
    
with tab2:
    st.write("You are in Tab 2")
    
with tab3:
    st.write("You are in Tab 3")

#Eine Seitenleiste eignet sich ideal für Navigation, Filter oder Einstellungen. Sie kann einfach über st.sidebar erzeugt werden:

st.sidebar.title("This is the Sidebar")
st.sidebar.write("You can playce elements like buttons and text here.")
sidebar_input = st.sidebar.text_input("Enter something in the sidebar:")

tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.write("You are in Tab 1")
    
with tab2:
    st.write("You are in Tab 2")
    
with tab3:
    st.write("You are in Tab 3")

#Mit st.columns(n) teilt man den verfügbaren Raum in n gleich breite Spalten auf. Man kann auch Gewichtungen angeben:

col1, col2 = st.columns(2)
with col1:
    st.header("Column 1")
    st.write("Content for column 1")
with col2:
    st.header("Column 2")
    st.write("Content for column 2")

#Ein st.container() ist ein flexibler Platzhalter, in dem man dynamisch Inhalte einfügen kann:

with st.container(border=True):
    st.write("This is inside a container.")
    st.write("You can think of containers as a grouping for elements.")
    st.write("Containers help manage sections of the page.")
    
#Mit st.empty() erzeugt man ein leeres Element im Layout, das man später befüllen, ersetzen oder löschen kann. Das ist praktisch, wenn man Inhalte dynamisch aktualisieren will, ohne die Position zu verändern:

placeholder = st.empty()
placeholder.write("This is an empty placeholder, useful for dynamic content.")

if st.button("Update Placeholder"):
    placeholder.write("The content of this placeholder has been updated")

# Ein Expander ist ein Bereich, der standardmäßig eingeklappt ist und bei Bedarf vom Nutzer aufgeklappt werden kann. Ideal, um zusätzliche Details oder Fortgeschrittenen-Optionen zu verbergen:

with st.expander("Expand for more details"):
    st.write("This is additional information that is hidden by default.")
    st.write("You can use expanders to keep your interface cleaner.")

# Ein einfacher Weg, kurze Hilfetexte oder Erklärungen als Popover anzuzeigen, ist die Nutzung des help-Arguments bei Widgets. Bei Hover über das Info-Icon erscheint automatisch ein Tooltip bzw. Popover mit deinem Text:

st.write("Hover over this button for a tooltip")
st.button("Button with Tooltip", help="This is a tooötip or popover on hover!")

#Zum Abschluss fügen wir noch die Eingabe aus der Seitenleiste in unser Layout hinzu:

if sidebar_input:
    st.write(f"You entered in the sidebar: {sidebar_input}")
