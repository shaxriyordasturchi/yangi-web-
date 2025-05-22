import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Lab 8 – PON Delay Tahlili")

st.markdown("""
PON tarmog‘ida masofa va foydalanuvchi soni asosida kechikish (delay) tahlili.
""")

# Parametrlar
distance = st.slider("Masofa (km):", min_value=0.1, max_value=20.0, value=5.0, step=0.1)
num_users = st.slider("Foydalanuvchi soni:", min_value=1, max_value=64, value=16, step=1)

# O'tkazuvchanlik va kechikish hisoblash
# Assumptions:
# - Optik signal tezligi: c/n, c=3e8 m/s, n=1.5 (optik tolali)
c = 3e8
n = 1.5
speed = c / n  # m/s

# Masofa metrda
distance_m = distance * 1000

# Asosiy kechikish = signalning masofani bosib o'tish vaqti * 2 (ikki yo'nalishda)
delay_propagation = (distance_m / speed) * 2  # sekund

# Qo'shimcha kechikish - tarmoqqa ulanayotgan foydalanuvchilar soniga bog'liq (soddalashtirilgan)
# Misol uchun, har bir foydalanuvchi uchun 1 ms navbat kutish
delay_queueing = num_users * 1e-3  # sekund

total_delay = delay_propagation + delay_queueing  # sekund
total_delay_ms = total_delay * 1e3

st.write(f"**Umumiy kechikish:** {total_delay_ms:.3f} ms")

# Grafik: Masofa va foydalanuvchi soni vs Kechikish
distances = np.linspace(0.1, 20, 50)
users = np.arange(1, 65)

X, Y = np.meshgrid(distances, users)
Z = (X * 1000 / speed) * 2 + Y * 1e-3  # sekund
Z_ms = Z * 1e3

fig, ax = plt.subplots(figsize=(8,6))
c = ax.contourf(X, Y, Z_ms, levels=50, cmap='viridis')
fig.colorbar(c, ax=ax, label='Kechikish (ms)')
ax.set_xlabel('Masofa (km)')
ax.set_ylabel('Foydalanuvchi soni')
ax.set_title('Masofa va foydalanuvchi soni bo\'yicha kechikish')
st.pyplot(fig)
