#!/bin/usr/python3
""" The main view for the portfolio app"""
from portfolio.utils import send_mail, save_message


from flask import Blueprint, render_template, request, redirect, flash

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=["GET", "POST"])
def index():
    """ The home view for the portfolio app"""

    if request.method == 'POST':
        # Get the form details
        
        form_data = request.form
        name = form_data.get('u_name')
        email = form_data.get('email')
        message = form_data.get('message')

        # Save the message to a json file
        try:
            v_msg = {
                'name': name,
                'email': email,
                'message': message
            }
            save_message(v_msg)
        except Exception as e:
            print('Error', e)
            flash('An error occured, please try again', 'danger')
            return redirect('/')

        # Send mail to the admin
        subject = 'New message from portfolio'
        message = f'Name: {name}\nEmail: {email}\nMessage: {message}'
        recipients = 'ogundareakinniyi247@gmail.com'

        send_mail(message, recipients, subject)
        
        

        flash('form submitted succesfully', 'success')
        return render_template('main/index.html', email=form_data, name=name)
    else:
        return render_template('main/index.html')