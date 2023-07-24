#!/bin/bash

# Palabra que quieres buscar en los nombres de los procesos
palabra="main.py"

# Buscar el proceso
pgrep -f $palabra > /dev/null

# Comprobar si el proceso está en ejecución
if [ $? -ne 0 ]; then
    echo "$palabra no se está ejecutando, iniciando el proceso..."
    # Aquí debes colocar el comando completo para ejecutar tu script python
    nohup sudo python /home/roacho/fotomultasinstall/fotomultas/main.py &
else
    echo "$palabra ya se está ejecutando."
fi