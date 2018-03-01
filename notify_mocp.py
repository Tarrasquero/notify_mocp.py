#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import subprocess
import commands
import os
import Image
# Opteniendo informacion artista titulo y album
artista = sys.argv[1]
cancion = sys.argv[2]
album = sys.argv[3]

# Variables redimensionado
width = 100
height = 100

# Opteniendo path coverart
fil = sys.argv[4]

# Recortando path
path = fil.rfind('/')
if path != -1:
    path = fil[:path+1] 

# Lista con todos los ficheros del directorio:
lstDir = os.walk(path)
 
# Crea una lista de los ficheros jpg/png/jpeg que existen en el directorio y los incluye a la lista.

for root, dirs, files in lstDir:
    for fichero in files:
        (nombreFichero, extension) = os.path.splitext(fichero)
        if (extension == ".jpg" or extension == ".png" or extension == ".jpeg"):
            imagen = '{0}{1}{2}'.format(path, nombreFichero, extension)
            I = Image.open(imagen)
            if (I.size != (100, 100)):
                img = I.resize((width, height), Image.ANTIALIAS)
                img.save(path + nombreFichero + extension)
            subprocess.call(['notify-send', "--icon=%s" % (imagen), artista + ':' '\n' + cancion + '\n' + album])
