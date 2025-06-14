# Simpan versi yang betul untuk 1_Login_Pelajar.py dengan interface selepas login

final_login_code = """
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

# UI login hanya jika belum login
if "pelajar" not in st.session_state:
    st.title("🔐 Log Masuk Pelajar")

    no_pelajar = st.text_input("No. Pelajar")
    katalaluan = st.text_input("Kata Laluan", type="password")

    if st.button("Login"):
        user = login(no_pelajar, katalaluan)
        if user:
            st.session_state["pelajar"] = user[3]  # Simpan nama pelajar
            st.experimental_rerun()
        else:
            st.error("No. pelajar atau kata laluan salah.")
else:
    pelajar_interface(st.session_state["pelajar"])
"""

with open("/mnt/data/1_Login_Pelajar.py", "w") as f:
    f.write(final_login_code)

"/mnt/data/1_Login_Pelajar.py telah dikemaskini dan sedia untuk dimuat turun."
