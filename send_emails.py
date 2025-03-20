import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email_addr = 'jddelgado95@gmail.com'
pswrd = 'sjoa rren jtih sgkg' #This address was given by Gmail app password feature
recipient = 'valealfaro@gmail.com'

message = MIMEMultipart()
message['From'] = email_addr
message['To'] = recipient
message['Subject'] =  'Escribi esto con Python'
body = 'Estoy automtizando mi correo de Gmail usando Python. Traeme helados de la Pops a la vuelta, plis'
message.attach(MIMEText(body,'plain'))

smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_server.starttls()
smtp_server.login(email_addr,pswrd)

smtp_server.sendmail(email_addr,recipient,message.as_string())
smtp_server.quit()
print('Email sent')
