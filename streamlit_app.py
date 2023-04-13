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


# Définir les paramètres de la simulation
S = 100  # prix initial de l'action
r = 0.05  # taux d'intérêt sans risque
sigma = 0.2  # volatilité de l'action
T = 2  # durée de la simulation en années
N = 504  # nombre de pas de temps (jours) dans la simulation (252 jours par an)

# Générer les valeurs aléatoires pour la simulation
dt = T / N
t = np.linspace(0, T, N+1)
W = np.random.standard_normal(size=N+1)

# Calculer le prix de l'action simulé
S_t = S * np.exp((r - 0.5 * sigma**2) * t + sigma * np.sqrt(dt) * W.cumsum())

# Générer les données OHLCV simulées
dates = pd.date_range('2022-01-01', periods=N+1)
open_values = S_t[:-1]
close_values = S_t[1:]
high_values = np.maximum(open_values, close_values) + np.random.normal(0, 0.5, N)
low_values = np.minimum(open_values, close_values) - np.random.normal(0, 0.5, N)
volume_values = np.random.randint(1000, 5000, size=N+1)

# Créer un dataframe avec les données OHLCV simulées
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
