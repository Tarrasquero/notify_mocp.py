#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Image
import cgi
import commands
import notify2
import os
import re
import sys

from cPickle import dump
from cPickle import load
notify2.init("mocp")
__autor__ = "Jorge"


class Cuerpo():
    def Load(self):
        self.file_dump = '/tmp/pymocp.id'
        self.n = None
        try:
            self.n = load(open(self.file_dump, mode="rb"))
        except IOError:
            self.n = notify2.Notification('')

    def Dump(self):
        self.n.update(self.sumario, self.filename, self.imagen)
        self.n.show()
        self.n = dump(self.n, open(self.file_dump, mode='wb'))


class Notify(Cuerpo):
    def Imagen(self):
        try:
            self.artista = sys.argv[1]
            self.cancion = sys.argv[2]
            self.album = sys.argv[3]
            self.fil = sys.argv[4]
        except IndexError:
            self.artista = commands.getoutput('mocp -Q %artist')
            self.cancion = commands.getoutput('mocp -Q %song')
            self.album = commands.getoutput('mocp -Q %album')
            self.fil = commands.getoutput('mocp -Q %file')
        if not self.cancion:
            filename = os.path.splitext(self.fil)[0]
            filename = os.path.basename(filename)
            f = filename.rfind('-')
            self.artista = filename[:f]
            self.cancion = filename[f + 1:]
            al = self.fil.split('/')
            self.album = al[4]
        self.sumario = ''
        self.width = 100
        self.height = 100
        self.filename = ("<b>Artista:  </b>" + "<b>%s</b>" %
                         cgi.escape(self.artista) + '\n' +
                         "<b>Cancion:  </b>" + "<i>%s</i>" %
                         cgi.escape(self.cancion) + '\n' +
                         "<b>Album:  </b>" + "<i>%s</i>" %
                         cgi.escape(self.album))
        self.ig = (".jpg", ".png", ".jpeg")
        _path = self.fil.rfind('/')
        if _path != -1:
            _path = self.fil[:_path + 1]
            _path = re.sub(r'CD[\d*]/', '', _path)
            _path = re.sub(r'CD [\d*]/', '', _path)
        lstDir = os.walk(_path)
        for root, dirs, files in lstDir:
            for fichero in files:
                (nombreFichero, extension) = os.path.splitext(fichero)
                if extension in self.ig:
                    self.imagen = '{0}{1}{2}'.format(
                                  _path, nombreFichero, extension)
                    i = Image.open(self.imagen)
                    if (i.size != (100, 100)):
                        img = i.resize((self.width,
                                        self.height), Image.ANTIALIAS)
                        nombreFichero = (nombreFichero + '.Thumbnail')
                        img.save(_path + nombreFichero + extension)
                        self.imagen = '{0}{1}{2}'.format(
                            _path, nombreFichero, extension)
                        MiNotify.Dump()
                        sys.exit(0)
        self.imagen = os.path.abspath(os.path.join(
            __file__, os.pardir, 'icon-moc.png'))


MiNotify = Notify()
MiNotify.Load()
MiNotify.Imagen()
MiNotify.Dump()
