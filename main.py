# Updated main.py structure with professional sidebar navigation by user role

import streamlit as st
import os
import hashlib

# Role-based imports (assuming all relevant login files exist in pages directory)
from pages.login_pelajar import pelajar_interface
from pages.login_penyelaras import penyelaras_interface
from pages.login_penyelia_akademik import penyelia_akademik_interface
from pages.login_penyelia_industri import penyelia_industri_interface


# Dummy credentials (replace with real verification or database lookup)
user_db = {
    "pelajar": {"2021123456": "passpelajar"},
    "penyelaras": {"admin001": "adminpass"},
    "penyelia_akademik": {"akademik01": "akademikpass"},
    "penyelia_industri": {"industri01": "industripass"}
}

st.set_page_config(page_title="Sistem Latihan Industri", layout="wide")

# Session init
if "role" not in st.session_state:
    st.session_state.role = None
if "username" not in st.session_state:
    st.session_state.username = ""

def login_page():
    st.title("Selamat Datang ke Sistem Latihan Industri")

    role = st.selectbox("Pilih Peranan Anda", ["-", "pelajar", "penyelaras", "penyelia_akademik", "penyelia_industri"])
    if role != "-":
        username = st.text_input("ID Pengguna")
        password = st.text_input("Kata Laluan", type="password")
        if st.button("Log Masuk"):
            if username in user_db.get(role, {}) and user_db[role][username] == password:
                st.session_state.role = role
                st.session_state.username = username
                st.success(f"Log masuk berjaya sebagai {role}")
                st.experimental_rerun()
            else:
                st.error("ID Pengguna atau Kata Laluan salah!")

def main_interface():
    role = st.session_state.role
    username = st.session_state.username

    with st.sidebar:
        st.write(f"🔐 Anda masuk sebagai: **{role.upper()}**")
        st.write(f"👤 ID: {username}")
        if st.button("Log Keluar"):
            st.session_state.role = None
            st.session_state.username = ""
            st.experimental_rerun()

    if role == "pelajar":
        pelajar_interface(username)
    elif role == "penyelaras":
        penyelaras_interface(username)
    elif role == "penyelia_akademik":
        penyelia_akademik_interface(username)
    elif role == "penyelia_industri":
        penyelia_industri_interface(username)

# Run the app
if st.session_state.role is None:
    login_page()
else:
    main_interface()
