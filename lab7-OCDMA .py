import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def run_lab7():
    st.header("📊 Laboratoriya 7 – OCDMA Kodingi va Interferensiya")

    st.write("""
    Ushbu laboratoriyada OCDMA kod uzunligi va foydalanuvchi soni asosida tizimdagi xatolik ehtimolini (BER) tahlil qilamiz.
    """)

    # Kirish parametrlar
    code_length = st.slider("🔢 Kod uzunligi (chiplar soni)", min_value=31, max_value=511, value=127, step=32)
    max_users = st.slider("👥 Maksimal foydalanuvchi soni", min_value=5, max_value=100, value=50, step=5)

    users = np.arange(1, max_users + 1)
    ber = np.exp(users / (2 * code_length)) - 1
    ber = np.clip(ber, 0, 1)  # BER qiymati 0–1 oraliqda bo'lishi kerak

    # Grafik
    fig, ax = plt.subplots()
    ax.plot(users, ber, marker='o', color='crimson')
    ax.set_xlabel("Foydalanuvchilar soni")
    ax.set_ylabel("Bit Error Rate (BER)")
    ax.set_title("OCDMA: BER vs Foydalanuvchilar soni")
    ax.grid(True)
    st.pyplot(fig)

    st.success(f"{max_users} ta foydalanuvchi va kod uzunligi {code_length} bo‘lsa, BER ≈ {ber[-1]:.4f}")
