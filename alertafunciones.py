import os
import sys
import time
import zipfile
import serial
import logging
from mailfunciones import EmailSender
import cv2
import shutil
from reportedb import reportdb

from datetime import datetime,timedelta

def enviarcorreoerror(correoat,claveat,destinatario,error,logger):
    try:
        
        correo=EmailSender(correoat,claveat,destinatario)
        correo.set_asunto("Error de sensor de velocidad")
        
        
        correo.set_cuerpo("Se detecto un problema con el sensor : " + error)
        correo.enviar()      
    except Exception as ex:
        logger.error("enviarcorreoerror : " + str(ex))        
        

def enviarmensaje(mensaje,logger):
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
        logger.error("Monitor no encontrado")
        print("error monitor")
        
def enviarcorreo(correoat,claveat,destinatario,ipcamara,velocidad,ajustehora,imgprefix,guardarimg,medidavel,logger):    
    try:
        now=datetime.now()
        now=now + timedelta(hours=ajustehora)
        formatted_now=now.strftime("%Y-%m-%d_%H-%M-%S")
        correo=EmailSender(correoat,claveat,destinatario)
        correo.set_asunto("Evidencia de exceso de velocidad")
        imagen=tomarfoto(ipcamara,formatted_now,velocidad,imgprefix,guardarimg,medidavel,logger)
        if imagen !=None:
            correo.adjuntar_zip(imagen)
        correo.set_cuerpo("Se detecto un exceso de velocidad a las " + str(formatted_now) +  " : " +  f'{velocidad:.2f}' + " KM/H")
        correo.enviar()
        if imagen !=None:
            if (os.path.exists(imagen)):
                os.remove(imagen)
    except Exception as ex:
        logger.error("enviarcorreo : " + str(ex))   
        print("error monitor")
    
def tomarfoto(ipcamara,fecha,velocidad,equipo,guardarimg,medidavelocidad,logger)->str:
    archivo=None
    try:
        os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS']='rtsp_transport;udp'        
        cap=cv2.VideoCapture(ipcamara,cv2.CAP_FFMPEG)
        if not cap.isOpened():
            return
        
        ret ,frame=cap.read()
        
        if ret:       
            font = cv2.FONT_HERSHEY_SIMPLEX
            
            text= equipo + ' ' + fecha + ' : ' +  f'{velocidad:.2f}' + " " + medidavelocidad
            position = (50,100)
            fontscale=2
            color=(255,255,255)
            thickness=3
            cv2.putText(frame,text,position,font,fontscale,color,thickness)
            archivo= f"{equipo}_captured_image_{fecha}.jpg"
            cv2.imwrite(archivo,frame,[cv2.IMWRITE_JPEG_QUALITY, 40])
            zip_image(archivo, 'imagen.zip')
            if (os.path.exists(archivo)):
                os.remove(archivo)
            archivo='imagen.zip'            
            if guardarimg=="1":
                archivo2= f"{equipo}_{fecha}.jpg"
                cv2.imwrite('./reporte/' + archivo2,frame)
                try:
                    db=reportdb()
                    db.insert(velocidad,archivo2,equipo)
                except:
                    pass
                #guardarfoto(archivo,fecha,velocidad)
        cap.release()
    except Exception as ex:
        logger.error("tomarfoto : " + str(ex)) 
        print("error monitor")
    return archivo

def zip_image(image_path, zip_path):
    # Crear un nuevo archivo zip en zip_path
    with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as myzip:
        # Agregar image_path al archivo zip
        myzip.write(image_path)



       
def guardarfoto(imagen,fecha,velocidad):    
    shutil.copy(imagen,'./reporte/' + imagen)
    db= reportdb()
    db.insert(fecha,velocidad,imagen)

#enviarmensaje("","")
