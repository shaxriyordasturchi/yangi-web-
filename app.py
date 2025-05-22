import streamlit as st
from login import app as login_app
import lab1_wdm
import lab2_ocdma
import lab3_pon
import lab4_hybrid
import lab5_error_correction

def main():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "username" not in st.session_state:
        st.session_state.username = ""

    if not st.session_state.logged_in:
        login_app()
    else:
        st.sidebar.title(f"Xush kelibsiz, {st.session_state.username}!")
        page = st.sidebar.selectbox("Sahifa tanlang", [
            "Bosh sahifa",  
            "Lab 1 - WDM Kanal Simulyatsiyasi", 
            "Lab 2 - OCDMA Kodlash va Dekodlash", 
            "Lab 3 - PON Tarmog‘i Tuzilishi",
            "Lab 4 - WDM/OCDMA Gibrid Arxitekturasi",
            "Lab 5 - Tarmoqlarda Xatolikni Tahlil va Tuzatish"
        ])

        if page == "Bosh sahifa":
            st.title("🏠 Bosh sahifa")
            st.write("Bu asosiy sahifa yoki foydalanuvchi paneli.")
            if st.button("Chiqish"):
                st.session_state.logged_in = False
                st.session_state.username = ""
                st.experimental_rerun()

        elif page == "Lab 1 - WDM Kanal Simulyatsiyasi":
            lab1_wdm.app()

        elif page == "Lab 2 - OCDMA Kodlash va Dekodlash":
            lab2_ocdma.app()

        elif page == "Lab 3 - PON Tarmog‘i Tuzilishi":
            lab3_pon.app()

        elif page == "Lab 4 - WDM/OCDMA Gibrid Arxitekturasi":
            lab4_hybrid.app()

        elif page == "Lab 5 - Tarmoqlarda Xatolikni Tahlil va Tuzatish":
            lab5_error_correction.app()

if __name__ == "__main__":
    main()
