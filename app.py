import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sqlite3

def login_page():
    st.title("🔐 Foydalanuvchi Kirish")
    username = st.text_input("Foydalanuvchi nomi")
    password = st.text_input("Parol", type="password")
    if st.button("Kirish"):
        # Bu yerda oddiy tekshiruv, haqiqiy loyihada ma'lumotlar bazasi bilan bog'laning
        if username == "SHAXRIYOR" and password == "SHAXRIYOR0219":
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.experimental_rerun()
        else:
            st.error("Login yoki parol noto‘g‘ri!")

def admin_panel():
    st.header("🛠️ Admin Panel")
    st.write("Bu yerda admin panel kodi joylashadi.")
    # Siz oldingi admin_panel() funksiyangizni shu yerga qo‘shishingiz mumkin.

def lab1():
    st.subheader("Laboratoriya 1: WDM Kanal Simulyatsiyasi")
    num_signals = st.slider("Kanalga beriladigan signal soni", 1, 5, 3)
    signal_power = st.slider("Har bir signal kuchi", 0.1, 10.0, 1.0)
    noise_power = st.slider("Shovqin kuchi", 0.01, 1.0, 0.1)

    x = np.linspace(0, 10, 500)
    fig, ax = plt.subplots()
    total_signal = np.zeros_like(x)
    for i in range(num_signals):
        freq = (i + 1) * 0.5
        signal = signal_power * np.sin(2 * np.pi * freq * x)
        ax.plot(x, signal, label=f"Signal {i+1}")
        total_signal += signal

    noise = noise_power * np.random.normal(size=x.shape)
    received_signal = total_signal + noise
    ax.plot(x, received_signal, label="Qabul qilingan signal (shovqin bilan)", color="black", linewidth=2)
    ax.set_xlabel("Vaqt")
    ax.set_ylabel("Signal kuchi")
    ax.legend()
    st.pyplot(fig)

def lab2():
    st.subheader("Laboratoriya 2: Oddiy Signalning Spektral Tahlili")
    # Misol uchun, oddiy Fourier transform grafigi
    t = np.linspace(0, 1, 500)
    freq = st.slider("Signal chastotasi (Hz)", 1, 50, 10)
    signal = np.sin(2 * np.pi * freq * t)
    st.line_chart(signal)
    st.write("Signalning Fourier spektri:")
    spectrum = np.abs(np.fft.fft(signal))
    st.line_chart(spectrum)

def lab3():
    st.subheader("Laboratoriya 3: Simulyatsiya Natijalarini Tahlil Qilish")
    st.write("Bu yerga laboratoriya natijalarini tahlil qilish uchun kod qo‘shing.")
    st.write("Masalan, statistikalar, grafiklar va h.k.")

def app():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if not st.session_state["logged_in"]:
        login_page()
    else:
        st.success(f"Xush kelibsiz, {st.session_state['username']}!")
        page = st.radio("Amalni tanlang:", ("Admin Panel", "Laboratoriya"))

        if page == "Admin Panel":
            admin_panel()
        elif page == "Laboratoriya":
            st.header("🧪 Laboratoriya bo‘limi")
            lab_choice = st.selectbox("Laboratoriya tanlang:", ["Laboratoriya 1", "Laboratoriya 2", "Laboratoriya 3"])

            if lab_choice == "Laboratoriya 1":
                lab1()
            elif lab_choice == "Laboratoriya 2":
                lab2()
            elif lab_choice == "Laboratoriya 3":
                lab3()

        if st.button("Chiqish"):
            st.session_state["logged_in"] = False
            st.experimental_rerun()

if __name__ == "__main__":
    app()

