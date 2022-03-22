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

html = """
<html>

    <body>

        <p>Oi,<br>
        Como vai você?<br>
        <a href="https://www.udemy.com/course/criando-robos-em-python/learn/lecture/16808876#questions">Video Aulas Gratuitas</a>
        Muitas aulas pra assistir.
        </p>
        
    </body>

</html>
"""
part1 = MIMEText(html, "html")

msg.attach(part1)



s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login(fromaddr, 'tavinho1502')

text = msg.as_string()

s.sendmail(fromaddr, toaddr, text)

s.quit()