import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.graph_objects as go

import streamlit.components.v1 as components

# bootstrap 4 collapse example
components.html(
#       '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">',
      """<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw7046Kd6TMOGn8HcYcNqVQ6UksdQRVvyVpTE1PiVo/" crossorigin="anonymous">""",
      height=0,
)

st.markdown(
    """
    <style>
    .block-container {
        width: 80%;
        text-align: center;
        }
      img {
            width:60%;
            align-self: center;
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

################################## Generate ETHEREUM's Data #####################################
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
high_prices += np.random.normal(scale=2, size=len(high_prices))
low_prices += np.random.normal(scale=2, size=len(low_prices))
close_prices += np.random.normal(scale=10, size=len(close_prices))

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

fig.update_layout(
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    )
)


################################## Generate BITCOIN's Data  #####################################
df2 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

df2['SMA_50'] = df2['AAPL.Close'].rolling(window=50).mean()
df2['SMA_100'] = df2['AAPL.Close'].rolling(window=100).mean()

df2['TP'] = (df2['AAPL.Close'] + df2['AAPL.Low'] + df2['AAPL.High'])/3
df2['std'] = df2['TP'].rolling(20).std(ddof=0)
df2['MA-TP'] = df2['TP'].rolling(20).mean()
df2['BOLU'] = df2['MA-TP'] + 2*df2['std']
df2['BOLD'] = df2['MA-TP'] - 2*df2['std']

fig2 = go.Figure(data=[go.Candlestick(x=df2['Date'],
                open=df2['AAPL.Open'], high=df2['AAPL.High'],
                low=df2['AAPL.Low'], close=df2['AAPL.Close'])
                     ])
fig2.update_layout(xaxis_rangeslider_visible=False)
fig2.add_trace(go.Scatter(x=df2['Date'], y=df2['SMA_50'], mode='lines', name='SMA 50'))
fig2.add_trace(go.Scatter(x=df2['Date'], y=df2['SMA_100'], mode='lines', name='SMA 100'))
fig2.add_trace(go.Scatter(x=df2['Date'], y=df2['BOLU'], mode='lines', name='Bande de Bollinger (up)'))
fig2.add_trace(go.Scatter(x=df2['Date'], y=df2['BOLD'], mode='lines', name='Bande de Bollinger (down)'))

fig2.update_layout(
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    )
)


df3 = pd.read_csv('https://raw.githubusercontent.com/matplotlib/mplfinance/2710cf4bb3d0c19fe9bda19c0b999588b658ed26/examples/data/yahoofinance-GOOG-20040819-20180120.csv')


df3['SMA_50'] = df3['Close'].rolling(window=50).mean()
df3['SMA_100'] = df3['Close'].rolling(window=100).mean()

df3['TP'] = (df3['Close'] + df3['Low'] + df3['High'])/3
df3['std'] = df3['TP'].rolling(20).std(ddof=0)
df3['MA-TP'] = df3['TP'].rolling(20).mean()
df3['BOLU'] = df3['MA-TP'] + 2*df3['std']
df3['BOLD'] = df3['MA-TP'] - 2*df3['std']

fig3 = go.Figure(data=[go.Candlestick(x=df3['Date'],
                open=df3['Open'], high=df3['High'],
                low=df3['Low'], close=df3['Close'])
                     ])
fig3.update_layout(xaxis_rangeslider_visible=False)
fig3.add_trace(go.Scatter(x=df2['Date'], y=df2['SMA_50'], mode='lines', name='SMA 50'))
fig3.add_trace(go.Scatter(x=df2['Date'], y=df2['SMA_100'], mode='lines', name='SMA 100'))
fig3.add_trace(go.Scatter(x=df2['Date'], y=df2['BOLU'], mode='lines', name='Bande de Bollinger (up)'))
fig3.add_trace(go.Scatter(x=df2['Date'], y=df2['BOLD'], mode='lines', name='Bande de Bollinger (down)'))

fig3.update_layout(
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    )
)



# Affichage du graphique dans Streamlit
if crypto == "Bitcoin":
      st.plotly_chart(fig2)
      col1, col2, col3 = st.columns(3)
      
      image1 = Image.open('./1.png')
      image2 = Image.open('./2.png')
      image3 = Image.open('./4.png')
      
      col1.image(image1, caption='Moyenne mobile 50 passe haussière')
      col2.image(image2, caption='Franchissement résistance horizontale')
      col3.image(image3, caption='Le cours se situe en dessous du point pivot S1')

    
elif crypto == "Ethereum":
      st.plotly_chart(fig3)
      
      image1 = Image.open('./3.png')
      image2 = Image.open('./4.png')
      image3 = Image.open('./5.png')
      image4 = Image.open('./7.png')
      
      col1.image(image1, caption='')
      col2.image(image2, caption='')
      col3.image(image3, caption='')
      col4.image(image4, caption='')



