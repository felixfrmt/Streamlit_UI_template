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


start_date = '2022-01-01'
end_date = '2022-12-31'

# Créer une série temporelle quotidienne pour l'année
dates = pd.date_range(start_date, end_date, freq='D')

# Générer des données OHLC aléatoires pour chaque jour
open_prices = np.random.randint(low=100, high=200, size=len(dates))
high_prices = np.random.randint(low=open_prices, high=300, size=len(dates))
low_prices = np.random.randint(low=50, high=open_prices, size=len(dates))
close_prices = np.random.randint(low=50, high=200, size=len(dates))

# Créer un DataFrame contenant les données OHLC
df = pd.DataFrame({'Open': open_prices, 'High': high_prices, 'Low': low_prices, 'Close': close_prices}, index=dates)

# Calculer les moyennes mobiles
df['SMA_50'] = df['Close'].rolling(window=50).mean()
df['SMA_100'] = df['Close'].rolling(window=100).mean()

# Créer le graphique Plotly
fig = go.Figure(data=[go.Candlestick(x=df.index,
                                     open=df['Open'],
                                     high=df['High'],
                                     low=df['Low'],
                                     close=df['Close'])])

# Ajouter les traces pour les moyennes mobiles 50 et 100
fig.add_trace(go.Scatter(x=df['Date'], y=df['SMA_50'], mode='lines', name='SMA 50'))
fig.add_trace(go.Scatter(x=df['Date'], y=df['SMA_100'], mode='lines', name='SMA 100'))


# Affichage du graphique dans Streamlit
st.plotly_chart(fig)
