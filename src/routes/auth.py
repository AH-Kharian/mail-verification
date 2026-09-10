from flask import request,Blueprint,render_template,jsonify
from src.extensions.db import get_db
from src.utils import generate_verification_token,send_verification_email
from src.config import Config
import hashlib
from google.cloud.firestore_v1.base_query import FieldFilter
from datetime import datetime,timedelta,timezone
from urllib.parse import urlencode

auth_bp=Blueprint('auth_bp',__name__,'')

@auth_bp.route('',methods=['GET'])
def auth():
    token=request.args.get('token')
    token_hash = hashlib.sha256(
        token.encode("utf-8")
    ).hexdigest()

    db = get_db()

    # Find verification record
    query = (
        db.collection("email_verifications")
        .where(filter=FieldFilter("token", "==", token_hash))
        .stream()
    )

    docs = list(query)
    print(token_hash)
    if not docs:
       return render_template(
            "email_verification.html",
            success=False,
            title="Invalid Verification Link",
            message="This verification link is invalid or has already been used."
        ), 400

    verification_doc = docs[0]
    verification = verification_doc.to_dict()

    # Check expiration
    sent_at = verification["sentAt"]
    expires_at = sent_at + timedelta(minutes=30)

    now = datetime.now(timezone.utc)

    if now > expires_at:
        return render_template(
            "email_verification.html",
            success=False,
            title="Verification Link Expired",
            message="This verification link has expired. Please request a new verification email."
        ), 400

    # Get the corresponding application
    email = verification["email"]

    application_query = list(db.collection("partner_applications").where(filter=FieldFilter("email", "==", email)).stream())
    # Mark email as verified
    for applications in application_query:
        applications.reference.update({
        "isVerified": True
    })


    verification_doc.reference.delete()

    return render_template(
        "email_verification.html",
        success=True,
        title="Email Verified!",
        message="Your email address has been successfully verified."
    )

@auth_bp.route('',methods=['POST'])

def verify():
    data=request.get_json()
    db=get_db()
    query=db.collection('partner_applications').where(filter=FieldFilter('email','==',data['email'])).limit(1)
    prev_docs=list(query.stream())
    if not prev_docs:
        token=generate_verification_token()
        send_verification_email(data['email'],(f"{Config.VERIFICATION_BASE_URL}"f"/verify-email?"f"{urlencode({'token': token})}"))
        db.collection('email_verifications').add(
            {
                'email':data['email'],
                'attempt':1,
                'sentAt':datetime.now(timezone.utc),
                'token':hashlib.sha256(token.encode('utf-8')).hexdigest()
            }

        
        )
        return jsonify({'status':'sent','code':501}),200
    else:
        if not prev_docs[0].to_dict()['isVerified']:
            record=db.collection('email_verifications').where(filter=FieldFilter('email','==',data['email'])).limit(1)
            _record=list(record.stream())[0].to_dict()
            if not _record['attempt'] >3 and not datetime.now(timezone.utc) < _record['sentAt']+timedelta(minutes=30):
                token=generate_verification_token()
                send_verification_email(data['email'],(f"{Config.VERIFICATION_BASE_URL}"f"/verify-email?"f"{urlencode({'token': token})}"))
                ref=list(record.stream())[0]
                ref.reference.update({
                    'attempt':_record['attempt']+1,
                    'sentAt':datetime.now(timezone.utc),
                    'token':hashlib.sha256(token.encode('utf-8')).hexdigest()
                })
                return jsonify({
                'status':'linked/sent',
                'code':502
                }),200
            elif datetime.now(timezone.utc) < _record['sentAt']+timedelta(minutes=30):
                return jsonify({'status':'linked/checkmail','code':503})
        else:
            return jsonify({
                'msg':'linked/verified',
                'code':504
            }),200
