import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Lab 6 – Spektral Samaradorlik Analizi")

st.markdown("""
WDM tizimlarida kanal soni oshgani sari spektral samaradorlik qanday o'zgarishini o'rganamiz.
""")

# Parametrlar
bandwidth_per_channel = st.slider("Har bir kanal uchun o'tkazuvchanlik (Gbps):", min_value=1.0, max_value=50.0, value=10.0, step=0.5)
channel_spacing = st.slider("Kanal orasidagi masofa (GHz):", min_value=10.0, max_value=100.0, value=50.0, step=1.0)
num_channels = st.slider("Kanal soni:", min_value=1, max_value=100, value=20, step=1)

# Hisoblash: Spektral samaradorlik (bit/s/Hz) = jami o'tkazuvchanlik / umumiy spektral kenglik
# jami o'tkazuvchanlik = channel bandwidth * number of channels (Gbps -> bit/s = *1e9)
# umumiy spektral kenglik = channel spacing * number of channels (GHz -> Hz = *1e9)

total_bandwidth_bps = bandwidth_per_channel * 1e9 * num_channels
total_spectral_width_hz = channel_spacing * 1e9 * num_channels

spectral_efficiency = total_bandwidth_bps / total_spectral_width_hz  # bit/s/Hz

st.write(f"**Spektral samaradorlik:** {spectral_efficiency:.3f} bit/s/Hz")

# Grafik: Kanal soni vs Spektral samaradorlik
channels_range = np.arange(1, 101)
total_bandwidth_arr = bandwidth_per_channel * 1e9 * channels_range
total_spectral_width_arr = channel_spacing * 1e9 * channels_range
spectral_efficiency_arr = total_bandwidth_arr / total_spectral_width_arr

fig, ax = plt.subplots()
ax.plot(channels_range, spectral_efficiency_arr, label="Spektral samaradorlik")
ax.axvline(num_channels, color='red', linestyle='--', label=f"Tanlangan kanal soni: {num_channels}")
ax.set_xlabel("Kanal soni")
ax.set_ylabel("Spektral samaradorlik (bit/s/Hz)")
ax.set_title("Kanal soni va Spektral samaradorlik")
ax.grid(True)
ax.legend()

st.pyplot(fig)
