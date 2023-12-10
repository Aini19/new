import streamlit as st
# SILAHKAN DI GANTI 2

st.set_page_config(
    page_title="Organizational Experience|aini",
    page_icon="👨‍🎓",
    layout="wide"
)

st.title("Pengalaman Organisasi")
st.write("Organisasi Yang Saya Ikuti: ")

st.container()
col1, = st.columns(1)
with col1:
    st.subheader("Ikatan Santri Intra Madrasah (ISIM)")
   

st.container()
st.write("---")
col1, = st.columns(1)
with col1:
   
    st.image("th.jpg", width= 190)

st.container()
st.write("---")
col1, = st.columns(1)
with col1:
    st.write("*Anggota Departemen Pendidikan*")
   