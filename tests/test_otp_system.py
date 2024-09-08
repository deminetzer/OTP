import unittest
from unittest.mock import patch, MagicMock
from app import app, client, totp
from twilio.base.exceptions import TwilioRestException

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('app.client')
    @patch('app.totp')
    def test_index_post_success(self, mock_totp, mock_client):
        # Mock the OTP generation and sending
        mock_totp.now.return_value = '123456'
        mock_client.messages.create.return_value = MagicMock()

        response = self.app.post('/', data={'phone': '+1234567890'})

        # Verify redirect status code
        self.assertEqual(response.status_code, 302)
        
        # Follow the redirect to /verify
        response = self.app.get(response.location)
        self.assertIn(b'Verify OTP', response.data)  # Check for the page content after redirect

    @patch('app.client')
    @patch('app.totp')
    def test_index_post_failure(self, mock_totp, mock_client):
        # Simulate a TwilioRestException
        mock_totp.now.return_value = '123456'
        mock_client.messages.create.side_effect = TwilioRestException('Error', 123)

        response = self.app.post('/', data={'phone': '+1234567890'})

        # Verify that we did not get a redirect and check the error flash message directly
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Error sending OTP:', response.data)

    def test_verify_post_success(self):
        with patch('app.totp.verify') as mock_verify:
            mock_verify.return_value = True

            response = self.app.post('/verify', data={'otp': '123456'})

            # Verify redirect status code
            self.assertEqual(response.status_code, 302)
            
            # Follow the redirect to /success
            response = self.app.get(response.location)
            self.assertIn(b'OTP verification successful!', response.data)

    def test_verify_post_failure(self):
        with patch('app.totp.verify') as mock_verify:
            mock_verify.return_value = False

            response = self.app.post('/verify', data={'otp': 'wrongotp'})

            self.assertEqual(response.status_code, 200)  # Check for successful rendering
            self.assertIn(b'Invalid OTP. Please try again.', response.data)

    def test_success(self):
        response = self.app.get('/success')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'OTP verification successful!', response.data)

if __name__ == '__main__':
    unittest.main()
