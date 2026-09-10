import os,json
from dotenv import load_dotenv

load_dotenv()

class Config:
    FIREBASE_ACCOUNT_KEY=json.loads(os.getenv('FIREBASE_ACCOUNT_KEY'))
    RESEND_API_KEY=os.getenv('RESEND_API_KEY')
    VERIFICATION_BASE_URL = "http://10.154.0.11:8000"