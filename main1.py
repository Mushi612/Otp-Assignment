from twilio.rest import Client
import smtplib
import random

account_sid="AC83269abe6b5473c7879cfa96bd9e2d3c"
auth_token="35dccfab0fcc6644e371ec283df6b6ef"

twilio_number='+14705162775'
phone_number='+919665015802'

client= Client(account_sid, auth_token)
otp = ''.join([str(random.randint(0,9))for i in range(6)])
SMS=client.messages.create(
    body="Your OTP is "+otp,
    from_=twilio_number,
    to=phone_number
)
print(SMS.body)



server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('ommhatre2003@gmail.com','cjtzttnalqeaughf')
SMS='your otp is '+str(otp)
server.sendmail('ommhatre2003@gmail.com','ryuzakil841@gmail.com',SMS)
server.quit()