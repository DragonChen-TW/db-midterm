from flask import current_app, render_template, g
from flask_mail import Mail, Message
from threading import Thread

# @current_app.app_context
def send_mail(msg_title, msg_sender, msg_receiver, msg_content, **kwargs):
    msg = Message(msg_title, sender=msg_sender, recipients=msg_receiver)
    msg.body = msg_content
    msg.html = render_template('mail_template.html', **kwargs)

    send_out(current_app, msg)

def send_out(app, msg):
    with app.app_context():
        mail = Mail(app)
        mail.send(msg)