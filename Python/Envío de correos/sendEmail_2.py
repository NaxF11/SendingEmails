import sendEmailCopy
# hjrprboviagfuqzy

# Todo en String
mi_nombre = 'Pablo Vidal'
mi_correo = 'pvidal@kastpinochet.cl'
clave = 'power16653569-7kaizen'
destinatarios = ['clanchile@hotmail.com','carlosruiz06@gmail.com','info@rematesferreira.cl','csalgadol@tgr.cl','clarinanunez@hotmail.es','claudio.soto@casc.cl','receptoraelisavargas@hotmail.com','receptor_emilioretamal@hotmail.com','sobarzoeugenia@gmail.com','fherreria1@hotmail.com','felipe.fontecilla@hotmail.com','grivano@gmail.com','gvera.receptor@gmail.com','hernan.leiva@cde.cl','hvergara.receptor@gmail.com','lucia_zavala@hotmail.com','of.receptor.mora@gmail.com','jorgereceptor@yahoo.es','jorge.concha@outlook.es','jose_receptor@live.cl','jfaundezs@gmail.com','receptoramariameza@gmail.com','marcelo.reyes@cde.cl','receptorgallardo@gmail.com','ale_laramar@gmail.com','nancy.pacheco@hotmail.com','rebecareceptorjudicial@gmail.com','sandrabaltierra@hotmail.com','receptor.guzman@gmail.com','villa.magna@hotmail.com','menard.atias@gmail.com','klepe@receptorsanmiguel.cl'] # String
#destinatarios =['ignacio.contreras.v1@gmail.com']
asunto = 'Lunes, 09 de mayo de 2022 9:30 SAICH con SANDOVAL MGM 21º Juzgado Civil de Santiago AUDIENCIA TESTIMONIAL C-3102-2018 Manuel Gutiérrez'
mensaje = 'Estimado/a\nJunto con saludar y esperando que se encuentre bien le escribo para saber si es posible\n 1. Citar los testigos Sres:\n1.1 PABLO SEBASTIAN GARCIA REYES, trabajador dependiente, N° de C.I. 14.179.487-6, domiciliado en Jaime Guzmán Errazuriz 3295, Ñuñoa.\n1.2. CLAUDIO OSVALDO CORDOVA HERNANDEZ, ingeniero civil metalúrgico, N° de C.I. 14.207.629-2, domiciliado en Januario Espinoza 7345, La Reina.\n1.3. CLAUDIO ANDRES HEUFEMANN ULLOA, ingeniero civil industrial, N° de C.I. 15.183.120-6, domiciliado en Marchant Pereira 1085, depto. 902. Providencia.\n1.4. MARCELO EDUARDO PÉREZ GARCÍA, ingeniero civil metalúrgico, N° de C.I. 15.492.767-0, domiciliado en Padre Mariano 128, depto. 404. Providencia.\n\n2. Tomar la audiencia testimonial el día 09 de mayo de 2022 a las 09:30 horas, fijada por resolución de fecha 20 de abril del año 2022 en el juicio de la referencia.\n\nEn atención a la reforma al art. 391 del Código Orgánico de Tribunales y en atención a la proximidad de la audiencia y en atención a que, lo más probable, es que la totalidad de los receptores de Santiago no tengan disponibilidad\n\nMuchas gracias\nSaludos cordiales'
adjunto = [] # String

try:
    sendEmailCopy.enviarCorreo(mi_nombre,mi_correo,clave,destinatarios,asunto,mensaje,adjunto)    
except:
    print('\nNo se pudo completar la operación')
    
    