import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="WDM/OCDMA/PON Web Ta'lim Platformasi", layout="wide")

st.sidebar.title("📚 Bo'lim tanlang")
section = st.sidebar.radio("Bo‘limlar", ["Tushuntiruvchi Maqolalar", "Tadqiqot Natijalari", "Virtual Laboratoriya"])

# --- 1. Tushuntiruvchi Maqolalar ---
if section == "Tushuntiruvchi Maqolalar":
    st.title("📖 Tushuntiruvchi Maqolalar")
    
    with st.expander("1️⃣ WDM texnologiyasi nima?"):
        st.markdown("""
        Wavelength Division Multiplexing (WDM) – bu bir nechta optik signalni yagona optik tolada uzatish texnologiyasidir. 
        Har bir signal turli to‘lqin uzunligida uzatiladi, bu esa kanal sig‘imini oshiradi.
        """)
    
    with st.expander("2️⃣ OCDMA prinsipi va afzalliklari"):
        st.markdown("""
        Optical Code Division Multiple Access (OCDMA) – bu foydalanuvchilarni yagona spektrda farqlash uchun kodlardan foydalanadigan metod. 
        Bu texnologiya xavfsizlik, moslashuvchanlik va dinamik uzatishni ta'minlaydi.
        """)
    
    with st.expander("3️⃣ PON (Passive Optical Network) modeli"):
        st.markdown("""
        PON – bu markaziy uzatgichdan (OLT) ko‘plab foydalanuvchilarga (ONT) optik bo‘luvchilar orqali signal yetkazuvchi passiv tarmoq. 
        Bu tizim arzon va energiyaga tejamkor hisoblanadi.
        """)
    
    with st.expander("4️⃣ Gibrid arxitektura"):
        st.markdown("""
        WDM + OCDMA + PON gibrid arxitekturasi yuqori sig‘imli, xavfsiz va masshtablanuvchi optik tarmoqni tashkil etadi. 
        Bu yondashuv o‘quvchilarga zamonaviy tarmoq dizaynini o‘rganishga imkon beradi.
        """)

# --- 2. Tadqiqot Natijalari ---
elif section == "Tadqiqot Natijalari":
    st.title("📊 Tadqiqot Natijalari")

    st.markdown("WDM, OCDMA, va PON texnologiyalarining samaradorligini solishtirish:")

    data = pd.DataFrame({
        "Texnologiya": ["WDM", "OCDMA", "PON", "Gibrid"],
        "Sig'im (Gbps)": [40, 20, 10, 60],
        "Kechaqish (ms)": [10, 5, 3, 8],
        "Xavfsizlik darajasi (1-5)": [3, 5, 2, 5]
    })

    st.dataframe(data.set_index("Texnologiya"))

    st.subheader("Sig'im va kechikish grafigi")
    fig, ax = plt.subplots()
    ax.bar(data["Texnologiya"], data["Sig'im (Gbps)"], color='skyblue', label="Sig'im")
    ax.set_ylabel("Gbps")
    ax.set_title("Texnologiyalar bo'yicha Sig'im taqqoslash")
    st.pyplot(fig)

# --- 3. Virtual Laboratoriya ---
elif section == "Virtual Laboratoriya":
    st.title("🧪 Virtual Laboratoriya: Signalni Simulyatsiya Qiling")

    st.markdown("Quyidagi parametrlarni tanlab, chiqish trafik sig‘imini hisoblang.")

    wdm_kanallar = st.slider("🔹 WDM kanallar soni", 1, 8, 4)
    signal_soni = st.slider("🔹 Har kanalga signal soni", 1, 4, 2)
    ocdma_effektiv = st.slider("🔹 OCDMA samaradorligi (foizda)", 10, 100, 80)

    total_signal = wdm_kanallar * signal_soni
    kanal_sigimi = 10  # har bir kanal uchun (Gbps)
    umumiy_sigim = total_signal * kanal_sigimi * (ocdma_effektiv / 100)

    st.success(f"🔧 Umumiy chiqish sig‘imi: **{umumiy_sigim:.2f} Gbps**")

    st.markdown("""
    Ushbu laboratoriya mashg‘uloti orqali siz:
    - Har xil WDM/OCDMA parametrlari orqali chiqish sig‘imini hisoblay olasiz.
    - Raqamli natijalarni real vaqt rejimida o‘zgartirish imkoniyatiga egasiz.
    """)

# --- Oxiri ---
st.sidebar.markdown("---")
st.sidebar.info("📌 Ushbu platforma ta'lim va ilmiy maqsadlar uchun mo‘ljallangan.")
