import math
import random
import smtplib
from twilio.rest import Client
import Keys

def valid_mobile_no(MobileNo):
    if len(MobileNo) != 10:
        print("Please enter valid Mobile number!")
        MobileNo = input("Enter the number:")
        valid_mobile_no(MobileNo)
    return MobileNo


def Check_Email(Email):
    if "@gmail.com" not in Email:
        print("Please Enter Valid Email address!")
        Email = input("Enter Email:")
        Check_Email(Email)
    return Email



git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global


TargetNo = input("Enter the number:")
Receivers_no = valid_mobile_no(TargetNo)

Email = input("Enter the Email:")
Receivers_email = Check_Email(Email)


OTP = function.Generate_OTP()
function.send_OTP(Receivers_no, OTP)
function.send_email(Receivers_email, OTP)



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
