import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Interaktives Diagramm steuert den App-Inhalt")

# --- Beispieldaten ----------------------------------------------------------
df = pd.DataFrame({
    "Stadt":        ["Berlin", "München", "Hamburg", "Köln", "Frankfurt", "Stuttgart"],
    "Einwohner":    [3_700_000, 1_500_000, 1_800_000, 1_100_000, 750_000, 635_000],
    "Bundesland":   ["Berlin",  "Bayern",   "Hamburg", "Nordrhein-Westfalen",
                     "Hessen",  "Baden-Württemberg"],
    "Fläche (km²)": [891, 310, 755, 405, 248, 208]
})

# --- Plotly-Diagramm --------------------------------------------------------
fig = px.bar(
    df,
    x="Stadt",
    y="Einwohner",
    hover_data=["Bundesland", "Fläche (km²)"],
    title="Einwohner der größten deutschen Städte"
)

selected_points = st.plotly_chart(fig, on_select="rerun")

# --- App-Logik, die auf die Auswahl reagiert --------------------------------
selected_points_indices = selected_points["selection"]["point_indices"]

if not selected_points_indices:
    st.write(
        "🔎 **Klicke** auf einen Balken im Diagramm, um "
        "Details anzuzeigen und den Rest der App dynamisch zu befüllen."
    )
else:
    selected_rows = df.iloc[selected_points_indices]
    st.dataframe(selected_rows, hide_index=True)