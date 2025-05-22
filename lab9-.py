import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Lab 9 – Hybrid Tarmoqda Faol Foydalanuvchilar Yuki")

st.markdown("""
WDM-OCDMA-PON gibrid tarmoqlarida bir vaqtning o‘zida faol foydalanuvchilar soni bilan kanal yuklanishini tahlil qilamiz.
""")

# Parametrlar
max_users_wdm = st.slider("WDM maksimal foydalanuvchilari:", min_value=1, max_value=100, value=50, step=1)
max_users_ocdma = st.slider("OCDMA maksimal foydalanuvchilari:", min_value=1, max_value=50, value=25, step=1)
max_users_pon = st.slider("PON maksimal foydalanuvchilari:", min_value=1, max_value=64, value=32, step=1)

active_users = st.slider("Faol foydalanuvchilar soni (umumiy):", min_value=1, max_value=max_users_wdm + max_users_ocdma + max_users_pon, value=50, step=1)

# Kanal yuklanishini hisoblash (soddalashtirilgan):
# Yuk = Faol foydalanuvchilar / Maksimal foydalanuvchilar soni (0..1)

total_max_users = max_users_wdm + max_users_ocdma + max_users_pon
channel_load = active_users / total_max_users
channel_load = min(channel_load, 1.0)

st.write(f"**Umumiy kanal yuklanishi:** {channel_load:.2%}")

# Grafik: Faol foydalanuvchilar vs Kanal yuklanishi
users_range = np.arange(1, total_max_users + 1)
load_arr = users_range / total_max_users
load_arr = np.clip(load_arr, 0, 1)

fig, ax = plt.subplots()
ax.plot(users_range, load_arr, label="Kanal yuklanishi")
ax.axvline(active_users, color='red', linestyle='--', label=f"Tanlangan foydalanuvchilar: {active_users}")
ax.set_xlabel("Faol foydalanuvchilar soni")
ax.set_ylabel("Kanal yuklanishi (%)")
ax.set_title("Faol foydalanuvchilar va kanal yuklanishi")
ax.grid(True)
ax.legend()

st.pyplot(fig)
