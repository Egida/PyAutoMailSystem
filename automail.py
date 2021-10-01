from smptlib import SMTP
from email.message import EmailMessage


# Hi I'm Z3NTL3 and uhm... This only works for your GMAIL shit. 
# Dont forget to allow accessing for LOW SECURE Apps through your gmail, so it accepts this SMTP Connection
# Coded by Z3NTL3

gmail = str("your gmail")
password = str("your gmail pass")
send_to = "target mail"

def mailsystem_through_py_software(smtplib):
    # 587 port is for SSL 
    connect = SMTP('smtp.gmail.com' , 587)
    connect.starttls()
    connect.login(user=gmail, password=password)

    msg = EmailMessage()
    msg['Subject'] = 'Subject Text'
    msg['From'] = 'your gmail'
    msg['To'] = send_to

    

    message = f"""Hi dear consumer,
    
We have seen that you did register on our forum!

We wanted to welcome you from our hearts :)

Kind Regards,
Bla bla duhhh :d
""" # example email text

    msg.set_content(message)    
    connect.send_message(msg)
    
mailsystem_through_py_software()
