import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def app():
    st.title("🏗️ Laboratoriya 1: WDM Kanal Simulyatsiyasi")

    # Parametrlar
    num_signals = st.slider("Kanalga beriladigan signal soni", min_value=1, max_value=5, value=3)
    signal_power = st.slider("Har bir signalning kuchi", min_value=0.1, max_value=10.0, value=1.0)
    noise_power = st.slider("Shovqin kuchi", min_value=0.01, max_value=1.0, value=0.1)

    # Signal yaratish
    x = np.linspace(0, 10, 500)
    fig, ax = plt.subplots()

    total_signal = np.zeros_like(x)
    for i in range(num_signals):
        freq = (i + 1) * 0.5
        signal = signal_power * np.sin(2 * np.pi * freq * x)
        ax.plot(x, signal, label=f"Signal {i+1}")
        total_signal += signal

    # Shovqin qo'shish
    noise = noise_power * np.random.normal(size=x.shape)
    received_signal = total_signal + noise

    ax.plot(x, received_signal, label="Qabul qilingan signal (shovqin bilan)", color="black", linewidth=2)
    ax.set_xlabel("Vaqt")
    ax.set_ylabel("Signal kuchi")
    ax.legend()
    st.pyplot(fig)

    # Natijalar
    st.write("### Simulyatsiya natijalari:")
    st.write(f"- Kanalga berilgan signal soni: {num_signals}")
    st.write(f"- Signal kuchi: {signal_power}")
    st.write(f"- Shovqin kuchi: {noise_power}")

    if st.button("Natijalarni PDF ga eksport qilish"):
        from utils import export_pdf
        username = st.session_state.get("username", "Anonim")  # agar login bilan bog‘lash bo‘lsa
        result_data = {
            "Signal soni": num_signals,
            "Signal kuchi": signal_power,
            "Shovqin kuchi": noise_power
        }
        export_pdf(username, result_data)
