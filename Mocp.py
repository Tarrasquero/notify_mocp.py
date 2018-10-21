
#! /usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import os
import re
import cv2


def descargar_img(cantante, disco, directorio):
    os.chdir(directorio)
    cantante = cantante.title()
    disco = disco.title()
    cantante = cantante.replace(' ', '_')
    cantante = cantante.replace('.', '_')
    disco = disco.replace(' ', '_')
    disco = disco.replace('...', '_')
    disco = disco.replace('.', '_')
    disco = disco.replace('?', '_')
    disco = disco.replace('[Ep]', '(Ep)')
    disco = disco.replace('_#', '_')
    disco = disco.replace(': ', '_')
    disco = disco.replace("_(Disc_1)", "")
    disco = disco.replace("_(Disc_2)", "")
    disco = re.sub(r"_(Cd[\d*])", "", disco)
    disco = re.sub(r"_(19[\d**])", "", disco)
    disco = re.sub(r"_(20[\d**])", "", disco)
    print(cantante, disco)
    link = ("http://images.coveralia.com/audio/%s/" +
           cantante + "-" + disco +
           "-Frontal.jpg") % cantante.lower()[0]
    #link = (url + cantante + "-" + disco + "-Frontal.jpg")
    try:
        imagen = requests.get(link).content
        nombreli = (directorio + cantante + "-" + disco + "-Frontal.jpg")
        print(link)
        with open(nombreli, 'wb') as handler:
            handler.write(imagen)
            path = os.walk(directorio)
            try:
                for root, dirs, files in path:
                    for fichero in files:
                        (nombreFichero, extension) = os.path.splitext(fichero)
                        if (extension == ".jpg"):
                            img = cv2.imread(nombreFichero + extension)
                            cv2.imwrite(nombreFichero +
                                        ".png", img,
                                        [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
                            os.remove(nombreFichero + ".jpg")
                            if os.stat(nombreFichero + ".png").st_size < 345:
                                os.remove(nombreFichero + ".png")
                        if (extension == ".jpeg"):
                            img = cv2.imread(nombreFichero + extension)
                            cv2.imwrite(nombreFichero +
                                        ".png", img,
                                        [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
                            os.remove(nombreFichero + ".jpeg")
                        else:
                            pass
            except OSError:
                pass
    except requests.exceptions.ConnectionError:
        pass
