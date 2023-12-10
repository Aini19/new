import streamlit as st



st.set_page_config(
    page_title="Portfolio | Aini",
    page_icon="👨‍🎓",
    layout="wide"
)

st.title("SELAMAT DATANG DI PORTFOLIO SAYA")

st.sidebar.success("SILAHKAN PILIH MENU DI ATAS")

import streamlit as st

col1, col2 = st.columns(2)

with col1:
   st.header("About Me")
   st.image("aini.jpg", width= 390)

with col2:
   st.header("My Biodata")
   st.subheader("NAMA : Nur Ma'rifatillah Aini")
   st.caption("NIM : 0402201089")
   st.write(
            """
            - Tempat Tanggal Lahir : Brebes, 19 Juli 2001
            - Alamat               : Sengon-Tanjung-Breres
            - Hobi                 : Njajan, ngemil, tidur, baca buku
            - Cita-cita            : Jadi Santri yang bermanfaat dan Qowiyyun Amin
            - Hal yang disukai     : Dapet amanah dari Guru dan Ortu
            - Status               : Jomblo bahagia
            """
        )
st.header("*Aini Ma'rifah 19*")