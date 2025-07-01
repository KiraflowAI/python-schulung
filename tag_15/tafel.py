import streamlit as st
# #print("Code wird erneut ausgeführt")
# st.title("Tag 2 wird interaktiv")

# is_adult = st.checkbox(label="Volljährig")

# #print(is_adult)

# if is_adult: 
#     st.write("Benutzer ist Volljährig")
# #else:
# #    st.write("Benutzer ist nicht Volljährig")

                    # 

# if klickbox:
#     st.write("Button wurde geklickt")
# else:
#     st.write("Button nicht geklickt")

# farbe = st.radio("Wähle eine Farbe:", ["Rot", "Blau", "Lila", "FFFFFF"])
# st.write(f"Die ausgewählte Farbe ist: {farbe}")

# city = st.selectbox("Stadt auswählen:", ["Berlin", "München", "Hamburg"])
# st.write("Deine Stadt:", city)

# foods = st.multiselect("Lieblingsessen:", ["Pizza","Sushi","Salat"])
# st.write("Du magst:", foods)

st.button("Klick mich", key="1button")
st.button("Klick mich", key="2button")
st.button("Klick mich", key="3button")

if st.session_state["1button"]:
    st.write("Button wurde geklickt")


st.radio("Wähle aus:", ["links", "mitte", "rechts", "oben", "unten"], key="richtuung")

# wird alles gespeichert was gemacht und getan wurde
st.write(st.session_state)





                # import streamlit as st
                
                # st.button("Klick mich", key="button1")
                # st.button("Klick mich", key="button2")
                # st.button("Klick mich", key="button3")
                
                # if st.session_state.button1:
                #     st.write("Button wurde geklickt")
                
                # #st.write(f"# Über Variable: {var_richtung}")
                # st.write(f"# Über Sessionstate: {st.session_state.richtung}")
                
                # st.radio(
                #     label="Wähle aus: ",
                #     options=["links", "mitte", "rechts", "oben", "unten"],
                #     key="richtung"
                #     )
                
                
                # st.write(st.session_state)