from smptlib import SMTP
from email.message import EmailMessage


# Hi I'm Z3NTL3 and uhm... This only works for your GMAIL shit. 
# Dont forget to allow accessing for LOW SECURE Apps through your gmail, so it accepts this SMTP Connection
# Coded by Z3NTL3

gmail = str("your gmail")
password = str("your gmail pass")
send_to = "target mail"
subject = "Subject Tex
yourmessage = """
Hi dear consumer,
    
We have seen that you did register on our forum!

We wanted to welcome you from our hearts :)

Kind Regards,
Bla bla duhhh :d
""" # example yourmessage string text
def mailsystem_through_py_software(smtplib):
    # 587 port is for SSL 
    connect = SMTP('smtp.gmail.com' , 587)
    connect.starttls()
    connect.login(user=gmail, password=password)

    raw = EmailMessage()
    raw['Subject'] = subject
    raw['From'] = gmail
    raw['To'] = send_to

    

    message = f"""{yourmessage}""" 

    raw.set_content(message)    
    connect.send_message(raw)
    
mailsystem_through_py_software()
