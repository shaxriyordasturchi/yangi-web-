import streamlit as st

st.set_page_config(page_title="WDM/OCDMA/PON Lab App", layout="wide")

st.title("🌐 WDM/OCDMA/PON Laboratoriya Multipage App")

# Yon panelda sahifa tanlash
page = st.sidebar.selectbox("📚 Sahifani tanlang", [
    "Login",
    "Laboratoriya 1 - WDM Kanal",
    "Laboratoriya 2 - OCDMA Kodlash",
    "Laboratoriya 3 - PON Optik Uzilish",
    "Admin Panel"
])

if page == "Login":
    import login
    login.app()
elif page == "Laboratoriya 1 - WDM Kanal":
    import lab1_wdm
    lab1_wdm.app()
elif page == "Laboratoriya 2 - OCDMA Kodlash":
    import lab2_ocdma
    lab2_ocdma.app()
elif page == "Laboratoriya 3 - PON Optik Uzilish":
    import lab3_pon
    lab3_pon.app()
elif page == "Admin Panel":
    import admin
    admin.app()
