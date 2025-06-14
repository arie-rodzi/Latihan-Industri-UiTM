
import streamlit as st
import sqlite3

def login(no_pelajar, katalaluan):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM pelajar WHERE no_pelajar=? AND katalaluan=?", (no_pelajar, katalaluan))
    user = c.fetchone()
    conn.close()
    return user

def pelajar_interface(nama):
    st.success(f"Selamat datang, {nama}!")
    st.info("Modul pelajar sedang dimuatkan...")
    # Tambah fungsi lain di sini

st.set_page_config(page_title="Log Masuk Pelajar")

st.title("🔐 Log Masuk Pelajar")

no_pelajar = st.text_input("No. Pelajar")
katalaluan = st.text_input("Kata Laluan", type="password")

if st.button("Log Masuk"):
    user = login(no_pelajar, katalaluan)
    if user:
        st.session_state["pelajar"] = user[3]  # Nama
        pelajar_interface(user[3])
    else:
        st.error("No. pelajar atau kata laluan salah.")
