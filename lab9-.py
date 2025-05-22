import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def run_lab9():
    st.header("📊 Laboratoriya 9 – Hybrid Tarmoqda Faol Foydalanuvchilar Yuki")

    st.write("""
    WDM-OCDMA-PON tarmoqlarida faol foydalanuvchi soni ortgani sari kanal yuklanishi qanday o‘zgarishini tahlil qilamiz.
    """)

    max_users = st.slider("👥 Faol foydalanuvchi soni", 10, 500, 100, step=10)
    total_channels = st.slider("📡 Umumiy kanal soni", 8, 64, 32, step=4)

    users = np.arange(1, max_users + 1)
    load = users / total_channels
    load = np.clip(load, 0, 1)  # 100% dan ortiq yuklanish bo‘lmasin

    # Grafik
    fig, ax = plt.subplots()
    ax.plot(users, load, color='orange')
    ax.set_xlabel("Faol foydalanuvchilar soni")
    ax.set_ylabel("Kanal yuklanishi (0–1)")
    ax.set_title("Hybrid tarmoq: Kanal yuklanishi")
    ax.grid(True)
    st.pyplot(fig)

    st.success(f"{max_users} foydalanuvchi va {total_channels} kanal uchun yuklanish ≈ {load[-1]*100:.1f}%")
