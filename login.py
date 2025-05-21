import streamlit as st
from utils import create_user_table, add_user, login_user, hash_password

def app():
    st.title("🔐 Foydalanuvchi Kirish")

    create_user_table()

    menu = ["Kirish", "Ro'yxatdan o'tish"]
    choice = st.radio("Amalni tanlang", menu)

    if choice == "Ro'yxatdan o'tish":
        st.subheader("Ro'yxatdan o'tish")
        new_user = st.text_input("Foydalanuvchi nomi")
        new_password = st.text_input("Parol", type='password')
        if st.button("Ro'yxatdan o'tish"):
            if new_user and new_password:
                if add_user(new_user, hash_password(new_password)):
                    st.success("Ro'yxatdan muvaffaqiyatli o'tdingiz!")
                else:
                    st.error("Foydalanuvchi allaqachon mavjud!")
            else:
                st.error("Iltimos, maydonlarni to'ldiring!")

    elif choice == "Kirish":
        st.subheader("Kirish")
        username = st.text_input("Foydalanuvchi nomi")
        password = st.text_input("Parol", type='password')
        if st.button("Kirish"):
            if username and password:
                user = login_user(username, hash_password(password))
                if user:
                    st.success(f"Xush kelibsiz, {username}!")
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.experimental_rerun()
                else:
                    st.error("Login yoki parol noto‘g‘ri!")
