# python-SMTP-mail
In this tutorial, you will got to know how to send mail using python


steps to follow
1.#import library smtplib in pyhton
  sender = 'sender_mail@gmail.com'
  receivers = 'receiver_mail@gmail.com'

2.#Add sender mail and receiver mail

3.#enter your password and meaasage
  password = 'your password'
  
note : make sure you enable "allow less secure app" in you mail.
If you not, when you run this script Google will ask for it.

4.# set up the SMTP server
smtpObj = smtplib.SMTP('smtp.gmail.com:587')
smtpObj.starttls()

5.#Login to gmail using smpt
smtpObj.login(sender,password)

6.#sending mail
   smtpObj.sendmail(sender, receivers, message) 
