## This program uses a SMTP client session object that can be used to send mail to any internet machine with an SMTP or ESMTP listener daemon. 

import smtplib
## Subclass of MIMEBase, this is an intermediate base class for MIME messages that are multipart.
from email.mime.multipart import MIMEMultipart
## MIMEText is a module and class that is used to create MIME objects of major type text.
from email.mime.text import MIMEText

## Add the sender and receiver information here. 
email_addr = 'sender-email95@gmail.com'
pswrd = 'sdffjoa rreggdsn jtih sgddfkgssss' #This address was given by Gmail app password feature
recipient = 'dest-email@gmail.com'

## Setup the email information and the message
message = MIMEMultipart()
message['From'] = email_addr
message['To'] = recipient
message['Subject'] =  'Escribi esto con Python'
body = 'Estoy automatizando mi correo de Gmail usando Python. Traeme helados de la Pops a la vuelta, plis'
message.attach(MIMEText(body,'plain'))

## Server setup
smtp_server = smtplib.SMTP('smtp.gmail.com', 587) ## encapsulates an SMTP connection
smtp_server.starttls()
smtp_server.login(email_addr,pswrd)

## Send the email and close the server connection
smtp_server.sendmail(email_addr,recipient,message.as_string())
smtp_server.quit()
print('Email sent')
