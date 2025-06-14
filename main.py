# Generate corrected main.py content for Streamlit structure (no import, just redirection via page_link)

main_py_corrected = """
import streamlit as st

st.set_page_config(page_title="Sistem Latihan Industri", layout="wide")

st.title("📚 Selamat Datang ke Sistem Latihan Industri UiTM")
st.markdown("Sila pilih peranan anda untuk log masuk ke sistem.")

role = st.selectbox("Pilih Peranan Anda", ["-", "Pelajar", "Penyelaras", "Penyelia Akademik", "Penyelia Industri"])

if role != "-":
    st.subheader(f"Log Masuk untuk {role}")
    if role == "Pelajar":
        st.page_link("pages/login_pelajar.py", label="➡ Terus ke Log Masuk Pelajar")
    elif role == "Penyelaras":
        st.page_link("pages/login_penyelaras.py", label="➡ Terus ke Log Masuk Penyelaras")
    elif role == "Penyelia Akademik":
        st.page_link("pages/login_penyelia_akademik.py", label="➡ Terus ke Log Masuk Penyelia Akademik")
    elif role == "Penyelia Industri":
        st.page_link("pages/login_penyelia_industri.py", label="➡ Terus ke Log Masuk Penyelia Industri")
"""

# Save the corrected main.py file
main_path = "/mnt/data/main.py"
with open(main_path, "w") as f:
    f.write(main_py_corrected)

main_path
