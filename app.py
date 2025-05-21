import streamlit as st
import sqlite3

# --- Bazadan foydalanuvchilarni olish ---
def get_users():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT username, name, age FROM userstable")
    data = c.fetchall()
    conn.close()
    return data

# --- Admin paneli ---
def admin_panel():
    st.title("🛠️ Admin Panel - Foydalanuvchilar Boshqaruvi")

    users = get_users()

    if users:
        st.write("### Foydalanuvchilar ro‘yxati:")
        st.table({
            "Login": [u[0] for u in users],
            "Ism": [u[1] for u in users],
            "Yosh": [u[2] for u in users],
        })
    else:
        st.info("Hech qanday foydalanuvchi topilmadi.")

    st.write("---")
    st.subheader("Laboratoriya Natijalari (Namuna)")
    sample_results = {
        "Foydalanuvchi": "user123",
        "Laboratoriya": "WDM Kanal Simulyatsiyasi",
        "Natija": "Yaxshi",
        "Sana": "2025-05-21"
    }
    for k, v in sample_results.items():
        st.write(f"**{k}:** {v}")

# --- Login sahifasi ---
def login_page():
    st.title("🔐 Foydalanuvchi Kirish")

    username = st.text_input("Foydalanuvchi nomi")
    password = st.text_input("Parol", type="password")

    if st.button("Kirish"):
        if username == "SHAXRIYOR" and password == "SHAXRIYOR0219":
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.experimental_rerun()
        else:
            st.error("Foydalanuvchi nomi yoki parol noto‘g‘ri!")

# --- Asosiy dastur ---
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
            st.write("Bu yerga laboratoriya sahifasining kodini qo‘shing.")

        if st.button("Chiqish"):
            st.session_state["logged_in"] = False
            st.experimental_rerun()

if __name__ == "__main__":
    st.set_page_config(page_title="Foydalanuvchi Tizimi", layout="wide")
    app()
