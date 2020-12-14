# Django
from django.test import TestCase

# Utitlities
import json


# Create your tests here.
class MailTests(TestCase):
    base_url = '/api/mailer/send/mail/'

    def setUp(self):
        self.valid_name = 'Edgar Gómez'
        self.valid_email = 'edgar@mail.com'
        self.valid_subject = 'Job proposal from KaabIT'
        self.valid_message = 'Hey I saw your page and work, and I loved it!.\n\nWanna word with you and looking forward to talk.\nSend me an email.\n\nRegards'

        self.invalid_name = 'Joe'
        self.invalid_subject = ''
        self.invalid_email = 'fake_email.com'
        self.invalid_message = 'Hi there!'

    def test_mail_post_request(self):
        successful_response = self.client.post(
            self.base_url,
            data={
                "name": self.valid_name,
                "email": self.valid_email,
                "subject": self.valid_subject,
                "message": self.valid_message
            }
        )
        json_response = json.loads(successful_response.content)
        self.assertEqual(successful_response.status_code, 200)
        self.assertEqual(json_response['success'], True)
        self.assertEqual(json_response['message'], 'Message sent successfully')

        unsuccessful_response = self.client.post(
            self.base_url,
            data={
                "name": self.invalid_name,
                "email": self.invalid_email,
                "subject": self.invalid_subject,
                "message": self.invalid_message
            }
        )
        json_response = json.loads(unsuccessful_response.content)
        self.assertEqual(unsuccessful_response.status_code, 400)
        self.assertEqual(json_response['success'], False)
        self.assertEqual(json_response['message'], 'Invalid data')
