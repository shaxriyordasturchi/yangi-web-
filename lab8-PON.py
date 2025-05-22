import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def run_lab8():
    st.header("📊 Laboratoriya 8 – PON Delay Tahlili")

    st.write("""
    PON tarmog‘ida masofa va foydalanuvchi soni ortgani sari kechikish (delay) qanday o‘zgarishini tahlil qilamiz.
    """)

    max_distance = st.slider("📏 Maksimal masofa (km)", min_value=10, max_value=100, value=40, step=10)
    users = st.slider("👥 Foydalanuvchi soni", min_value=1, max_value=64, value=16)

    distances = np.linspace(1, max_distance, 50)
    propagation_delay = distances * 5  # ms/km (taxminan 5 ms/km)
    queueing_delay = users * 0.3  # ms

    total_delay = propagation_delay + queueing_delay

    # Grafik
    fig, ax = plt.subplots()
    ax.plot(distances, total_delay, color='darkgreen')
    ax.set_xlabel("Masofa (km)")
    ax.set_ylabel("Kechikish (ms)")
    ax.set_title("PON: Kechikish vs Masofa")
    ax.grid(True)
    st.pyplot(fig)

    st.success(f"{max_distance} km va {users} foydalanuvchi uchun kechikish ≈ {total_delay[-1]:.1f} ms")
