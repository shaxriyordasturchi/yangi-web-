import streamlit as st
from utils import create_user_table, add_user, login_user, hash_password

def app():
    st.title("🔐 Foydalanuvchi Kirish")

    # Bazada userlar jadvalini yaratamiz (faqat bir marta)
    create_user_table()

    menu = ["Kirish", "Ro'yxatdan o'tish"]
    choice = st.radio("Amalni tanlang", menu)

    if choice == "Ro'yxatdan o'tish":
        st.subheader("Ro'yxatdan o'tish")
        new_user = st.text_input("Foydalanuvchi nomi")
        new_password = st.text_input("Parol", type='password')
        if st.button("Ro'yxatdan o'tish"):
            if new_user and new_password:
                hashed_password = hash_password(new_password)
                success = add_user(new_user, hashed_password)  # <-- Shu yerda natijani olamiz
                if success:
                    st.success("Ro'yxatdan muvaffaqiyatli o'tdingiz!")
                else:
                    st.error("Bu foydalanuvchi nomi allaqachon mavjud!")
            else:
                st.error("Iltimos, barcha maydonlarni to'ldiring!")

    elif choice == "Kirish":
        st.subheader("Kirish")
        username = st.text_input("Foydalanuvchi nomi")
        password = st.text_input("Parol", type='password')
        if st.button("Kirish"):
            if username and password:
                hashed_password = hash_password(password)
                user = login_user(username, hashed_password)
                if user:
                    st.success(f"Xush kelibsiz, {username}!")
                    st.write("Bu yerda keyingi sahifaga o‘tish yoki ishga davom etish kodini yozing.")
                else:
                    st.error("Login yoki parol noto‘g‘ri!")
            else:
                st.error("Iltimos, foydalanuvchi nomi va parolni kiriting!")
