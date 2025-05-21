import streamlit as st
import plotly.graph_objects as go
import numpy as np

def app():
    st.title("Lab 4: Hybrid WDM/OCDMA PON Arxitekturasi")

    st.write("""
    Ushbu laboratoriyada WDM va OCDMA texnologiyalarining kombinatsiyasi yordamida 
    PON tizimining samaradorligini o‘rganamiz.
    """)

    kanal_soni = st.slider("Kanal sonini tanlang", 1, 16, 8)

    # Simulyatsiya uchun signal o'tish tezligi (Mbps) ni yaratamiz
    # Har bir kanal uchun tasodifiy tezliklar
    np.random.seed(42)
    tezliklar = np.random.uniform(50, 150, kanal_soni)

    # Grafik chizamiz
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=[f"Kanal {i+1}" for i in range(kanal_soni)],
        y=tezliklar,
        marker_color='lightskyblue'
    ))

    fig.update_layout(
        title="Har bir kanal uchun o'tish tezligi (Mbps)",
        xaxis_title="Kanal",
        yaxis_title="Tezlik (Mbps)",
        yaxis=dict(range=[0, 200])
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info("Bu yerda haqiqiy simulyatsiya va tahlil kodini qo‘shishingiz mumkin.")
