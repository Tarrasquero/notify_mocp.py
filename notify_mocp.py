#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import dowload_img
import notify2
import sys
import os
import commands
import Image
import cgi
from cPickle import dump, load
notify2.init("mocp")

file_dump = '/tmp/pymocp.id'

artista = commands.getoutput("mocp -Q %artist")  # sys.argv[1]
cancion = commands.getoutput("mocp -Q %song")  #  sys.argv[2]
album = commands.getoutput("mocp -Q %album")  # sys.argv[3]
fil = commands.getoutput("mocp -Q %file")  # sys.argv[4]
img = ''

text = ("<b>Artista:  </b>" + "<b>%s</b>" % cgi.escape(artista) + '\n' + "<b>Cancion:  </b>" + "<i>%s</i>" % 
        cgi.escape(cancion) + '\n' + "<b>Album:  </b>" + "<i>%s</i>" % cgi.escape(album))
sumario = ('')
if not (artista and cancion and album):
    filename = os.path.splitext(fil)[0]
    filename = os.path.basename(filename)
    artista = filename.rfind('-')
    if artista != -1:
        artista = filename[:artista]
    cancion = filename.find('-')
    if cancion != -1:
    	cancion = filename[cancion:]
    	cancion = cancion.strip('- ')
    filename = os.path.splitext(fil)[0]
    filename = os.path.dirname(filename)
    album = filename.rfind('/')
    if album != -1:
    	album = filename[album:]
    	album = album.strip('/')
n = None    
try:
    n = load(open(file_dump, mode="rb"))
except:
    n = notify2.Notification('')

width = 100
height = 100

path = fil.rfind('/')
if path != -1:
    path = fil[:path+1] 
lstDir = os.walk(path)

for root, dirs, files in lstDir:
    for fichero in files:
        (nombreFichero, extension) = os.path.splitext(fichero)
        if (extension == ".jpg" or extension == ".png" or extension == ".jpeg"):
            imagen = '{0}{1}{2}'.format(path, nombreFichero, extension)
            I = Image.open(imagen)
            if (I.size != (100, 100)):
                img = I.resize((width, height), Image.ANTIALIAS)
                nombreFichero = (nombreFichero + '.Thumbnail')
                img.save(path + nombreFichero + extension)
                imagen = '{0}{1}{2}'.format(path, nombreFichero, extension)
                n.update(sumario, text, imagen)
                n.show()
                n = dump(n, open(file_dump, mode='wb'))
