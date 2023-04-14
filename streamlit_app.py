import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

import streamlit.components.v1 as components

# bootstrap 4 collapse example
components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    """,
    height=600,
)


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

crypto = st.selectbox(
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
    if i < 3 * len(dates) // 4:
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
fig.update_layout(xaxis_rangeslider_visible=False)

# Ajouter les traces pour les moyennes mobiles 50 et 100
fig.add_trace(go.Scatter(x=df.index, y=df['SMA_50'], mode='lines', name='SMA 50'))
fig.add_trace(go.Scatter(x=df.index, y=df['SMA_100'], mode='lines', name='SMA 100'))

df2 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig2 = go.Figure(data=[go.Candlestick(x=df2['Date'],
                open=df2['AAPL.Open'], high=df2['AAPL.High'],
                low=df2['AAPL.Low'], close=df2['AAPL.Close'])
                     ])
fig2.update_layout(xaxis_rangeslider_visible=False)


# Affichage du graphique dans Streamlit
if crypto == "Bitcoin":
    st.plotly_chart(fig2)

    
elif crypto == "Ethereum":
    st.plotly_chart(fig)



col1, col2, col3 = st.columns(3)
col1.write("""
    <div class="card" style="width: 18rem;">
        <img src="https://via.placeholder.com/150" class="card-img-top" alt="...">
        <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
            <a href="#" class="btn btn-primary">Go somewhere</a>
        </div>
    </div>
""", unsafe_allow_html=True)


