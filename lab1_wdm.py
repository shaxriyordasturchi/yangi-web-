import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def app():
    st.title("📡 WDM Kanal Simulyatsiyasi")

    st.write("Ushbu laboratoriyada 3 ta sinusoidal signal WDM kanalida taqdim etiladi.")

    # Signal parametrlari
    x = np.linspace(0, 10, 500)
    signal1 = np.sin(x)
    signal2 = np.sin(2 * x)
    signal3 = np.sin(3 * x)

    # Grafik chizish
    fig, ax = plt.subplots()
    ax.plot(x, signal1, label="Signal 1 (freq = 1 Hz)")
    ax.plot(x, signal2, label="Signal 2 (freq = 2 Hz)")
    ax.plot(x, signal3, label="Signal 3 (freq = 3 Hz)")

    ax.set_xlabel("Vaqt (s)")
    ax.set_ylabel("Signal Amplitudasi")
    ax.set_title("WDM Kanalidagi 3 ta Signal")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)
