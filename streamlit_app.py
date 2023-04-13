import streamlit as st
import pandas as pd
import numpy as np
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


# Création des données aléatoires
dates = pd.date_range('2022-01-01', periods=100)
open_values = np.random.randint(10, 50, size=100)
high_values = np.random.randint(50, 100, size=100)
low_values = np.random.randint(0, 10, size=100)
close_values = np.random.randint(10, 50, size=100)
volume_values = np.random.randint(1000, 5000, size=100)

# Création du dataframe OHLCV
df = pd.DataFrame({'Date': dates,
                   'Open': open_values,
                   'High': high_values,
                   'Low': low_values,
                   'Close': close_values,
                   'Volume': volume_values})

# Création du graphique
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open'],
                                     high=df['High'],
                                     low=df['Low'],
                                     close=df['Close'])])

# Affichage du graphique dans Streamlit
st.plotly_chart(fig)
