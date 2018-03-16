import smtplib

sender = 'sender_mail@gmail.com'
receivers = 'receiver_mail@gmail.com'
password = 'your password'
message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""



try:
   smtpObj = smtplib.SMTP('smtp.gmail.com:587')
   smtpObj.starttls()
   smtpObj.login(sender,password)

   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except:
    print "Error: unable to send email"
