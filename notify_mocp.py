#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import string
import notify2
import sys
import os
import commands
import Image
import cgi
from cPickle import dump, load, dumps, loads
notify2.init("mocp")

file_dump = '/tmp/pymocp.id'

artista = commands.getoutput("mocp -Q %artist")  # sys.argv[1]
cancion = commands.getoutput("mocp -Q %song")  #  sys.argv[2]
album = commands.getoutput("mocp -Q %album")  # sys.argv[3]
fil = commands.getoutput("mocp -Q %file")  # sys.argv[4]
imge = '/home/jorge/.moc/scripts/icon-moc.png'

filename = ("<b>Artista:  </b>" + "<b>%s</b>" % cgi.escape(artista) + '\n' + "<b>Cancion:  </b>" + "<i>%s</i>" % 
        cgi.escape(cancion) + '\n' + "<b>Album:  </b>" + "<i>%s</i>" % cgi.escape(album))
sumario = ('')
if not (artista and cancion):
    filename = os.path.splitext(fil)[0]
    filename = os.path.basename(filename)
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
    path = path.replace("CD1/", "")
    path = path.replace("CD2/", "")
    path = path.replace("CD3/", "")
    path = path.replace("CD4/", "")
    path = path.replace("CD5/", "")
    path = path.replace("CD 1/", "")
    path = path.replace("CD 2/", "")
    path = path.replace("CD 3/", "")
    path = path.replace("CD 4/", "")
    path = path.replace("CD 6/", "")
lstDir = os.walk(path)
def noimagen():
    file_dump = '/tmp/pymocp.id'
    n = None    
    try:
        n = load(open(file_dump, mode="rb"))
    except:
        n = notify2.Notification('')
    artista = commands.getoutput("mocp -Q %artist")  # sys.argv[1]
    cancion = commands.getoutput("mocp -Q %song")  #  sys.argv[2]
    album = commands.getoutput("mocp -Q %album")  # sys.argv[3]
    fil = commands.getoutput("mocp -Q %file")  # sys.argv[4]
    imge = '/home/user/.moc/scripts/icon-moc.png'
    filename = ("<b>Artista:  </b>" + "<b>%s</b>" % cgi.escape(artista) + '\n' + "<b>Cancion:  </b>" + "<i>%s</i>" % 
                cgi.escape(cancion) + '\n' + "<b>Album:  </b>" + "<i>%s</i>" % cgi.escape(album))
    sumario = ('')
    n.update(sumario, filename, imge)
    n.show()
    n = dump(n, open(file_dump, mode='wb'))
    sys.exit()

for root, dirs, files in lstDir:
    for fichero in files:
        (nombreFichero, extension) = os.path.splitext(fichero)
        if (extension == ".jpg" or extension == ".png" or extension == ".jpeg"):
            _imagen = '{0}{1}{2}'.format(path, nombreFichero, extension)           	
            _I = Image.open(_imagen)
            if (_I.size != (100, 100)):
                img = _I.resize((width, height), Image.ANTIALIAS)
                nombreFichero = (nombreFichero + '.Thumbnail')
                img.save(path + nombreFichero + extension)
                _imagen = '{0}{1}{2}'.format(path, nombreFichero, extension)
                n.update(sumario, filename, _imagen)
                n.show()
                n = dump(n, open(file_dump, mode='wb'))
                sys.exit()
noimagen()
