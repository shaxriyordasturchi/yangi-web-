import streamlit as st
from utils import create_user_table, add_user, login_user, hash_password

create_user_table()

st.title("🔑 Kirish / Ro‘yxatdan O‘tish")

menu = ["Kirish", "Ro'yxatdan o'tish"]
choice = st.sidebar.selectbox("Tanlang", menu)

if choice == "Ro'yxatdan o'tish":
    st.subheader("Ro'yxatdan o'tish")
    new_name = st.text_input("Ismingiz")
    new_age = st.number_input("Yoshingiz", min_value=5, max_value=100)
    new_user = st.text_input("Login")
    new_password = st.text_input("Parol", type='password')
    if st.button("Ro'yxatdan o'tish"):
        if new_name and new_user and new_password and new_age:
            hashed_pass = hash_password(new_password)
            add_user(new_user, hashed_pass, new_name, new_age)
            st.success("Foydalanuvchi yaratildi! Kirish sahifasiga o'ting.")
        else:
            st.error("Iltimos, barcha maydonlarni to'ldiring.")

elif choice == "Kirish":
    st.subheader("Tizimga kirish")
    username = st.text_input("Login")
    password = st.text_input("Parol", type='password')
    if st.button("Kirish"):
        hashed_pass = hash_password(password)
        result = login_user(username, hashed_pass)
        if result:
            st.success(f"Xush kelibsiz, {result[2]}!")
            st.write("Keyingi sahifaga o‘tish uchun Streamlit multipage navigatsiyasidan foydalaning.")
            # Bu yerda sessiya holati yoki boshqa navigatsiya qo'shish mumkin
        else:
            st.error("Login yoki parol noto‘g‘ri!")
