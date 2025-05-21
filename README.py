import streamlit as st
import sqlite3
import pandas as pd
import hashlib
from datetime import datetime

# --- Ma'lumotlar bazasi ulanish ---
conn = sqlite3.connect('lab_app.db', check_same_thread=False)
c = conn.cursor()

# --- Foydalanuvchilar jadvali ---
c.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    age INTEGER,
    role TEXT
)''')

# --- Natijalar jadvali ---
c.execute('''CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    task_name TEXT,
    signal_count INTEGER,
    result_text TEXT,
    date TEXT
)''')
conn.commit()

# --- Parolni shifrlash ---
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# --- Foydalanuvchini qo'shish ---
def add_user(username, password, age, role):
    hashed_pw = hash_password(password)
    try:
        c.execute("INSERT INTO users (username, password, age, role) VALUES (?, ?, ?, ?)",
                  (username, hashed_pw, age, role))
        conn.commit()
        return True
    except:
        return False

# --- Foydalanuvchini tekshirish ---
def check_user(username, password):
    hashed_pw = hash_password(password)
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_pw))
    return c.fetchone()

# --- Natijani saqlash ---
def save_result(user_id, task_name, signal_count, result_text):
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c.execute("INSERT INTO results (user_id, task_name, signal_count, result_text, date) VALUES (?, ?, ?, ?, ?)",
              (user_id, task_name, signal_count, result_text, date))
    conn.commit()

# --- PDF eksporti ---
def export_to_csv():
    df = pd.read_sql_query("SELECT users.username, users.age, results.task_name, results.signal_count, results.result_text, results.date FROM results JOIN users ON results.user_id = users.id", conn)
    df.to_csv("lab_results_export.csv", index=False)
    return "lab_results_export.csv"

# --- Kirish sahifasi ---
def login_section():
    st.subheader("🔐 Kirish")
    username = st.text_input("Foydalanuvchi nomi")
    password = st.text_input("Parol", type='password')
    if st.button("Kirish"):
        user = check_user(username, password)
        if user:
            st.session_state.user = user
            st.success(f"Xush kelibsiz, {user[1]}!")
        else:
            st.error("Login yoki parol xato")

# --- Ro'yxatdan o'tish ---
def register_section():
    st.subheader("📝 Ro‘yxatdan o‘tish")
    username = st.text_input("Foydalanuvchi nomi")
    password = st.text_input("Parol", type='password')
    age = st.number_input("Yosh", min_value=10, max_value=100)
    role = st.radio("Rolni tanlang", ["talaba", "admin"])
    if st.button("Ro‘yxatdan o‘tish"):
        success = add_user(username, password, age, role)
        if success:
            st.success("Ro‘yxatdan o‘tildi! Endi kirish mumkin.")
        else:
            st.error("Foydalanuvchi mavjud")

# --- 1-laboratoriya ---
def lab_task_1(user_id):
    st.subheader("🔬 Laboratoriya 1: WDM signal qo‘shish")
    signal_count = st.slider("Nechta signal qo‘shiladi?", 1, 8, 3)
    if st.button("Natijani tahlil qilish"):
        result = f"WDM tizimida {signal_count} ta signal birlashtirildi. Chiqishda spektral ajratish bajariladi."
        st.success(result)
        save_result(user_id, "WDM Signal Qo‘shish", signal_count, result)

# --- 2-laboratoriya ---
def lab_task_2(user_id):
    st.subheader("🔬 Laboratoriya 2: OCDMA yuklanishni baholash")
    users = st.slider("Foydalanuvchi soni", 1, 50, 10)
    effective_load = round(users * 0.25, 2)
    result = f"OCDMA orqali {users} ta foydalanuvchi uzatmoqda. Umumiy yuk: {effective_load} Gbps."
    if st.button("Yukni hisobla"):
        st.success(result)
        save_result(user_id, "OCDMA Yuklanma Baholash", users, result)

# --- Admin paneli ---
def admin_panel():
    st.subheader("🛠️ Admin Panel")
    df = pd.read_sql_query("SELECT users.username, users.age, results.task_name, results.signal_count, results.result_text, results.date FROM results JOIN users ON results.user_id = users.id", conn)
    st.dataframe(df)
    if st.button("📥 Natijalarni CSV ko‘chirib olish"):
        path = export_to_csv()
        st.success("CSV fayl yaratildi")
        with open(path, "rb") as f:
            st.download_button("Yuklab olish", f, file_name="lab_results.csv")

# --- Asosiy ilova ---
def main():
    st.title("🔬 WDM/OCDMA/PON – Virtual Laboratoriya")
    if "user" not in st.session_state:
        login_tab, register_tab = st.tabs(["Kirish", "Ro‘yxatdan o‘tish"])
        with login_tab:
            login_section()
        with register_tab:
            register_section()
    else:
        user = st.session_state.user
        st.sidebar.write(f"👤 {user[1]} ({user[4]})")
        if user[4] == "admin":
            admin_panel()
        else:
            task = st.radio("Laboratoriya topshirig‘ini tanlang", ["1 - WDM", "2 - OCDMA"])
            if "1" in task:
                lab_task_1(user[0])
            else:
                lab_task_2(user[0])
            if st.button("Chiqish"):
                st.session_state.clear()
                st.experimental_rerun()

if __name__ == '__main__':
    main()
