# OTP System

## Overview

This is a simple One-Time Password (OTP) system built using Python and Flask. The application allows users to request an OTP via SMS and then verify it. It uses Twilio for sending SMS messages and PyOTP for generating OTPs.

## Features

- Request an OTP via SMS.
- Verify the OTP entered by the user.
- Simple web interface built with Flask.

## Prerequisites

- Python 3.6 or higher
- A Twilio account for SMS functionality

## Setup

### 1. Install Python and Required Libraries

Ensure you have Python installed on your machine. Install the required libraries using pip:

```bash
pip install flask pyotp twilio
```

### 2. Run the application:
    ```bash
    python app.py
    ```

### 3. Access the application at http://localhost:5000.

### 4. Enter you phone number, +9725XXXXXXXX

## How It Works

- The user enters their phone number.
- An OTP is generated and sent to the provided phone number via SMS.
- The user enters the received OTP to verify it.

## License

This project is licensed under the MIT License.