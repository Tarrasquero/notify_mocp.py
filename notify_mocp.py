#!/usr/bin/env python
# -*- coding: utf-8 -*-
import notify2
import os
import Image
from commands import getoutput
from sys import argv, exit
from re import sub
from cgi import escape
from cPickle import dump
from cPickle import load
import Mocp

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
        objeto = os.path.abspath(os.path.join(
            __file__, os.pardir, 'icon-moc.png'))
        try:
            self.n.update(self.sumario, self.filename, self.imagen_t)
            self.n.show()
            self.n = dump(self.n, open(self.file_dump, mode='wb'))
            exit(0)
        except AttributeError:
            self.n.update(self.sumario, self.filename, objeto)
            self.n.show()
            self.n = dump(self.n, open(self.file_dump, mode='wb'))
            exit(0)


class Notify(Cuerpo):
    def Imagen(self):
        try:
            self.artista = argv[1]
            self.cancion = argv[2]
            self.album = argv[3]
            self.fil = argv[4]
        except IndexError:
            self.artista = getoutput('mocp -Q %artist')
            self.cancion = getoutput('mocp -Q %song')
            self.album = getoutput('mocp -Q %album')
            self.fil = getoutput('mocp -Q %file')
        if not self.cancion:
            filename = os.path.splitext(self.fil)[0]
            filename = os.path.basename(filename)
            f = filename.split('-')
            self.artista = f[0]
            self.cancion = f[1]
            al = self.fil.split('/')
            self.album = al[4]
        self.sumario = ''
        self.width = 100
        self.height = 100
        self.filename = ("<b>Artista:  </b>" + "<b>%s</b>" %
                         escape(self.artista) + '\n' +
                         "<b>Cancion:  </b>" + "<i>%s</i>" %
                         escape(self.cancion) + '\n' +
                         "<b>Album:  </b>" + "<i>%s</i>" %
                         escape(self.album))
        _path = self.fil.rfind('/')
        if _path != -1:
            _path = self.fil[:_path + 1]
            _path = sub(r"CD[\d*]/", "", _path)
            _path = sub(r"CD [\d*]/", "", _path)
            _path = sub(r"Disc [\d*]/", "", _path)
            _path = sub(r"Disc[\d*]/", "", _path)
        Mocp.descargar_img(self.artista, self.album, _path)
        lstDir = os.walk(_path)
        for root, dirs, files in lstDir:
            for fichero in files:
                (nombreFichero, extension) = os.path.splitext(fichero)
                try:
                    if (extension == ".png"):
                        self.imagen = '{0}{1}{2}'.format(
                            _path, nombreFichero, extension)
                        self.img = Image.open(self.imagen)
                        if (self.img.size == (100, 100)):
                            self.imagen_t = '{0}{1}{2}'.format(
                                _path, nombreFichero, extension)
                            MiNotify.Dump()
                            exit(0)
                        elif (self.img.size > (100, 100)):
                            self.imagen = '{0}{1}{2}'.format(
                                _path, nombreFichero, extension)
                            self.img = Image.open(self.imagen)
                            nombreFichero = (nombreFichero + '.Thumbnail')
                            self.img = self.img.resize((
                                self.width, self.height), Image.ANTIALIAS)
                            self.img.save(_path + nombreFichero + extension)
                            self.imagen_t = (_path + nombreFichero + extension)
                            MiNotify.Dump()
                            exit(0)
                except IOError:
                    self.imagen_t = os.path.abspath(os.path.join(
                        __file__, os.pardir, 'icon-moc.png'))
                    MiNotify.Dump()
                    exit(0)


if __name__ == "__main__":
    MiNotify = Notify()
    MiNotify.Load()
    MiNotify.Imagen()
    MiNotify.Dump()
