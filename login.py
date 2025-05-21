import streamlit as st
import sqlite3
import hashlib

# Parolni hash qilish funksiyasi
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

# Hashlangan parolni tekshirish funksiyasi
def check_hashes(password, hashed_text):
    return make_hashes(password) == hashed_text

# Ma'lumotlar bazasi funksiyalari
def create_usertable():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, password TEXT)')
    conn.commit()
    conn.close()

def add_userdata(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('INSERT INTO userstable(username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()

def login_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM userstable WHERE username = ? AND password = ?', (username, password))
    data = c.fetchall()
    conn.close()
    return data

# Kirish sahifasi
def app():
    st.title("🔐 Foydalanuvchi Kirish")
    menu = ["Kirish", "Ro'yxatdan o'tish"]
    choice = st.selectbox("Amalni tanlang", menu)

    create_usertable()

    if choice == "Kirish":
        st.subheader("Kirish")

        username = st.text_input("Foydalanuvchi nomi")
        password = st.text_input("Parol", type='password')

        if st.button("Kirish"):
            hashed_pwd = make_hashes(password)
            result = login_user(username, hashed_pwd)
            if result:
                st.success(f"Xush kelibsiz, {username}!")
                st.session_state.logged_in = True
                st.session_state.username = username
                st.experimental_rerun()  # Sahifani yangilash
            else:
                st.error("Login yoki parol noto‘g‘ri.")

    elif choice == "Ro'yxatdan o'tish":
        st.subheader("Yangi foydalanuvchi")

        new_user = st.text_input("Yangi foydalanuvchi nomi")
        new_password = st.text_input("Yangi parol", type='password')

        if st.button("Ro‘yxatdan o‘tish"):
            add_userdata(new_user, make_hashes(new_password))
            st.success("Ro'yxatdan o'tish muvaffaqiyatli. Endi Kirish sahifasiga o'ting.")
