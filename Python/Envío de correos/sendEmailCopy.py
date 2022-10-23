import os
import smtplib
from email.message import EmailMessage

# nombre = '' # Tu nombre 
# emisor = '' # Tu correo
# clave = ''
# emails = [] # Lista de correos para enviar
# asunto = '' 
# mensaje = ''

def enviarCorreo(nombre,emisor,clave,emails,asunto,mensaje,adjunto):
    # Creamos el mensaje
    msg = EmailMessage()
    msg['From'] = nombre # Nombre de quién lo está escribiendo
    msg['Subject'] = asunto # Asunto del correo
    msg.set_content(mensaje) # Mensaje

    # Cargamos los archivos PDFs
    if adjunto:
        files = adjunto # Nombre.pdf

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

    return("Correos enviados")