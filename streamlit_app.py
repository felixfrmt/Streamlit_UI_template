import streamlit as st
import pandas as pd
import numpy as np

st.markdown(
    """
    <style>
    .title {
        width: 80%;
        text-align: center;
        }
    .text {
        width: 80%;
        }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("Analyse des crypto-monnaies")

st.text("Selectionnez une crypto-monnaie et visualisez le cours de sa valeur issue des données de Binance. L'analyse technique ensuite générée permet de calculer les indicateurs utilisés et d'afficher des alertes sur ces indicateurs."
)
