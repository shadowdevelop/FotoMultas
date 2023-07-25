import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders

class EmailSender:
    def __init__(self,remite,clave,destinatario) -> None:
        self.remite=remite
        self.clave=clave
        self.destinatario=destinatario.split(";")
        self.mensaje=MIMEMultipart()
        
    def set_asunto(self,asunto:str)->None:
        self.mensaje['subject']=asunto
    
    def set_cuerpo(self,cuerpo:str)->None:
        self.mensaje.attach(MIMEText(cuerpo))
        
    def adjuntar_imagen(self,archivo)->None:
        with open(archivo,'rb') as f:
            imagen=MIMEImage(f.read())
            self.mensaje.attach(imagen)
            
    def adjuntar_zip(self,archivo)->None:
        with open(archivo,'rb') as f:
            parte = MIMEBase('application', 'octet-stream')
            parte.set_payload(f.read())
        
        encoders.encode_base64(parte)
        
        parte.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(archivo))
        self.mensaje.attach(parte)
        
    
    # def enviar(self):
    #     try:
    #         servidor=smtplib.SMTP_SSL('mail.bluenet.com.mx',587)
    #         #servidor.starttls()
    #         servidor.login(self.remite,self.clave)
    #         servidor.sendmail(self.remite,self.destinatario,self.mensaje.as_string())
    #         servidor.quit()
    #     except Exception as ex:
    #         print("error enviar correo: " + str(ex))
    
    
    def enviar(self):
        try:
            servidor=smtplib.SMTP('mail.bluenet.com.mx',587)
            #servidor.starttls()
            servidor.ehlo()
            servidor.login(self.remite,self.clave)
            servidor.sendmail(self.remite,self.destinatario,self.mensaje.as_string())
            servidor.quit()
        except Exception as ex:
            print("error enviar correo: " + str(ex))