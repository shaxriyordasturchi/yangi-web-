import streamlit as st

def app():
    st.title("Lab 5 - Tarmoqlarda Xatolikni Tahlil va Tuzatish")
    st.write("""
    Ushbu laboratoriyada optik tarmoqlarda yuzaga keladigan xatoliklarni aniqlash va ularni tuzatish usullari 
    o‘rganiladi.
    
    Asosiy mavzular:
    - Optik signal uzatishda yuzaga keladigan xatoliklar turlari
    - Error detection va correction kodlari (masalan, Hamming kodi)
    - Xatoliklarni aniqlash algoritmlari
    - Signal sifatini baholash usullari
    """)

    st.subheader("Hamming kodi bilan xatolikni tuzatish (oddiy misol)")

    st.write("3 bitli ma'lumotga 1 bitli parity qo‘shiladi (Hamming(7,4) kodi asosida)")

    data_bits = st.text_input("Ma'lumot bitlari (4 ta 0 yoki 1 raqami)", "1011")

    if len(data_bits) == 4 and all(bit in '01' for bit in data_bits):
        # Oddiy parity bit qo'shish (bu haqiqiy Hamming emas, ammo misol uchun)
        parity_bit = str(data_bits.count('1') % 2)
        codeword = data_bits + parity_bit
        st.write(f"Kodni so‘z (data + parity): {codeword}")

        st.write("Agar kodda bittagina xatolik yuzaga kelsa, u aniqlanib, tuzatilishi mumkin.")
    else:
        st.warning("Iltimos, faqat 4 ta 0 yoki 1 raqamidan iborat bitlarni kiriting.")
