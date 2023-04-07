import streamlit as st
import datetime
from todo import TodoDB
# pip install email-validator
from email_validator import validate_email, EmailNotValidError
import re

db = TodoDB()  # TodoDB에서 db라는 이름으로 객체 생성
db.connectToDatabase()

sb = st.sidebar
menu = sb.selectbox('메뉴', ['회원가입', '할 일', '통계'], index=1)