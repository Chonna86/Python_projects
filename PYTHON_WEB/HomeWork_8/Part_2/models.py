from mongoengine import Document, StringField, BooleanField

class Contact(Document):
    full_name = StringField(required=True)
    email = StringField(required=True)
    phone_number = StringField(required=True)
    preferred_channel = StringField(choices=['email', 'sms'], required=True, default='email')
    message_sent = BooleanField(default=False)