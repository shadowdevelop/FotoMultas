import os
import sys
import time
import serial
import logging
from mailfunciones import EmailSender
import cv2
import datetime

def enviarmensaje(mensaje):
    try:
        serial_mensaje = serial.Serial() 
        serial_mensaje = serial.Serial(
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1,
            writeTimeout=2
        )

        serial_mensaje.port = "/dev/ttyUSB0"  # good for linux
        serial_mensaje.open()
        serial_mensaje.flushInput()
        serial_mensaje.flushOutput()

        serial_mensaje.write(str.encode(mensaje))
    except:
        print("error monitor")
        
def enviarcorreo(correoat,claveat,destinatario,ipcamara,velocidad):    
    now=datetime.datetime.now()
    formatted_now=now.strftime("%Y-%m-%d_%H-%M-%S")
    correo=EmailSender(correoat,claveat,destinatario)
    correo.set_asunto("Evidencia de exceso de velocidad")
    imagen=tomarfoto(ipcamara,formatted_now)
    if imagen !=None:
        correo.adjuntar_imagen(imagen)
    correo.set_cuerpo("Se detecto un exceso de velocidad a las {formatted_now}")
    correo.enviar()
    if imagen !=None:
        if (os.path.exists(imagen)):
            os.remove(imagen)
    
def tomarfoto(ipcamara,fecha)->str:
    os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS']='rtsp_transport;udp'
    archivo=None
    cap=cv2.VideoCapture(ipcamara,cv2.CAP_FFMPEG)
    if not cap.isOpened():
        return
    
    ret ,frame=cap.read()
    
    if ret:       
        archivo= f"captured_image_{fecha}.jpg"
        cv2.imwrite(archivo,frame)
        
    cap.release()
    
    return archivo
       
    


#enviarmensaje("","")
