import firebase_admin
from firebase_admin import credentials, firestore

# Automatically uses application default credentials in Cloud Run
if not firebase_admin._apps:
    firebase_admin.initialize_app()

db = firestore.client()
