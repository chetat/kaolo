import os
from twilio.rest import Client
from app.core.settings import Settings, get_settings
import random

settings: Settings = get_settings()


def get_twilio_client():
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)
    return client


def send_sms(phone_number: str, message: str, client: Client):
    message = client.messages.create(
        body=message, from_="+12543293270", to=phone_number
    )


def generate_otp():
    verification_code = random.randint(100000, 999999)
    return str(verification_code)


def send_otp_sms(phone_number: str, otp: str):
    client = get_twilio_client()
    message = f"Your OTP is {otp}"
    send_sms(phone_number, message, client)
