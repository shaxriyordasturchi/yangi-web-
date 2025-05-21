import streamlit as st
import sqlite3

def app():

# CSS uslublari
st.markdown("""
    <style>
    .main {
        background-color: #f0f8ff;
        color: #003366;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .header {
        background: linear-gradient(90deg, #4A90E2 0%, #50E3C2 100%);
        padding: 20px;
        border-radius: 8px;
        color: white;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        box-shadow: 0 4px 6px rgba(74, 144, 226, 0.3);
        margin-bottom: 20px;
    }
    .section {
        background-color: white;
        border-radius: 8px;
        padding: 15px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .table-header {
        background-color: #50E3C2;
        color: white;
        font-weight: 600;
        text-align: center;
        padding: 10px 5px;
    }
    table {
        width: 100%;
        border-collapse: collapse;
    }
    td {
        padding: 8px;
        text-align: center;
        border-bottom: 1px solid #ccc;
    }
    </style>
""", unsafe_allow_html=True)

# Foydalanuvchilarni olish funksiyasi
def get_users():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT username, name, age FROM userstable")
    data = c.fetchall()
    conn.close()
    return data

st.markdown('<div class="header">🛠️ Admin Panel - Foydalanuvchilar Boshqaruvi</div>', unsafe_allow_html=True)

users = get_users()

st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("Foydalanuvchilar ro‘yxati")

if users:
    st.markdown("""
    <table>
        <thead>
            <tr>
                <th class="table-header">Login</th>
                <th class="table-header">Ism</th>
                <th class="table-header">Yosh</th>
            </tr>
        </thead>
        <tbody>
    """, unsafe_allow_html=True)

    for user in users:
        st.markdown(f"""
            <tr>
                <td>{user[0]}</td>
                <td>{user[1]}</td>
                <td>{user[2]}</td>
            </tr>
        """, unsafe_allow_html=True)

    st.markdown("</tbody></table>", unsafe_allow_html=True)
else:
    st.info("Hech qanday foydalanuvchi topilmadi.")

st.markdown('</div>', unsafe_allow_html=True)

# Laboratoriya natijalari bo‘limi (namuna)
st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("Laboratoriya Natijalari (Namuna)")

sample_results = {
    "Foydalanuvchi": "user123",
    "Laboratoriya": "WDM Kanal Simulyatsiyasi",
    "Natija": "Yaxshi",
    "Sana": "2025-05-21"
}

for k, v in sample_results.items():
    st.markdown(f"**{k}:** {v}")

st.markdown('</div>', unsafe_allow_html=True)
