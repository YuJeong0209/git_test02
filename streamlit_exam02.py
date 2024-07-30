import streamlit as st

with st.sidebar:
    st.title('ID')
    db_address = st.text_input('DB주소를 입력하세요')
    db_id = st.text_input('DB아이디를 입력하세요.')
    db_pw = st.text_input('DB패스워드를 입력하세요.')
    db_button_input = st.button('DB에 접속하기')