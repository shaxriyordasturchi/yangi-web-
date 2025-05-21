import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def app():
    st.title("🏗️ Laboratoriya 3: PON Optik Uzilish Aniqlash")

    # Parametrlar
    fiber_length = st.slider("Optik tol uzunligi (km)", min_value=1, max_value=50, value=10)
    break_position = st.slider("Uzilish joyi (km)", min_value=0, max_value=fiber_length, value=5)
    signal_power = 10  # boshlang‘ich signal kuchi (dBm)

    # Signal yo‘qotilishi (attenuatsiya) km ga
    attenuation_db_per_km = 0.2
    loss_before_break = attenuation_db_per_km * break_position
    loss_after_break = attenuation_db_per_km * (fiber_length - break_position)

    # Signal kuchini hisoblash
    power_before_break = signal_power - loss_before_break
    power_after_break = power_before_break - 20  # Uzilishda katta yo‘qotish (+20dB kamayish)

    # Grafik chizish
    x = np.linspace(0, fiber_length, 500)
    power = np.piecewise(
        x,
        [x <= break_position, x > break_position],
        [lambda x: signal_power - attenuation_db_per_km * x,
         lambda x: power_before_break - 20 - attenuation_db_per_km * (x - break_position)]
    )

    fig, ax = plt.subplots()
    ax.plot(x, power, label="Signal kuchi (dBm)")
    ax.axvline(break_position, color='red', linestyle='--', label="Uzilish joyi")
    ax.set_xlabel("Optik tol uzunligi (km)")
    ax.set_ylabel("Signal kuchi (dBm)")
    ax.set_title("PON Optik Uzilish Aniqlash")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    st.write(f"Uzilish joyi: {break_position} km da")

    if st.button("Natijalarni PDF ga eksport qilish"):
        from utils import export_pdf
        username = st.session_state.get("username", "Anonim")
        result_data = {
            "Tol uzunligi (km)": fiber_length,
            "Uzilish joyi (km)": break_position,
            "Signal kuchi boshlanishi (dBm)": signal_power,
            "Signal kuchi uzilishdan oldin (dBm)": round(power_before_break, 2),
            "Signal kuchi uzilishdan keyin (dBm)": round(power_after_break, 2)
        }
        export_pdf(username, result_data)
