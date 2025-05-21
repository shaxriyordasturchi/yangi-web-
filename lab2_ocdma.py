import streamlit as
def app ();
st.title("🏗️ Laboratoriya 2: OCDMA Kodlash Tahlili")

# Parametrlar
code_length = st.slider("Kod uzunligi (bitlarda)", min_value=4, max_value=32, value=8)
num_users = st.slider("Foydalanuvchilar soni", min_value=1, max_value=5, value=3)

# Kod generatori (oddiy Pseudo Random Binary Sequence)
def generate_code(length):
    return np.random.choice([0, 1], size=length)

codes = [generate_code(code_length) for _ in range(num_users)]

st.write("### Foydalanuvchilar kodlari:")
for i, code in enumerate(codes, 1):
    st.write(f"Foydalanuvchi {i} kodi:", ''.join(map(str, code)))

# Kodlarni vizual ko‘rsatish
fig, ax = plt.subplots(figsize=(8, num_users))
for i, code in enumerate(codes):
    ax.step(range(code_length), code + i*1.5, where='mid', label=f"User {i+1}")
ax.set_ylim(-0.5, num_users*1.5)
ax.set_xlabel("Bit indeksi")
ax.set_yticks([i*1.5 for i in range(num_users)])
ax.set_yticklabels([f"Foydalanuvchi {i+1}" for i in range(num_users)])
ax.set_title("OCDMA kodlari")
ax.grid(True)
ax.legend()
st.pyplot(fig)

if st.button("Natijalarni PDF ga eksport qilish"):
    from utils import export_pdf
    username = st.session_state.get("username", "Anonim")
    result_data = {
        "Kod uzunligi": code_length,
        "Foydalanuvchilar soni": num_users,
        "Kodlar": ', '.join(''.join(map(str, c)) for c in codes)
    }
    export_pdf(username, result_data)

