import streamlit as st
import login
import admin
import lab1_wdm
import lab2_ocdma
import lab3_pon

def app():
    # Session holatini tekshirish va o‘rnatish
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "username" not in st.session_state:
        st.session_state.username = ""

    # Agar foydalanuvchi login qilmagan bo‘lsa
    if not st.session_state.logged_in:
        login.app()
    else:
        # Yon panel va sahifa tanlash
        st.sidebar.title(f"👤 Xush kelibsiz, {st.session_state.username}!")
        page = st.sidebar.selectbox("Sahifa tanlang", [
            "🏠 Bosh sahifa",
            "🛠️ Admin",
            "🔬 Lab 1 - WDM",
            "💡 Lab 2 - OCDMA",
            "🌐 Lab 3 - PON"
        ])

        if page == "🏠 Bosh sahifa":
            st.title("🏠 Bosh sahifa")
            st.success("Siz tizimga muvaffaqiyatli kirdingiz. Quyidagi yon panel orqali sahifalarni tanlang.")
            if st.button("🔓 Chiqish"):
                st.session_state.logged_in = False
                st.session_state.username = ""
                st.experimental_rerun()

        elif page == "🛠️ Admin":
            admin.app()

        elif page == "🔬 Lab 1 - WDM":
            lab1_wdm.app()

        elif page == "💡 Lab 2 - OCDMA":
            lab2_ocdma.app()

        elif page == "🌐 Lab 3 - PON":
            lab3_pon.app()

# Streamlit ishga tushganda shu funksiyani chaqiradi
if __name__ == "__main__":
    app()
