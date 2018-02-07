import smtplib


email_user = ''
email_receiver = ''
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_user,'password')

i=0
while i<100:
    message = "Test message"

    server.sendmail(email_user,email_receiver,message)
    i+=1

server.quit()
