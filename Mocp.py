#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import os


def descargar_img(cantante, disco, directorio):
    cantante = cantante.title()
    disco = disco.title()
    cantante = cantante.replace(' ', '_')
    cantante = cantante.replace('.', '_')
    disco = disco.replace(' ', '_')
    disco = disco.replace('.', '_')

    url = "http://images.coveralia.com/audio/%s/" % cantante.lower()[0]
    link = (url + cantante + "-" + disco + "-Frontal.jpg")
    nombre_local_imagen = (directorio + disco + ".jpg")
    imagen = requests.get(link).content
    with open(nombre_local_imagen, 'wb') as handler:
        handler.write(imagen)
    if os.stat(nombre_local_imagen).st_size <= 345:
        os.remove(nombre_local_imagen)
