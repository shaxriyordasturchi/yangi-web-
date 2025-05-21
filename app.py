import streamlit as st
from login import app as login_app
from admin import app as admin_app
from lab1_wdm import app as lab1_app
from lab2_ocdma import app as lab2_app
from lab3_pon import app as lab3_app

def main():
    st.set_page_config(page_title="WDM/OCDMA/PON Web App", layout="wide", page_icon="🌐")

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "username" not in st.session_state:
        st.session_state.username = ""

    if not st.session_state.logged_in:
        login_app()
    else:
        st.sidebar.title(f"Xush kelibsiz, {st.session_state.username}!")
        choice = st.sidebar.radio("Sahifani tanlang", ["🏠 Bosh sahifa", "🛠️ Admin", "💡 Lab 1 - WDM", "🔓 Lab 2 - OCDMA", "📡 Lab 3 - PON", "🚪 Chiqish"])

        if choice == "🏠 Bosh sahifa":
            st.title("Bosh sahifa")
            st.write("Bu yerda umumiy ma’lumotlar bo‘ladi.")

        elif choice == "🛠️ Admin":
            admin_app()

        elif choice == "💡 Lab 1 - WDM":
            lab1_app()

        elif choice == "🔓 Lab 2 - OCDMA":
            lab2_app()

        elif choice == "📡 Lab 3 - PON":
            lab3_app()

        elif choice == "🚪 Chiqish":
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.experimental_rerun()

if __name__ == "__main__":
    main()
