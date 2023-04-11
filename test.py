import sys
os = sys.platform
print("Current OS: ", os)

# import requests
# from datetime import datetime

# def capture_image_from_ip_camera(url, username, password, output_file):
#     # Realiza una solicitud HTTP para obtener la imagen de la cámara IP
#     response = requests.get(url, auth=(username, password))

#     # Verifica si la respuesta fue exitosa
#     if response.status_code == 200:
#         # Guarda la imagen en un archivo
#         with open(output_file, 'wb') as f:
#             f.write(response.content)
#         print(f"Imagen guardada en {output_file}")
#     else:
#         print(f"Error al obtener la imagen: {response.status_code}")

# # Reemplaza los siguientes valores con la información de tu cámara IP
# ip_camera_url = "rtsp://192.168.1.54:554/Streaming/Channels/101"  #rtsp://admin:PA$$w0rd@192.168.1.54:554/Streaming/Channels/101
# username = "admin"
# password = "PA$$w0rd"

# # Genera un nombre de archivo con la fecha y hora actuales
# current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
# output_file = f"image_{current_time}.jpg"

# # Captura la imagen de la cámara IP
# capture_image_from_ip_camera(ip_camera_url, username, password, output_file)

# from mailfunciones import EmailSender

# correo=EmailSender("angel.roacho@gmail.com","yovuwtocegxorsmf","angel_m84@hotmail.com")
# correo.set_asunto("prueba clase correo")
# correo.adjuntar_imagen("test.png")
# correo.set_cuerpo("Este correo es prueba")

# correo.enviar()


# from configdb import configdb





# config=configdb()

# value=config.getConfig()

# print("Limit km:",value.get("limitkm","80"))
# print("mailto:",value.get("mailto","angel.roacho@gmail.com"))
# print("smtp Server:",value.get("smtpserver","127.0.0.1"))

# if (value["limitkm"]!=None):
#     print ("Limit km :",value["limitkm"])
# else:
#     print ("no existe limitkm")
    

# if (value["smtpserver"]!=None):
#     print ("smtpserver:",value["smtpserver"])
# else:
#     print ("no existe smtpserver")
    


# print(config.get("limitkm"))
# config.update("limitkm","80")
# print(config.all())
