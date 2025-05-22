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
elif lab == "lab6":
    st.header("Laboratoriya 6 – Spektral Samaradorlik Analizi")
    st.write("WDM tizimlarida kanal soni oshgani sari spektral samaradorlik qanday o'zgarishini ko'rsatadi.")
elif lab == "lab7":
    st.header("Laboratoriya 7 – OCDMA Kodingi va Interferensiya")
    st.write("OCDMA kod uzunligi va foydalanuvchi soni asosida interferensiya tahlili.")
elif lab == "lab8":
    st.header("Laboratoriya 8 – PON Delay Tahlili")
    st.write("PON tarmog‘ida masofa va foydalanuvchi soni asosida kechikish (delay) aniqlanadi.")
elif lab == "lab9":
    st.header("Laboratoriya 9 – Hybrid Tarmoqda Faol Foydalanuvchilar Yuki")
    st.write("WDM-OCDMA-PON tarmoqlarida bir vaqtning o‘zida faol foydalanuvchilar soni bilan yuklanish tahlili.")
elif lab == "lab10":
    st.header("Laboratoriya 10 – BER tahlili barcha texnologiyalarda")
    st.write("WDM, OCDMA, PON va ularning gibridlarida BER (Bit Error Rate) taqqoslanadi.")
else:
    st.write("Noto‘g‘ri laboratoriya tanlandi.")
