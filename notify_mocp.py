#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# -*- coding: ascii -*-
import subprocess
import sys
import commands
import os
#import Tkinter
import Image
import PIL
"""import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify
Notify.init("mocp")
Notify.Notification.new(artista + ':' '\n' + cancion).show()
APPLICATION_DIR = sys.path[0] + "/"
coverImage = APPLICATION_DIR + 'icon-moc.png'
"""
#imagenAnchuraMaxima=100
#imagenAlturaMaxima=100
artista = commands.getoutput("mocp -Q %artist")
cancion = commands.getoutput("mocp -Q %song")

#Opteniendo path coverart
fil = commands.getoutput("mocp -Q %file")

#Variable para la ruta al directorio
"""path = fil.rstrip(' &\'\"!#,;:0123456789{\}\(\)\[\]\.äëaAbBcCdDeEfFgGhHiIJjKLMNOPQRSTUVWXYZklmnopqrstuvwxyz-_')
print (path)
"""
path = fil.rfind('/')
if path != -1:
    path = fil[:path+1] 
else: 
    path = fil

#Lista vacia para incluir los ficheros
lstFiles = []
 
#Lista con todos los ficheros del directorio:
lstDir = os.walk(path)   #os.walk()Lista directorios y ficheros
 
#Crea una lista de los ficheros jpg/png/jpeg que existen en el directorio y los incluye a la lista.

for root, dirs, files in lstDir:
    for fichero in files:
        (nombreFichero, extension) = os.path.splitext(fichero)
        if(extension == ".jpg" or extension == ".png" or extension == ".jpeg"):
            lstFiles.append(nombreFichero+extension)
            img = '{0}{1}{2}'.format(path, nombreFichero, extension)
            
            """img = imagen.resize((100, 100))
            img.show()
            img = Image.open(imagen)
            img = imagen.thumbnail((imagenAnchuraMaxima, imagenAlturaMaxima), Image.ANTIALIAS)
            tkimage = ImageTk.PhotoImage(img)
            
            print imagen
            """ 
subprocess.call(['notify-send', "--icon=%s" % (img), {0} + ':' '\n' + {1}])           