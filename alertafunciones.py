import os
import sys
import time
import serial
import logging
from mailfunciones import EmailSender
import cv2
import shutil
from reportedb import reportdb

from datetime import datetime,timedelta

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
        
def enviarcorreo(correoat,claveat,destinatario,ipcamara,velocidad,ajustehora,imgprefix,guardarimg,medidavel):    
    try:
        now=datetime.now()
        now=now + timedelta(hours=ajustehora)
        formatted_now=now.strftime("%Y-%m-%d_%H-%M-%S")
        correo=EmailSender(correoat,claveat,destinatario)
        correo.set_asunto("Evidencia de exceso de velocidad")
        imagen=tomarfoto(ipcamara,formatted_now,velocidad,imgprefix,guardarimg,medidavel)
        if imagen !=None:
            correo.adjuntar_imagen(imagen)
        correo.set_cuerpo("Se detecto un exceso de velocidad a las " + str(formatted_now) +  " : " +  f'{velocidad:.2f}' + " KM/H")
        correo.enviar()
        if imagen !=None:
            if (os.path.exists(imagen)):
                os.remove(imagen)
    except:
        print("error monitor")
    
def tomarfoto(ipcamara,fecha,velocidad,prefix,guardarimg,medidavelocidad)->str:
    archivo=None
    try:
        os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS']='rtsp_transport;udp'        
        cap=cv2.VideoCapture(ipcamara,cv2.CAP_FFMPEG)
        if not cap.isOpened():
            return
        
        ret ,frame=cap.read()
        
        if ret:       
            font = cv2.FONT_HERSHEY_SIMPLEX
            
            text= prefix + ' ' + fecha + ' : ' +  f'{velocidad:.2f}' + " " + medidavelocidad
            position = (50,50)
            fontscale=2
            color=(0,0,153)
            thickness=2
            cv2.putText(frame,text,position,font,fontscale,color,thickness)
            archivo= f"{prefix}captured_image_{fecha}.jpg"
            cv2.imwrite(archivo,frame)
            if guardarimg==1:
                cv2.imwrite('./reporte/' + archivo,frame)
                #guardarfoto(archivo,fecha,velocidad)
        cap.release()
    except:
        print("error monitor")
    return archivo
       
def guardarfoto(imagen,fecha,velocidad):    
    shutil.copy(imagen,'./reporte/' + imagen)
    db= reportdb()
    db.insert(fecha,velocidad,imagen)

#enviarmensaje("","")
