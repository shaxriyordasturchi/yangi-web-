import streamlit as st

st.set_page_config(page_title="WDM/OCDMA PON Tushunchalari", layout="wide")

# --- Sahifa tanlov ---
section = st.selectbox("🌍 Qaysi bo'limni ko'rmoqchisiz?", [
    "WDM texnologiyasi",
    "OCDMA prinsipi",
    "PON modeli",
    "Gibrid arxitektura"
])

# --- Bo'lim 1: WDM ---
if section == "WDM texnologiyasi":
    st.header("🚀 WDM (Wavelength Division Multiplexing) texnologiyasi")
    st.markdown("""
    WDM — bu bir nechta optik signalni turli to'lqin uzunliklarida (ranglarda) bitta optik tolada uzatish imkonini beruvchi texnologiya.
    
    **Afzalliklari:**
    - O'tkazuvchanlikni oshiradi
    - Tarmoq resurslaridan samarali foydalanadi
    - Har bir signal mustaqil kanalga ega
    """)
    st.image("images/wdm_diagram.png", caption="WDM signal ajratilishi", use_column_width=True)
    st.video("videos/wdm_explainer.mp4")

# --- Bo'lim 2: OCDMA ---
elif section == "OCDMA prinsipi":
    st.header("🌐 OCDMA (Optical Code Division Multiple Access)")
    st.markdown("""
    OCDMA — foydalanuvchilarning ma'lumotlarini noyob kodlar orqali bitta kanalga joylashtirish imkonini beradi.

    **Afzalliklari:**
    - Yuqori xavfsizlik
    - Mustaqil kanalga ehtiyoj yo'q
    - Past kechikish va yuqori samaradorlik
    """)
    st.image("images/ocdma_diagram.png", caption="OCDMA kodlash jarayoni")
    st.video("videos/ocdma_explainer.mp4")

# --- Bo'lim 3: PON ---
elif section == "PON modeli":
    st.header("📡 PON (Passive Optical Network) modeli")
    st.markdown("""
    PON — passiv optik tarmoq bo‘lib, markaziy OLT dan foydalanuvchilargacha signalni kuchsizlantirmasdan yetkazadi.

    **Afzalliklari:**
    - Kam quvvat sarfi (passiv elementlar)
    - Masshtablash oson
    - Narxi nisbatan past
    """)
    st.image("images/pon_model.png", caption="PON arxitekturasi")
    st.video("videos/pon_overview.mp4")

# --- Bo'lim 4: Gibrid arxitektura ---
elif section == "Gibrid arxitektura":
    st.header("🧰 WDM/OCDMA asosidagi PON gibrid arxitekturasi")
    st.markdown("""
    Gibrid arxitekturasi orqali WDM yordamida fizik kanallar bo‘linadi va har bir kanalda OCDMA orqali foydalanuvchilar kodlar bilan farqlanadi.

    **Afzalliklari:**
    - Yuqori o'tkazuvchanlik
    - Kengaytirilgan xavfsizlik
    - Katta miqyosdagi foydalanuvchi qo‘llab-quvvatlovi
    """)
    st.image("images/hybrid_architecture.png", caption="WDM + OCDMA gibrid modeli")
    st.video("videos/hybrid_demo.mp4")
