import smtplib

sender = "sender@gmail.com"
receiver = "reciever@gmail.com"
password = "password123"
subject = "Python email test"
body = """
I wrote an email :D

"""

message = f"""From: Snoop Dogg{sender}
To: {receiver}
Subject:{subject}\n
{body}

"""

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

try:
    server.login(sender,password)
    print("Logged in.....")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")

except smtplib.SMTPAuthenticationError:
    print("Unable to sign in")
