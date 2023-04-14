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


# Définir la date de début et de fin de l'année
start_date = '2022-01-01'
end_date = '2022-12-31'

# Créer une série temporelle quotidienne pour l'année
dates = pd.date_range(start_date, end_date, freq='D')

# Générer des données OHLC aléatoires avec une tendance haussière exponentielle suivie d'une tendance baissière linéairement
prices = np.zeros(len(dates))
prices[0] = np.random.randint(low=100, high=200)
for i in range(1, len(dates)):
    if i < len(dates) // 2:
        prices[i] = prices[i-1] * np.random.normal(loc=1.002, scale=0.01)
    else:
        prices[i] = prices[i-1] - 1.0
open_prices = prices + np.random.randint(low=10, high=20, size=len(dates))
high_prices = prices + np.random.randint(low=50, high=100, size=len(dates))
low_prices = prices - np.random.randint(low=50, high=100, size=len(dates))
close_prices = prices - np.random.randint(low=10, high=20, size=len(dates))

# Ajouter des perturbations aux prix OHLC
open_prices += np.random.normal(scale=15, size=len(open_prices))
high_prices += np.random.normal(scale=15, size=len(high_prices))
low_prices += np.random.normal(scale=15, size=len(low_prices))
close_prices += np.random.normal(scale=15, size=len(close_prices))

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
fig.add_trace(go.Scatter(x=df.index, y=df['SMA_50'], mode='lines', name='SMA 50'))
fig.add_trace(go.Scatter(x=df.index, y=df['SMA_100'], mode='lines', name='SMA 100'))


# Affichage du graphique dans Streamlit
st.plotly_chart(fig)
