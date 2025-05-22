import streamlit as st

# URL query parametrlarini o‘qish (YANGILANGAN USUL)
params = st.query_params
lab = params.get("lab", "lab1")  # default 'lab1'

# Sarlavha
st.title("🔬 WDM/OCDMA PON laboratoriyalar")

# Parametrga qarab kontentni ko‘rsatish
if lab == "lab1":
    from lab1_wdm import run_lab1
    run_lab1()

elif lab == "lab2":
    from lab2_ocdma import run_lab2
    run_lab2()

elif lab == "lab3":
    from lab3_pon import run_lab3
    run_lab3()

elif lab == "lab4":
    from lab4_hybrid import run_lab4
    run_lab4()

elif lab == "lab5":
    from lab5_error_correction import run_lab5
    run_lab5()

else:
    st.error("❌ Noto‘g‘ri laboratoriya tanlandi.")


