import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.graph_objects as go

st.markdown(
    """
    <style>
    .block-container {
        width: 80%;
        text-align: center;
        }
      img {
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
df1 = pd.read_csv('https://raw.githubusercontent.com/matplotlib/mplfinance/2710cf4bb3d0c19fe9bda19c0b999588b658ed26/examples/data/yahoofinance-INTC-19950101-20040412.csv')


df1['SMA_50'] = df1['Close'].rolling(window=50).mean()
df1['SMA_100'] = df1['Close'].rolling(window=100).mean()

df1['TP'] = (df1['Close'] + df1['Low'] + df1['High'])/3
df1['std'] = df1['TP'].rolling(20).std(ddof=0)
df1['MA-TP'] = df1['TP'].rolling(20).mean()
df1['BOLU'] = df1['MA-TP'] + 2*df1['std']
df1['BOLD'] = df1['MA-TP'] - 2*df1['std']

fig1 = go.Figure(data=[
      go.Candlestick(
            x=df1['Date'],
            open=df1['Open'], 
            high=df1['High'],
            low=df1['Low'],
            close=df1['Close'])
      ])

fig1.update_layout(xaxis_rangeslider_visible=False)
fig1.add_trace(go.Scatter(x=df1['Date'], y=df1['SMA_50'], mode='lines', name='SMA 50'))
fig1.add_trace(go.Scatter(x=df1['Date'], y=df1['SMA_100'], mode='lines', name='SMA 100'))
fig1.add_trace(go.Scatter(x=df1['Date'], y=df1['BOLU'], mode='lines', name='Bande de Bollinger (up)'))
fig1.add_trace(go.Scatter(x=df1['Date'], y=df1['BOLD'], mode='lines', name='Bande de Bollinger (down)'))

fig1.update_layout(
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="left",
        x=0
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

fig2 = go.Figure(data=[
            go.Candlestick(
                  x=df2['Date'],
                  open=df2['AAPL.Open'], 
                  high=df2['AAPL.High'],
                  low=df2['AAPL.Low'],
                  close=df2['AAPL.Close'])
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
        xanchor="left",
        x=0
    )
)

################################## Generate BITCOIN's Data  #####################################
df3 = pd.read_csv('https://raw.githubusercontent.com/matplotlib/mplfinance/2710cf4bb3d0c19fe9bda19c0b999588b658ed26/examples/data/SPY_20110701_20120630_Bollinger.csv')

df3['SMA_50'] = df3['Close'].rolling(window=50).mean()
df3['SMA_100'] = df3['Close'].rolling(window=100).mean()

df3['TP'] = (df3['Close'] + df3['Low'] + df3['High'])/3
df3['std'] = df3['TP'].rolling(20).std(ddof=0)
df3['MA-TP'] = df3['TP'].rolling(20).mean()
df3['BOLU'] = df3['MA-TP'] + 2*df3['std']
df3['BOLD'] = df3['MA-TP'] - 2*df3['std']

fig3 = go.Figure(data=[
            go.Candlestick(
                  x=df3['Date'],
                  open=df3['Open'],
                  high=df3['High'],
                  low=df3['Low'],
                  close=df3['Close'])
            ])

fig3.update_layout(xaxis_rangeslider_visible=False)
fig3.add_trace(go.Scatter(x=df3['Date'], y=df3['SMA_50'], mode='lines', name='SMA 50'))
fig3.add_trace(go.Scatter(x=df3['Date'], y=df3['SMA_100'], mode='lines', name='SMA 100'))
fig3.add_trace(go.Scatter(x=df3['Date'], y=df3['BOLU'], mode='lines', name='Bande de Bollinger (up)'))
fig3.add_trace(go.Scatter(x=df3['Date'], y=df3['BOLD'], mode='lines', name='Bande de Bollinger (down)'))

fig3.update_layout(
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="left",
        x=0
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
      
      col1, col2, col3 = st.columns(3)
      
      image1 = Image.open('./3.png')
      image2 = Image.open('./5.png')
      image3 = Image.open('./6.png')
      
      col1.image(image1, caption="Gap d'ouverture haussier")
      col2.image(image2, caption='RSI en sur-achat au dessus de 80')
      col3.image(image3, caption='Le cours se situe au dessus du point pivot R3')

elif crypto == "BNB":
      st.plotly_chart(fig1)
      
      col1, col2, col3 = st.columns(3)
      
      image1 = Image.open('./3.png')
      image2 = Image.open('./8.png')
      image3 = Image.open('./9.png')
      image4 = Image.open('./7.png')
      
      col1.image(image1, caption="Gap d'ouverture haussier")
      col2.image(image2, caption='Le cours croise à la baisse la moyenne mobile adaptative 20')
      col3.image(image3, caption='Proximité résistance horizontale')
      col1.image(image4, caption='Ouverture baissière')
    
