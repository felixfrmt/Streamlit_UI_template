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


# Générer des données OHLCV aléatoires
dates = pd.date_range('2022-01-01', periods=1000)
open_values = np.random.normal(100, 1, 1000)
close_values = np.random.normal(100, 1, 1000)
high_values = np.maximum(open_values, close_values) + np.random.normal(0, 0.5, 1000)
low_values = np.minimum(open_values, close_values) - np.random.normal(0, 0.5, 1000)
volume_values = np.random.randint(1000, 5000, size=1000)


# Créer un dataframe avec les données OHLCV
df = pd.DataFrame({'Date': dates,
                   'Open': open_values,
                   'High': high_values,
                   'Low': low_values,
                   'Close': close_values,
                   'Volume': volume_values})

# Calculer les moyennes mobiles
df['SMA_50'] = df['Close'].rolling(window=50).mean()
df['SMA_100'] = df['Close'].rolling(window=100).mean()

# Créer le graphique Plotly
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open'],
                                     high=df['High'],
                                     low=df['Low'],
                                     close=df['Close'])])

# Ajouter les traces pour les moyennes mobiles 50 et 100
fig.add_trace(go.Scatter(x=df['Date'], y=df['SMA_50'], mode='lines', name='SMA 50'))
fig.add_trace(go.Scatter(x=df['Date'], y=df['SMA_100'], mode='lines', name='SMA 100'))


# Affichage du graphique dans Streamlit
st.plotly_chart(fig)
