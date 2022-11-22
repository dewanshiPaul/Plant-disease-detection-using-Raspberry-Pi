import smtplib
from email.message import EmailMessage
import time

def email_alert_disease(subject, body, to, image_data, image_name, subtype):
    message = EmailMessage()
    message.set_content(body)
    message['subject'] = subject
    message['to'] = to

    user = '' #set
    password = '' #set

    message['from'] = user
    #attach image
    message.add_attachment(image_data, maintype='image', subtype=subtype, filename=image_name)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls() #tls used for preventing bounce backs
    server.login(user, password)
    server.send_message(message)

    server.quit()

def email_alert_temp_humid(subject, body, to):
    message = EmailMessage()
    message.set_content(body)
    message['subject'] = subject
    message['to'] = to

    user = 'dewanshipaul84@gmail.com'
    password = 'gmztqaleblfyuuhj'

    message['from'] = user

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls() #tls used for preventing bounce backs
    server.login(user, password)
    server.send_message(message)

    server.quit()