#!/bin/bash

# Ruta del directorio donde deseas buscar los archivos antiguos
directorio="/home/roacho/fotomultasinstall/fotomultas/logs"

# Ejecuta el comando find para encontrar archivos con más de 30 días de antigüedad
# y utiliza el flag -delete para eliminarlos.
find "$directorio" -type f -mtime +30 -delete

echo "Archivos antiguos borrados."