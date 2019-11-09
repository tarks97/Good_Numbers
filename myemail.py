import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders




def send_numbers(numbers):

    smtp_server = 'smtp.gmail.com'
    port = 587
    sender_mail = 'numbersgood1@gmail.com'
    password = "goodgooD1"
    reciever_mail = 'Rrkk@outlook.dk'
    

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()        
        server.starttls(context=context)
        server.ehlo()
        print("proslo1")
        server.login(sender_mail, password)

        server.sendmail(sender_mail, reciever_mail, numbers)
    except Exception as e:
        print(e)
    finally:
        server.close()

