import streamlit as st
import plotly.graph_objects as go
import numpy as np

def app():
    st.title("Lab 5: Xatoliklarni Tuzatish Kodlari")

    st.write("""
    Ushbu laboratoriyada PON tizimlarida xatoliklarni tuzatish 
    uchun qo‘llaniladigan kodlarni o‘rganamiz.
    """)

    # Xatoliklar foizda (%)
    kod_bosqichlari = ["Kodlash", "Dekodlash", "Sinov"]
    xatoliklar = [5, 2, 1]  # Masalan

    # Interaktiv radio tugma tanlovi
    tanlov = st.radio("Kodlash bosqichlarini tanlang", kod_bosqichlari)

    # Grafik uchun index
    idx = kod_bosqichlari.index(tanlov)

    # Grafik yaratish
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=xatoliklar[idx],
        title={'text': f"{tanlov} bosqichidagi xatolik darajasi (%)"},
        gauge={'axis': {'range': [0, 10]},
               'bar': {'color': "red"},
               'steps': [
                   {'range': [0, 3], 'color': "lightgreen"},
                   {'range': [3, 7], 'color': "yellow"},
                   {'range': [7, 10], 'color': "red"}]}
    ))

    st.plotly_chart(fig, use_container_width=True)

    st.info("Bu yerda xatoliklarni aniqlash va tuzatish algoritmini qo‘shishingiz mumkin.")
