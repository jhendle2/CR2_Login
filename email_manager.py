import smtplib, ssl

port = 465  # For SSL
password = "plantasia2cr2&a"
sender_email = "cr2emailer@gmail.com"
receiver_email = "td@whrwfm.org"

# Create a secure SSL context
context = ssl.create_default_context()


def send_login_email(engineer, time):
    email = "Subject: CR2 Login - %s\n\n%s logged into CR2 at %s" % (engineer, engineer, time)
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, email)
    print("! Sent login email to %s" % receiver_email)
