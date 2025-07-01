import streamlit as st
bmi_form = st.form(key="bmi_form")
 
with bmi_form:
    col1, col2 = st.columns(2)
 
    with col1:
        first_name = st.text_input("Vorname")
        age = st.number_input(
            "Dein Alter",
            min_value=0,
            max_value=120,
            value=18,
            step=1,
        )
 
    with col2:
        height_cm = st.number_input(
            "Körpergröße in cm",
            min_value=50.5,
            max_value=250.0,
            value=170.0,
            step=0.1,
            format="%.1f",
        )
 
        weight = st.number_input(
            "Dein Gewicht in kg",
            min_value=0.0,        
            max_value=600.0,      
            value=50.5,        
            step=0.1,          
            format="%.1f"
        )
 
    subbmitted = st.form_submit_button("Absenden")
 
if subbmitted:
    st.write(f"Hallo {first_name}")
    st.write(f"du bist {age} Jahre alt")
    st.metric(
        label="BMI",
        value=weight/(height_cm/100)**2
        )