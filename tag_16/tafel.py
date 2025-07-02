import streamlit as st
import pandas as pd
import plotly.express as px
 
df = pd.DataFrame({
    "Stadt": ["Berlin", "München", "Hamburg", "Köln", "Frankfurt"],
    "Einwohner": [3_700_000, 1_500_000, 1_800_000, 1_100_000, 750_000]
})
 
fig = px.bar(df, x="Stadt", y="Einwohner")
 
st.plotly_chart(fig)

selected = st.plotly_chart(fig, on_select="rerun")

user_selection = selected["selection"]["point_indices"]

#st.header(selected["selection"]["points"][0])

st.write(user_selection)
st.dataframe(df.loc[user_selection])

st.write(selected)