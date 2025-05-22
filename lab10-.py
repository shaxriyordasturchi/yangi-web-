import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, erfc

st.title("Lab 10 – BER tahlili barcha texnologiyalarda")

st.markdown("""
WDM, OCDMA, PON va ularning gibridlarida BER (Bit Error Rate) taqqoslash.
""")

# Parametrlar
num_users = st.slider("Foydalanuvchilar soni:", min_value=1, max_value=100, value=20, step=1)
code_length_ocdma = st.slider("OCDMA kod uzunligi:", min_value=8, max_value=128, value=32, step=8)
distance_pon = st.slider("PON masofasi (km):", min_value=0.1, max_value=20.0, value=5.0, step=0.1)

# BER uchun oddiy modellar:

# WDM: Faraz qilamiz BER doimiy past (masalan 1e-6)
ber_wdm = 1e-6

# OCDMA (ber ocda formuladan)
if num_users > 1:
    ber_ocdma = 0.5 * erfc(sqrt(code_length_ocdma / (2 * (num_users - 1))))
else:
    ber_ocdma = 0.0

# PON kechikish va masofadan kelib chiqib BERni o'ylaymiz (oddiy model):
# BER oshishi masofa bilan (exponential)
ber_pon = min(1.0, 1e-5 * np.exp(distance_pon / 5))

# Hybrid (gibrid) – WDM va OCDMA BER aralashmasi (oddiy o‘rtacha)
ber_hybrid = (ber_wdm + ber_ocdma) / 2

technologies = ['WDM', 'OCDMA', 'PON', 'Hybrid (WDM+OCDMA)']
ber_values = [ber_wdm, ber_ocdma, ber_pon, ber_hybrid]

fig, ax = plt.subplots()
bars = ax.bar(technologies, ber_values, color=['blue', 'orange', 'green', 'purple'])
ax.set_yscale('log')
ax.set_ylabel('BER (log scale)')
ax.set_title('Texnologiyalar bo\'yicha BER taqqoslash')
ax.grid(True, which='both', linestyle='--')

for bar, val in zip(bars, ber_values):
    height = bar.get_height()
    ax.annotate(f'{val:.2e}', xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')

st.pyplot(fig)
