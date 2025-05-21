import sqlite3
import hashlib
from fpdf import FPDF
import streamlit as st

DB_NAME = "users.db"

def create_user_table():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS userstable(
            username TEXT PRIMARY KEY,
            password TEXT,
            name TEXT,
            age INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def add_user(username, password, name, age):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        c.execute('INSERT INTO userstable(username, password, name, age) VALUES (?, ?, ?, ?)',
                  (username, password, name, age))
        conn.commit()
    except sqlite3.IntegrityError:
        st.error("Bu foydalanuvchi nomi allaqachon mavjud!")
    conn.close()

def login_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT * FROM userstable WHERE username = ? AND password = ?', (username, password))
    data = c.fetchone()
    conn.close()
    return data

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def export_pdf(username, result_data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Laboratoriya Natijalari", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Foydalanuvchi: {username}", ln=True)
    pdf.ln(10)
    for k, v in result_data.items():
        pdf.cell(200, 10, txt=f"{k}: {v}", ln=True)
    pdf.output("lab_report.pdf")
    st.success("✅ PDF fayl yaratildi: lab_report.pdf")
