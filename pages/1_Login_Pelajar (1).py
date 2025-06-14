# Versi login pelajar stabil tanpa st.experimental_rerun
stable_login_code = """
import streamlit as st
import sqlite3

st.set_page_config(page_title="Log Masuk Pelajar")

def login(no_pelajar, katalaluan):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM pelajar WHERE no_pelajar=? AND katalaluan=?", (no_pelajar, katalaluan))
    user = c.fetchone()
    conn.close()
    return user

def pelajar_interface(nama):
    st.success(f"Selamat datang, {nama}!")
    st.markdown("### 📄 Fungsi untuk pelajar:")
    st.markdown("- 📝 Isi maklumat peribadi")
    st.markdown("- 📤 Muat naik laporan")
    st.markdown("- 📥 Cetak surat penempatan")

# Mula paparan
st.title("🔐 Log Masuk Pelajar")

# Jika dah login, teruskan interface
if "pelajar_login" in st.session_state and st.session_state["pelajar_login"]:
    pelajar_interface(st.session_state["pelajar_nama"])
else:
    no_pelajar = st.text_input("No. Pelajar")
    katalaluan = st.text_input("Kata Laluan", type="password")

    if st.button("Login"):
        user = login(no_pelajar, katalaluan)
        if user:
            st.session_state["pelajar_login"] = True
            st.session_state["pelajar_nama"] = user[3]
            pelajar_interface(user[3])
        else:
            st.error("No. pelajar atau kata laluan salah.")
"""

with open("/mnt/data/1_Login_Pelajar.py", "w") as f:
    f.write(stable_login_code)

"/mnt/data/1_Login_Pelajar.py (versi stabil tanpa rerun) telah disediakan."
