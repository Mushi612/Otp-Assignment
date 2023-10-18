from twilio.rest import Client
import math
import smtplib
import random
import re

account_sid="AC83269abe6b5473c7879cfa96bd9e2d3c"
auth_token="35dccfab0fcc6644e371ec283df6b6ef"

twilio_number='+14705162775'
# phone_number='+919665015802'

def validate_mobile_no(Mobile_no):
    return len(Mobile_no) == 10 and Mobile_no.isdigit()


def validate_email(email):
    validating_condition = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.search(validating_condition, email):
        return True
    else:
        return False


def generate_otp():
    otp = ''.join([str(random.randint(0,9))for i in range(6)])

    return otp


def send_email(email, otp):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls() 
    server.login('ommhatre2003@gmail.com', 'cjtzttnalqeaughf')
    message = 'Your 6 digit OTP is '+str(otp)
    server.sendmail('ommhatre2003@gmail.com', email, message)
    server.quit()


def send_otp_through_sms(mobile_no, otp):
    client = Client(account_sid, auth_token)
    Message = client.messages.create(
        body="Your 6 digit OTP is "+otp,
        from_=twilio_number,
        to='+91'+str(mobile_no),
    )
    print(Message.body)


if __name__ == "__main__":

    otp = generate_otp()
    mobile_no = input("Enter the Mobile number:")
    if (validate_mobile_no(mobile_no)):
        send_otp_through_sms(mobile_no, otp)
    else:
        print("Invalid Mobile no")

    email = input("Enter the Email:")
    if (validate_email(email)):
        send_email(email, otp)
    else:
        print("Invalid Email ")