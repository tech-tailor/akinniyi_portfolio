from flask_mail import Message
from .app import mail
from datetime import datetime
import os
import json


def send_mail(message, recipients, subject):
    """ This sends mail"""

    msg = Message(
        subject=subject,
        recipients=[recipients]
    )
    msg.body = message
    try:
        print('about to send mail')
        mail.connect()
        res = mail.send(msg)
        print('mail sent')
        return res
    except Exception as e:
        print('Error', e)
        res = e
    return res

def save_message(v_msg={}):
    """ Save visitors messages"""
    
    file_path = 'visitor_tmp_msg'
    # Create message path
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    
    message_path = os.path.join(file_path, 'messages.json')

    if os.path.exists(message_path):
        with open(message_path, 'r') as file:
            messages = json.load(file)
    else:
        messages = []
    
    # Get current date time
    d_t = datetime.now()
    print('date-----------------------', d_t)
    v_msg['date'] = d_t.strftime('%d %b, %Y %H:%M:%S')
    # Add new visitor messages
    messages.append(v_msg)

    # Save new messsages to file
    with open(message_path, 'w') as file:
        json.dump(messages, file, indent=4)