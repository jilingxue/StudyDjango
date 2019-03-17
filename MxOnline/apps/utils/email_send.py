from users.models import EmailVerifyRecord
from django.core.mail import send_mail
from MxOnline.settings import EMAIL_FORM

def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    code = 'abcdef'
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = '注册激活链接'
        email_body = '点击链接激活http://127.0.0.1/8000'
        email_status = send_mail(email_title, email_body, EMAIL_FORM, [email])
        if email_status:
            pass

