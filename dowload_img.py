#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       download2.py
#       
#       Copyright 2013 Recursos Python - www.recursospython.com
#       
#
from urllib import urlretrieve, urlcleanup
import commands
import time
import string
def main():
    
    front = "Frontal.jpg"
    artista = commands.getoutput("mocp -Q %artist")
    criterio = artista[0]
    criterio = criterio.lower()
    album = commands.getoutput("mocp -Q %album")
    album = string.replace(string.replace(string.capwords(artista)+"-"+string.capwords(album)+"-","."," ")," ","_")
    album = album.replace("(CD 1)", "")
    album = album.replace("(CD 2)", "")
    album = album.replace("?", "_")
    print album     
    

    
    url = ("http://images.coveralia.com/audio/%s/%s%s" % (criterio, album, front))

    print url  
  
    filename = url[url.rfind("/") + 1:]

    print filename
    fil = commands.getoutput("mocp -Q %file")
    _directorio = fil.rfind('/')
    if _directorio != -1:
        _directorio = fil[:_directorio+1]
        urlretrieve(url, _directorio + filename)  # Descargar archivo
        # urlcleanup()  #  Limpiar cache
       
        print "%s descargado correctamente." % filename
if __name__ == "__main__":
    main()