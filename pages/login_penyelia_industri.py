import streamlit as st

st.title("🔐 Login")

with st.form("login_form"):
    nama = st.text_input("Nama")
    kata_laluan = st.text_input("Kata Laluan", type="password")
    submitted = st.form_submit_button("Login")
    if submitted:
        if nama and kata_laluan:
            st.session_state["penyelia_industri"] = ("id", "nama")
            st.success("Login berjaya!")
            st.rerun()
        else:
            st.warning("Sila masukkan nama dan kata laluan.")
