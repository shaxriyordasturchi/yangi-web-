import streamlit as st

users_db = {"SHAXRIYOR": "SHAXRIYOR0219"}

def login_page():
    st.title("🔐 Foydalanuvchi Kirish")
    username = st.text_input("Foydalanuvchi nomi")
    password = st.text_input("Parol", type="password")
    login_btn = st.button("Kirish")

    if login_btn:
        if username in users_db and users_db[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.page = "admin_panel"
            st.experimental_rerun()
        else:
            st.error("Noto‘g‘ri foydalanuvchi nomi yoki parol!")

def admin_panel():
    st.title(f"Xush kelibsiz, {st.session_state.username}!")
    st.write("Bu yerda admin panel ishga tushadi.")
    if st.button("Chiqish"):
        st.session_state.logged_in = False
        st.session_state.page = "login"
        st.experimental_rerun()

def app():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "page" not in st.session_state:
        st.session_state.page = "login"
    if "username" not in st.session_state:
        st.session_state.username = None

    if st.session_state.logged_in and st.session_state.page == "admin_panel":
        admin_panel()
    else:
        login_page()

if __name__ == "__main__":
    app()
