# Mocp-Notify.py python 2.7


[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/x6CiPKTay8o/0.jpg)](https://www.youtube.com/watch?v=x6CiPKTay8o)


## Dependencias:
- Instale dependencias: `sudo pip install --upgrade -r requeriments.txt`


## Novedades:
- Agregado `modulo de descarga para carátulas`.
- `Reemplazo` de la notificación.
- `Redimensionado` de imagenes a 100x100 a copia en miniatura.

## Configuración para notificación de mocp:
- Extraer `/usr/share/doc/moc/example/config.example.gz` en `~/.moc` con el nombre `config`.
- Mover script: `notify_mocp.py` con modulo `Mocp.py` y `icon-moc.png` a `~/.moc/scripts`:
`mkdir $HOME/.moc/scripts ; mv notify_mocp.py Mocp.py icon-moc.png $HOME/.moc/scripts`
- Otorgar permisos de ejecución:  `chmod +x notify_mocp.py`
- En el archibo `config` buscar la linea: `#OnSongChange=` que debería quedar parecida a esta: `OnSongChange= "$HOME/.moc/scripts/notify_mocp.py %a %t %r %f"` 
