import streamlit as st

with st.sidebar:
    st.title('제목입니다')
    st.input01 = st.text_input('DB주소를 입력하세요.')
    st.input02 = st.text_input('DB아이디를 입력하세요.')
    st.input03 = st.text_input('DB패스워드를 입력하세요.')

    st.button01 = st.button('DB에 접속하기')