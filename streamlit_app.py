import streamlit as st
import pandas as pd
import numpy as np
import plotly
import plotly.graph_objects as go

st.markdown(
    """
    <style>
    .block-container {
        width: 80%;
        text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("Analyse des crypto-monnaies")

st.write("Selectionnez une crypto-monnaie et visualisez le cours de sa valeur issue des données de Binance. L'analyse technique ensuite générée permet de calculer les indicateurs utilisés et d'afficher des alertes sur ces indicateurs."
)

st.selectbox(
        "Choisissez une crypto !",
        ("Bitcoin", "Ethereum", "BNB"))


# Création des données de test
data = {'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
        'Open': [100, 110, 120, 130, 140],
        'High': [120, 130, 140, 150, 160],
        'Low': [90, 100, 110, 120, 130],
        'Close': [110, 120, 130, 140, 150]}

df = pd.DataFrame(data)

# Création du graphique
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open'],
                                     high=df['High'],
                                     low=df['Low'],
                                     close=df['Close'])])

# Affichage du graphique dans Streamlit
st.plotly_chart(fig)
