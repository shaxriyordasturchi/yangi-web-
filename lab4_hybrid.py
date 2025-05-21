import streamlit as st

def app():
    st.title("Lab 4 - WDM/OCDMA Gibrid Arxitekturasi")
    st.write("""
    Ushbu laboratoriyada WDM (Wavelength Division Multiplexing) va OCDMA (Optical Code Division Multiple Access) 
    texnologiyalarining gibrid arxitekturasi haqida tushuncha beriladi. 
    
    Asosiy mavzular:
    - WDM va OCDMA texnologiyalarining asosiy xususiyatlari
    - Ularning birgalikda ishlash imkoniyatlari
    - Signal integratsiyasi va kanallarni ajratish metodlari
    - Gibrid tizim samaradorligini baholash
    """)

    st.subheader("Gibrid tizim konfiguratsiyasi")
    num_channels = st.slider("Kanallar soni (WDM)", 1, 16, 4)
    num_codes = st.slider("Kodlar soni (OCDMA)", 1, 16, 4)
    
    total_capacity = num_channels * num_codes
    st.write(f"Gibrid tizimning taxminiy maksimal kanallar soni: **{total_capacity}**")

    st.info("Bu laboratoriya amaliy simulyatsiya emas, balki tushunchalar va parametrlarni o‘rganishga mo‘ljallangan.")
