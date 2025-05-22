import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Lab 7 – OCDMA Kodingi va Interferensiya")

st.markdown("""
OCDMA tizimida kod uzunligi va foydalanuvchi soni asosida interferensiya va BER (Bit Error Rate) tahlili.
""")

# Parametrlar
code_length = st.slider("Kod uzunligi (chiplar soni):", min_value=8, max_value=128, value=32, step=8)
num_users = st.slider("Foydalanuvchi soni:", min_value=1, max_value=50, value=10, step=1)

# BER hisoblash (soddalashtirilgan model):
# BER ≈ 0.5 * erfc(sqrt(code_length / (2 * (num_users - 1))))
# erfc — komplementar xato funktsiyasi, scipy kutubxonasidan kerak, ammo soddalashtirish uchun approx qilamiz.

from math import sqrt, erfc

if num_users > 1:
    ber = 0.5 * erfc(sqrt(code_length / (2 * (num_users - 1))))
else:
    ber = 0.0

st.write(f"**BER (Bit Error Rate):** {ber:.4e}")

# Grafik: Foydalanuvchi soni vs BER turli kod uzunliklarida

users_range = np.arange(1, 51)
code_lengths = [8, 16, 32, 64, 128]
plt.figure(figsize=(8,5))

for cl in code_lengths:
    ber_arr = []
    for u in users_range:
        if u > 1:
            val = 0.5 * erfc(sqrt(cl / (2 * (u - 1))))
        else:
            val = 0
        ber_arr.append(val)
    plt.plot(users_range, ber_arr, label=f"Kod uzunligi: {cl}")

plt.yscale('log')
plt.xlabel("Foydalanuvchi soni")
plt.ylabel("BER (log scale)")
plt.title("Foydalanuvchi soni va BER (log-o'lcham)")
plt.grid(True, which='both', linestyle='--')
plt.legend()
st.pyplot(plt.gcf())
