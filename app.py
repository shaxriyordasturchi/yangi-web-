import streamlit as st
from login import app as login_app
from admin import app as admin_app
import lab1_wdm
import lab2_ocdma
import lab3_pon

# Streamlit sessiya holatini tekshiramiz
def main():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "username" not in st.session_state:
        st.session_state.username = ""

    if not st.session_state.logged_in:
        login_app()  # Kirish sahifasiga yo'naltiramiz
    else:
        st.sidebar.title(f"Xush kelibsiz, {st.session_state.username}!")
        page = st.sidebar.selectbox("Sahifa tanlang", [
            "Bosh sahifa", "Admin", "Lab 1 - WDM", "Lab 2 - OCDMA", "Lab 3 - PON"
        ])

        if page == "Bosh sahifa":
            st.title("🏠 Bosh sahifa")
            st.write("Bu asosiy sahifa yoki foydalanuvchi paneli.")
            if st.button("Chiqish"):
                st.session_state.logged_in = False
                st.session_state.username = ""
                st.experimental_rerun()

        elif page == "Admin":
            admin_app()

        elif page == "Lab 1 - WDM":
            lab1_wdm.app()

        elif page == "Lab 2 - OCDMA":
            lab2_ocdma.app()

        elif page == "Lab 3 - PON":
            lab3_pon.app()

if __name__ == "__main__":
    main()
