from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

from ...settings.environments import SMTP_SERVER_CRED_PASSWORD, SMTP_SERVER_CRED_EMAIL


class SMTP:
    def sendMail(to: str, subject: str, message: str):
        # message object instance
        msg = MIMEMultipart()
        # setup the parameters of the message
        msg['From'] = SMTP_SERVER_CRED_EMAIL
        msg['To'] = to
        msg['Subject'] = subject
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # create server
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()

        # login credentials for sending the mail
        server.login(msg['From'], SMTP_SERVER_CRED_PASSWORD)

        # send the message via the server
        server.sendmail(msg['From'], msg['To'], msg.as_string())

        server.quit()
