import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def run_lab6():
    st.header("📊 Laboratoriya 6 – Spektral Samaradorlik Analizi")

    st.write("""
    Ushbu laboratoriyada WDM tizimida kanal soni oshgani sari spektral samaradorlik (bit/s/Hz) qanday o‘zgarishini o‘rganamiz.
    """)

    # Slider orqali foydalanuvchi parametr tanlaydi
    max_channels = st.slider("🔧 Maksimal kanal soni:", min_value=4, max_value=128, value=32, step=4)
    bandwidth = st.number_input("🌐 Umumiy optik diapazon (Hz)", value=5e12, step=1e12, format="%.0e")

    # Hisoblash
    channels = np.arange(1, max_channels + 1)
    bitrate_per_channel = 10e9  # Har bir kanal uchun 10 Gbps
    spectral_efficiency = (channels * bitrate_per_channel) / bandwidth

    # Grafik
    fig, ax = plt.subplots()
    ax.plot(channels, spectral_efficiency, marker='o')
    ax.set_xlabel("Kanal soni")
    ax.set_ylabel("Spektral samaradorlik (bit/s/Hz)")
    ax.set_title("Spektral samaradorlik vs Kanal soni")
    ax.grid(True)
    st.pyplot(fig)

    # Natijani chiqarish
    st.success(f"128 ta kanal uchun spektral samaradorlik: {spectral_efficiency[-1]:.2e} bit/s/Hz")
