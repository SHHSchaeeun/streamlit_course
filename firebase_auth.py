import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyCiXUCgnYhiJYs15tAECoWf3XIXJtv2OaQ",
    'authDomain': "streamlit-shhschaeeun.firebaseapp.com",
    'projectId': "streamlit-shhschaeeun",
    'storageBucket': "streamlit-shhschaeeun.appspot.com",
    'messagingSenderId': "106404196016",
    'appId': "1:106404196016:web:687b7a7e7b73ecb2521575",
    'databaseURL': "https://streamlit-shhschaeeun-default-rtdb.firebaseio.com/"}

firebase = pyrebase.initialize_app(firebaseConfig)  # 위 정보를 이용해서 firebase에 접근할 수 있는 객체 생성
auth = firebase.auth()  # 여러 기능 중 auth를 사용할게

auth.create_user_with_email_and_password('uncon2756@gmail.com', 'kimchaeeun')
auth.send_email_verification()

isLogged = False

try:

    login = auth.sign_in_with_email_and_password('uncon2756@gmail.com', 'kimchaeeun')
    # print(login)  # 딕셔너리
    # print(login['idToken'])
    user = auth.get_account_info(login['idToken'])
    # print(user['users'][0]['localId'])
    print(user)

    isLogged = True

except Exception as e:
    print(e)

if isLogged == True:
    print('로그인 성공!!!')
    # 로그인 했을 때 스트림릿 코드
else:
    print('로그인 실패...')
    # 로그인하쎄용 이라고 출력