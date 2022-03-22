from cgitb import text
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "testeroboudemy@gmail.com"
toaddr = "testeroboudemy@gmail.com, tavinho1502@gmail.com"

msg = MIMEMultipart()

msg['from'] = fromaddr

msg['to'] = toaddr

msg['Subject'] = "Email de teste"

body = "Email enviado pelo robô"

msg.attach(MIMEText(body, 'plain'))

filename='Doc1.pdf'
anexo= open("C:\Apps\Robo email\Doc1.pdf", "rb")

p = MIMEBase('application', 'octet-stream')

p.set_payload((anexo).read())
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename )
msg.attach(p)

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login(fromaddr, 'tavinho1502')

text = msg.as_string()

s.sendmail(fromaddr, toaddr, text)

s.quit()