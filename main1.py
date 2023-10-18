import math
import random
import smtplib
from twilio.rest import Client



account_sid="AC83269abe6b5473c7879cfa96bd9e2d3c"
auth_token="35dccfab0fcc6644e371ec283df6b6ef"

twilio_number='+14705162775'
# phone_number='+919665015802'

def validate_mobile_no(MobileNo):
    if len(MobileNo) != 10:
        print("Please enter valid Mobile number!")
        MobileNo = input("Enter the number:")
        validate_mobile_no(MobileNo)
    return MobileNo



def validate_Email(Email):
    if "@gmail.com" not in Email:
        print("Please Enter Valid Email address!")
        Email = input("Enter Email:")
        validate_Email(Email)
    return Email


def send_email(Receivers_email, otp):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('ommhatre2003@gmail.com','cjtzttnalqeaughf')
    SMS='your otp is '+str(otp)
    server.sendmail('ommhatre2003@gmail.com',Receivers_email,SMS)
    server.quit()

def Generate_OTP():
    otp = ''.join([str(random.randint(0,9))for i in range(6)])

    return otp


def send_OTP(Receivers_no, OTP):
    client = Client(account_sid, auth_token)
    Message = client.messages.create(
        body="Your 6 digit OTP is "+OTP,

        from_=twilio_number,
        to='+91'+str(Receivers_no),
    )
    print(Message.body)






TargetNo = input("Enter the number:")
Receivers_no = validate_mobile_no(TargetNo)

Email = input("Enter the Email:")
Receivers_email = validate_Email(Email)


OTP = Generate_OTP()
send_OTP(Receivers_no, OTP)
send_email(Receivers_email, OTP)




