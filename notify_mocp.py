#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# import string
# import dowload_img
import notify2
import sys
import os
import commands
import Image
import cgi
import re
from cPickle import dump, load
notify2.init("mocp")

def notify():
    file_dump = '/tmp/pymocp.id'
    try:
        artista = sys.argv[1]
        cancion = sys.argv[2]
        album = sys.argv[3]
        fil = sys.argv[4]
    except IndexError:
        artista = commands.getoutput('mocp -Q %artist')
        cancion = commands.getoutput('mocp -Q %song')
        album = commands.getoutput('mocp -Q %album')
        fil = commands.getoutput('mocp -Q %file')
    if not (artista and cancion and album):
        filename = os.path.splitext(fil)[0]
        filename = os.path.basename(filename)
        f = filename.rfind('-')
        artista = filename[:f]
        cancion = filename[f+1:]
        al = fil.split('/')
        album = al[4]    
    imge = '/home/jorge/.moc/scripts/icon-moc.png'
    filename = ("<b>Artista:  </b>" + "<b>%s</b>" % 
                cgi.escape(artista) + '\n' + "<b>Cancion:  </b>" + "<i>%s</i>" % 
                cgi.escape(cancion) + '\n' + "<b>Album:  </b>" + "<i>%s</i>" % 
                cgi.escape(album))
    sumario = ('')
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
        path = path.replace("CD 5/", "")
    lstDir = os.walk(path)
    for root, dirs, files in lstDir:
        for fichero in files:
            (nombreFichero, extension) = os.path.splitext(fichero)
            if (extension == ".jpeg" or extension == ".png" or extension == ".jpg"):
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
                    sys.exit(0)
	
def noimagen():
    file_dump = '/tmp/pymocp.id'
    n = None    
    try:
        n = load(open(file_dump, mode="rb"))
    except:
        n = notify2.Notification('')
    try:
        artista = sys.argv[1]
        cancion = sys.argv[2]
        album = sys.argv[3]
        fil = sys.argv[4]
    except IndexError:
        artista = commands.getoutput('mocp -Q %artist')
        cancion = commands.getoutput('mocp -Q %song')
        album = commands.getoutput('mocp -Q %album')
        fil = commands.getoutput('mocp -Q %file') 
    if not (artista and cancion and album):
        filename = os.path.splitext(fil)[0]
        filename = os.path.basename(filename)
        f = filename.rfind('-')
        artista = filename[:f]
        cancion = filename[f+1:]
        al = fil.split('/')
        album = al[4]    
    imge = '/home/jorge/.moc/scripts/icon-moc.png'
    filename = ("<b>Artista:  </b>" + "<b>%s</b>" % cgi.escape(artista) + '\n' + "<b>Cancion:  </b>" + "<i>%s</i>" % 
                cgi.escape(cancion) + '\n' + "<b>Album:  </b>" + "<i>%s</i>" % cgi.escape(album))
    sumario = ('')
    n.update(sumario, filename, imge)
    n.show()
    n = dump(n, open(file_dump, mode='wb'))
    sys.exit(0)

notify()
noimagen()
