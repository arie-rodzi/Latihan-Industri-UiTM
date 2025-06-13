import streamlit as st

st.set_page_config(page_title="Sistem Latihan Industri", layout="wide")

with st.sidebar:
    st.markdown("## 👨‍🎓 Pelajar")
    st.page_link("auth/login_pelajar.py", label="🔑 Login Pelajar")
    if "pelajar" in st.session_state:
        st.page_link("pages/2_BLI_01_Isian.py", label="BLI 01 Isian")
        st.page_link("pages/3_Upload_BLI_02.py", label="Upload BLI 02")
        st.page_link("pages/4_Logbook.py", label="Logbook")
        st.page_link("pages/5_Upload_Laporan_Akhir.py", label="Upload Laporan Akhir")

    st.markdown("## 🧑‍🏫 Penyelia Akademik")
    st.page_link("auth/login_penyelia_akademik.py", label="🔑 Login Penyelia Akademik")
    if "penyelia_akademik" in st.session_state or "penyelaras" in st.session_state:
        st.page_link("pages/9_BLI_08_Akademik.py", label="BLI 08 Akademik")

    st.markdown("## 🧑‍🔧 Penyelia Industri")
    st.page_link("auth/login_penyelia_industri.py", label="🔑 Login Penyelia Industri")
    if "penyelia_industri" in st.session_state or "penyelaras" in st.session_state:
        st.page_link("pages/8_BLI_05_Industri.py", label="BLI 05 Industri")

    st.markdown("## 👨‍💼 Penyelaras")
    st.page_link("auth/login_penyelaras.py", label="🔑 Login Penyelaras")
    if "penyelaras" in st.session_state:
        st.page_link("pages/6_Semakan_Supervisor.py", label="Semakan Supervisor")
        st.page_link("pages/7_Admin_Panel.py", label="Panel Penyelaras")
        st.page_link("pages/10_Export_Keputusan.py", label="Export Keputusan")

st.title("📚 Selamat Datang ke Sistem Latihan Industri UiTM")
st.write("Sila login mengikut peranan anda untuk akses fungsi sistem.")
