import streamlit as st

# URL query parametrlarini o‘qish
params = st.experimental_get_query_params()
lab = params.get("lab", ["lab1"])[0]  # default lab1

# Sarlavha
st.title("WDM/OCDMA PON laboratoriyalar")

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
else:
    st.write("Noto‘g‘ri laboratoriya tanlandi.")
