# OTP System

## Overview

This is a simple One-Time Password (OTP) system built using Python and Flask. The application allows users to request an OTP via SMS and then verify it. It uses Twilio for sending SMS messages and PyOTP for generating OTPs.

## Features

- Request an OTP via SMS.
- Verify the OTP entered by the user.
- Simple web interface built with Flask.
- Unit tests for ensuring application functionality.

## Prerequisites

- Python 3.6 or higher
- A Twilio account for SMS functionality
- Flask, PyOTP, and Twilio libraries

## Setup

### 1. Install Python and Required Libraries

Ensure you have Python installed on your machine. Install the required libraries using pip:

```bash
pip install flask pyotp twilio
```

### 2. Set Up Environment Variables
Create a .env file in the root directory of the project and add the following environment variables:

- FLASK_SECRET_KEY=your_secret_key
- TWILIO_ACCOUNT_SID=your_twilio_account_sid
- TWILIO_AUTH_TOKEN=your_twilio_auth_token
- TWILIO_PHONE_NUMBER=your_twilio_phone_number

### 3. Run the Application
Start the Flask application:

```bash
python app.py
```

### 4. Access the Application
Open your browser and go to http://localhost:5000.

### 5. Using the Application
* Enter your phone number in the provided field (e.g., +9725XXXXXXXX).
* Request an OTP, which will be sent to the provided phone number.
* Enter the received OTP to verify it.

## Running Tests
To ensure everything is working correctly, run the unit tests:

```bash
python -m unittest discover -s tests
```

## How It Works
* The user enters their phone number.
* An OTP is generated and sent to the provided phone number via SMS.
* The user enters the received OTP to verify it.

## License
This project is licensed under the MIT License.
