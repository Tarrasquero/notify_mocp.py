#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import notify2
import sys
import os
from cPickle import dump, load
notify2.init("mocp")
# Opteniendo informacion artista titulo y album
file_dump = '/tmp/pymocp.id'
artista = sys.argv[1]
cancion = sys.argv[2]
album = sys.argv[3]
fil = sys.argv[4]
n = None    
try:
    n = load(open(file_dump, mode="rb"))
except:
    n = notify2.Notification('')
    
    

# Variables redimensionado
width = 100
height = 100

# Recortando path
path = fil.rfind('/')
if path != -1:
    path = fil[:path+1] 
    import Image
    import cgi
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
            text = ("<b>Artista:  </b>" + "<b>%s</b>" % cgi.escape(artista) + '\n' + "<b>Cancion:  </b>" + "<i>%s</i>" % 
                    cgi.escape(cancion) + '\n' + "<b>Album:  </b>" + "<i>%s</i>" % cgi.escape(album))
            sumario = ('')            
            n.update(sumario, text, imagen)
            n.show()
            n = dump(n, open(file_dump, mode='wb'))
