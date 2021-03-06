from config import  Config, EmailConfig
from datetime import datetime
from flask_mail import Message
from flask import render_template, current_app
from srcode import create_current_app, mail, app
from threading import Thread


def send_async_email(app, msg):
     '''FUcntionality to send emails asynchronously in the background, accepts both the meessage and the instance of the flask app.
     Giving flask mail a context of our app so that it can access config values'''
     with current_app.app_context():
          mail.send(msg)
def send_confirmation_email(to, template_html, template_body, attachements = None, sync = False, subject = 'Welcome to [Flaskgram].Please Confirm your email'):
     msg = Message(subject=subject, sender = EmailConfig.DEFAULT_MAIL_SENDER, template_html = template_html, template_body = template_body, recipients= [to])   
     if sync:
          mail.send(msg) 
     '''Using a thread class and passing in the apps and msg as the args and start the thread'''
     Thread(target=send_async_email, args = (create_current_app._get_current_object(), msg)).start()  


def send_async_password_reset(app, msg):
     '''FUcntionality to send emails asynchronously in the background, accepts both the meessage and the instance of the flask app.
     Giving flask mail a context of our app so that it can access config values'''
     with current_app.app_context():
          mail.send(msg)


def password_request_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
 
    Thread(target=send_async_password_reset, args=(current_app._get_current_object(), msg)).start() 
    
def send_password_reset_email(user):
     token = user.get_reset_password_token()
     password_request_email('[Flaskgram] Reset Your Password', sender = EmailConfig.DEFAULT_MAIL_SENDER,recipients = [user.email], text_body = render_template('auth/reset_password.txt', user=user, token=token),
     html_body = render_template('auth/reset_password.html', user=user, token=token))
