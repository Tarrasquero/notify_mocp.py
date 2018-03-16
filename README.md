# Mocp-Notify.py python 2.7


[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/x6CiPKTay8o/0.jpg)](https://www.youtube.com/watch?v=x6CiPKTay8o)


## Dependencias:
- python-notify2


## Novedades:
- Modulo de `descargas` Coveralia agregado. (BETA)
- `Reemplazo` de la notificación.
- `Redimensionado` de imagenes a 100x100 a copia en miniatura.

## Configuración para notificación de mocp:
- Extraer `/usr/share/doc/moc/example/config.example.gz` en `~/.moc` con el nombre `config`.
- Mover script: `notify_mocp.py` a `~/.moc/scripts`:
`mkdir $HOME/.moc/scripts ; mv notify_mocp.py $HOME/.moc/scripts`
- Otorgar permisos de ejecución:  `chmod +x notify_mocp.py`
- Buscar la linea: `#OnSongChange=` que debería quedar parecida a esta: `OnSongChange= "$HOME/.moc/scripts/notify_mocp.py %a %t %r %f"` 

## Bugs:
- El directorio del album debería contener `al menos una imagen y solo una para mostrar en la notificacion`.
