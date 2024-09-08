from flask import Flask, render_template, request, redirect, url_for, flash
import pyotp
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get sensitive values from environment variables
app.secret_key = os.getenv('FLASK_SECRET_KEY')  # Set the secret key for session management and flash messages
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_phone_number = os.getenv('TWILIO_PHONE_NUMBER')

client = Client(account_sid, auth_token)
totp = pyotp.TOTP(pyotp.random_base32())

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        phone_number = request.form['phone']
        otp = totp.now()

        try:
            message = client.messages.create(
                body=f'Your OTP code is {otp}',
                from_=twilio_phone_number,
                to=phone_number
            )
            flash('OTP sent successfully!')
            return redirect(url_for('verify'))
        except TwilioRestException as e:
            # Check for specific error codes or messages
            if 'unverified' in str(e):
                flash('Error sending OTP: The phone number is unverified. Please verify the number in your Twilio account.')
            else:
                flash(f'Error sending OTP: {e}')
        except Exception as e:
            flash(f'An unexpected error occurred: {e}')
    
    return render_template('index.html')

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        user_otp = request.form['otp']
        if totp.verify(user_otp):
            flash('OTP verified successfully!')
            return redirect(url_for('success'))
        else:
            flash('Invalid OTP. Please try again.')

    return render_template('verify.html')

@app.route('/success')
def success():
    return 'OTP verification successful!'

if __name__ == '__main__':
    app.run(debug=True)
