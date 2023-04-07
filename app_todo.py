import streamlit as st
import datetime
import time
from todo import TodoDB
# pip install email-validator
from email_validator import validate_email, EmailNotValidError
import re

db = TodoDB()  # TodoDB에서 db라는 이름으로 객체 생성
db.connectToDatabase()



sb = st.sidebar
menu = sb.selectbox('메뉴', ['회원가입', '할 일', '통계'], index=0, key='mnu', help='selectable')

if menu == '회원가입':
    ucol1, ucol2 = st.columns(2)  # 5:5로 나누고 싶을 때 st.columns([5, 5])

    with ucol1:
        st.subheader('회원가입')

    with ucol2:
        st.subheader('회원목록')



elif menu == '할 일':
    st.snow()

elif menu == '통계':
    with st.spinner('Wait for it...'):
        time.sleep(5)
    st.success('Done!')

    st.balloons()