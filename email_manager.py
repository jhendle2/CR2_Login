import smtplib, ssl
import login

port = 465  # For SSL
# password
# sender_email = "cr2emailer@gmail.com"
# td_email = "td@whrwfm.org"
# prod_email = "production@whrwfm.org"

# Create a secure SSL context
context = ssl.create_default_context()


def send_login_email(engineer, time):
    email = "Subject: CR2 Login - %s\n\n%s logged into CR2 at %s" % (engineer, engineer, time)
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, td_email, email)
    print("! Sent login email to %s" % td_email)


def send_error_email(error, time):
    email = "Subject: CR2 Problem - %s\n\n%s" % (time, error)
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, td_email, email)
        # server.sendmail(sender_email, prod_email, email)
    print("! Problem reported to %s" % td_email)
    # print("! Problem reported to %s" % prod_email)