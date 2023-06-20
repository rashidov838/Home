import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

message=MIMEMultipart("alternative")
message['Subject']='multipart test'
message['From']=os.environ.get("salimrashidov09@gmail.com")
message['To']="bekzodrashidov0110@gmail.com"
sender_email=os.environ.get("salimrashidov09@gmail.com")
reciever_email="bekzodrashidov0110@gmail.com"
password=os.environ.get("bekzodr1973")

text = """\
    Hi, 
    How are you?
    Real Pythin has many great tutorials: 
    www.realpython.com"""
html = """\
    <html>
        <body>
            <p> Hi, <br>
                How are you?<br>
                <a href = "http://www.realpython.com">Real Python fourth time</a>
                has many great tutorials.
            </p>
        </body>
    </html>
    """

part1=MIMEText(text,'plain')
part2=MIMEText(html,'html')



message.attach(part1)
message.attach(part2)


context=ssl.create_default_context()
print("Sending email")
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
    server.login(sender_email,password)
    server.sendmail(
        sender_email,reciever_email,message.as_string()

    )
    print("Email was sent")