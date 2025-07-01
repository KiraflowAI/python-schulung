import streamlit as st

st.title("Dashboard: Kennzahlen 2024")

st.header("Finanzen")
st.metric(label="Umsatz", value="2,5 Mio €", delta="+4 %")

st.header("Kunden")
st.metric(label="Kundenanzahl", value="8.420", delta="+120")

st.header("Mitarbeitende")
st.metric(label="Zufriedenheit", value="87 %", delta="-2 %")

st.markdown("**Stand:** April 2024")
