import sqlite3
import hashlib
from fpdf import FPDF  # PDF yaratish uchun kutubxona

def create_user_table():
    """Foydalanuvchilar jadvalini yaratadi (agar mavjud bo'lmasa)."""
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS userstable (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_user(username, password):
    """
    Yangi foydalanuvchini qo'shadi.
    Parol oldin hash qilingan bo'lishi kerak.
    Agar foydalanuvchi allaqachon mavjud bo'lsa, False qaytaradi.
    """
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    try:
        c.execute('INSERT INTO userstable(username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        # username allaqachon mavjud
        return False
    finally:
        conn.close()

def login_user(username, password):
    """
    Foydalanuvchini tekshiradi (username va hash qilingan password bo'yicha).
    Agar topilsa, user malumotlarini qaytaradi, aks holda None.
    """
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute('SELECT * FROM userstable WHERE username = ? AND password = ?', (username, password))
    data = c.fetchone()
    conn.close()
    return data

def hash_password(password):
    """
    Parolni sha256 hash qiladi va hex formatda qaytaradi.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def export_pdf(title, content, filename="lab_report.pdf"):
    """
    Matnli kontentni PDF faylga saqlaydi.
    title - PDFning sarlavhasi
    content - matn (string)
    filename - saqlanadigan fayl nomi (default: lab_report.pdf)
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt=title, ln=True, align='C')
    pdf.ln(10)

    pdf.set_font("Arial", size=12)
    for line in content.split('\n'):
        pdf.multi_cell(0, 10, line)

    pdf.output(filename)
    return filename
