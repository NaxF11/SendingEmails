import os
import smtplib
from email.message import EmailMessage

nombre = '' # Tu nombre 
emisor = '' # Tu correo
emails = [] # Lista de correos para enviar
asunto = '' 
clave = ''

# Creamos el mensaje
msg = EmailMessage()
msg['From'] = nombre # Nombre de quién lo está escribiendo
msg['Subject'] = asunto # Asunto del correo
msg.set_content()

# Cargamos los archivos PDFs
files = [''] # Nombre.pdf

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name
        
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
    print(file + '  ha sido subido')
    


# Conectamos con el servidor
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(emisor, clave)
print(emisor,'  sesión iniciada')

# Enviamos los correos
for email in emails:
    msg['To'] = email
    text = msg.as_string()
    server.sendmail(emisor,email,text)
    del msg['To']
    print(email + '  enviado')
    
server.quit()

print("Correos enviados")