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


import random

# Générer des données aléatoires
dates = pd.date_range('2022-01-01', periods=100)
open_values = np.random.normal(100, 1, 100)
close_values = np.random.normal(100, 1, 100)
high_values = np.maximum(open_values, close_values) + np.random.normal(0, 0.5, 100)
low_values = np.minimum(open_values, close_values) - np.random.normal(0, 0.5, 100)
volume_values = np.random.randint(1000, 5000, size=100)

# Ajouter des moyennes mobiles pour créer une courbe plus douce
window_size = 10
rolling_window = np.ones(window_size) / float(window_size)
open_values = np.convolve(open_values, rolling_window, mode='valid')
close_values = np.convolve(close_values, rolling_window, mode='valid')
high_values = np.convolve(high_values, rolling_window, mode='valid')
low_values = np.convolve(low_values, rolling_window, mode='valid')
volume_values = np.convolve(volume_values, rolling_window, mode='valid')

# Créer le dataframe OHLCV
df = pd.DataFrame({'Date': dates[window_size-1:],
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
