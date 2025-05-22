import streamlit as st

# 6–10 laboratoriyalarni import qilish
from lab6_spektr import run_lab6
from lab7_ocdma import run_lab7
from lab8_pon_delay import run_lab8
from lab9_hybrid_load import run_lab9
from lab10_ber_comparison import run_lab10

# URL query parametrlarini o‘qish
params = st.experimental_get_query_params()
lab = params.get("lab", ["lab1"])[0]  # default lab1

# Sarlavha
st.title("🔬 WDM/OCDMA PON laboratoriyalar")

# Parametrga qarab kontentni ko‘rsatish
if lab == "lab1":
    st.header("Laboratoriya 1 - WDM texnologiyasi")
    st.write("Bu yerda WDM texnologiyasi bo‘yicha laboratoriya vazifalari joylashgan.")

elif lab == "lab2":
    st.header("Laboratoriya 2 - OCDMA texnologiyasi")
    st.write("Bu yerda OCDMA texnologiyasi bo‘yicha laboratoriya vazifalari joylashgan.")

elif lab == "lab3":
    st.header("Laboratoriya 3 - PON texnologiyasi")
    st.write("Bu yerda PON texnologiyasi bo‘yicha laboratoriya vazifalari joylashgan.")

elif lab == "lab4":
    st.header("Laboratoriya 4 - Hybrid sistemalar")
    st.write("Bu yerda Hybrid WDM/OCDMA/PON tizimlari bo‘yicha laboratoriya vazifalari.")

elif lab == "lab5":
    st.header("Laboratoriya 5 - Tizim monitoringi va tahlil")
    st.write("Bu yerda tizim monitoringi va tahlil bo‘yicha laboratoriya vazifalari.")

elif lab == "lab6":
    run_lab6()

elif lab == "lab7":
    run_lab7()

elif lab == "lab8":
    run_lab8()

elif lab == "lab9":
    run_lab9()

elif lab == "lab10":
    run_lab10()

else:
    st.error("❌ Noto‘g‘ri laboratoriya tanlandi.")
