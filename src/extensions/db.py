from firebase_admin import credentials,firestore
from google.cloud.firestore_v1.base_query import FieldFilter
from src.config import Config
import firebase_admin
import hashlib
from datetime import datetime,timezone,timedelta
from src.utils import send_verification_email,generate_verification_token
from urllib.parse import urlencode




def init_db():
    if not firebase_admin._apps:
        cred=credentials.Certificate(Config.FIREBASE_ACCOUNT_KEY)
        firebase_admin.initialize_app(cred)

def get_db():
    return firestore.client()
