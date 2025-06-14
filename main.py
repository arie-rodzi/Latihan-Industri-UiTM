import streamlit as st

st.set_page_config(page_title="Sistem Latihan Industri", layout="wide")

st.title("Selamat Datang ke Sistem Latihan Industri")
st.markdown("---")

st.markdown("## 👤 Sila Pilih Kategori Pengguna")

col1, col2 = st.columns(2)

with col1:
    st.page_link("pages/login_pelajar.py", label="Log Masuk Pelajar 👨‍🎓", icon="🎓")

    st.page_link("pages/login_penyelia_akademik.py", label="Log Masuk Penyelia Akademik 📘", icon="🧑‍🏫")

with col2:
    st.page_link("pages/login_penyelia_industri.py", label="Log Masuk Penyelia Industri 🏭", icon="👷")

    st.page_link("pages/login_penyelaras.py", label="Log Masuk Penyelaras ⚙️", icon="🗂️")

st.markdown("---")
st.info("Sila log masuk mengikut peranan anda untuk mengakses modul berkaitan.")

