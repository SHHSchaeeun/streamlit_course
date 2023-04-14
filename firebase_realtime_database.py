import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyCiXUCgnYhiJYs15tAECoWf3XIXJtv2OaQ",
    'authDomain': "streamlit-shhschaeeun.firebaseapp.com",
    'projectId': "streamlit-shhschaeeun",
    'storageBucket': "streamlit-shhschaeeun.appspot.com",
    'messagingSenderId': "106404196016",
    'appId': "1:106404196016:web:687b7a7e7b73ecb2521575",
    'databaseURL': "https://streamlit-shhschaeeun-default-rtdb.firebaseio.com/"}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

#Push Data
data = {"김채은": {
    "name": '김채은',
    "age": 19,
    "address": '대구 북구'
}}

# print(db.push(data))

db.child("users").set(data)