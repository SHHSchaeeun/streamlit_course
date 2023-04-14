import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Setup
cred = credentials.Certificate("serviceAccount.json")
firebase_admin.initialize_app(cred)

"""
db = firestore.client()
docs = db.collection('users').get()  # 이 위치에서 이하 데이터를 불러옴
for doc in docs:  # for문을 통해 아래 데이터를 불러옴
    print(doc.to_dict())
# 뽀독인돇
"""

db = firestore.client()

docs = db.collection('users').where('name', '==', 'chaeeun').stream()  # 이 위치에서 이하 데이터를 불러옴
for doc in docs:  # for문을 통해 아래 데이터를 불러옴
    print(doc.to_dict())