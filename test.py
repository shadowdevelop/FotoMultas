from mailfunciones import EmailSender

correo=EmailSender("angel.roacho@gmail.com","yovuwtocegxorsmf","angel_m84@hotmail.com")
correo.set_asunto("prueba clase correo")
correo.adjuntar_imagen("test.png")
correo.set_cuerpo("Este correo es prueba")

correo.enviar()


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
