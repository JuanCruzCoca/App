import smtplib, ssl

def send_email(user_message):
    host = "smtp.gmail.com"
    port = 465


    username = "juancruzcoca16@gmail.com"
    password = "yncy qyzv kmwr ieto"

    receiver = "juancruzcoca16@gmail.com"
    context = ssl.create_default_context()

    message = """
Subject: Test Email
This is a test email sent from Python!
""" 

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, user_message)


