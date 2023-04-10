import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

class EmailSender:
    def __init__(self,remite,clave,destinatario) -> None:
        self.remite=remite
        self.clave=clave
        self.destinatario=destinatario
        self.mensaje=MIMEMultipart()
        
    def set_asunto(self,asunto:str)->None:
        self.mensaje['subject']=asunto
    
    def set_cuerpo(self,cuerpo:str)->None:
        self.mensaje.attach(MIMEText(cuerpo))
        
    def adjuntar_imagen(self,archivo)->None:
        with open(archivo,'rb') as f:
            imagen=MIMEImage(f.read())
            self.mensaje.attach(imagen)
    
    def enviar(self):
        try:
            servidor=smtplib.SMTP_SSL('smtp.gmail.com',465)
            #servidor.starttls()
            servidor.login(self.remite,self.clave)
            servidor.sendmail(self.remite,self.destinatario,self.mensaje.as_string())
            servidor.quit()
        except:
            print("error monitor")