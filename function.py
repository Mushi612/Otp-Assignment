import math
import random
import smtplib
from twilio.rest import Client
import Keys


def send_email(Receivers_email, otp):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('ommhatre2003@gmail.com','jhrrlkhwesiwadmw')
    SMS='your otp is '+str(otp)
    server.sendmail('ommhatre2003@gmail.com',Receivers_email,SMS)
    server.quit()

def Generate_OTP():
    otp = ''.join([str(random.randint(0,9))for i in range(6)])

    return otp


def send_OTP(Receivers_no, OTP):
    client = Client(Keys.account_sid, Keys.auth_token)
    Message = client.messages.create(
        body="Your 6 digit OTP is "+OTP,

        from_=Keys.twilio_number,
        to='+91'+(Receivers_no),
    )
    print(Message.body)
