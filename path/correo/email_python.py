from email.message import EmailMessage
import ssl
import smtplib
import imghdr

email_emisor = 'jeo2k1@gmail.com'
email_password = 'yawlgporlzvlaigz'
email_receptor = 'jeo20@hotmail.com'

asunto = 'Mail desde Python'
cuerpo = """
    Correo de prueba desde Script Python
"""
em = EmailMessage()
em['FROM'] = email_emisor
em['TO'] = email_receptor
em['SUBJECT'] = asunto
em.set_content(cuerpo)

#Adjuntar imagen
with open('bookshelf-at-dunster-house-library.jpg','rb') as file:
    file_data = file.read()
    file_tipo = imghdr.what(file.name)
    file_nombre = file.name
em.add_attachment(file_data, filename=file_nombre,subtype=file_tipo, maintype='image')

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_emisor, email_password)
    smtp.sendmail(email_emisor, email_receptor, em.as_string())