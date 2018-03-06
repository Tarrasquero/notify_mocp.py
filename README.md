# Mocp-Notify.py

![Mocp_notify en acción](https://github.com/Tarrasquero/notify_mocp.py/blob/master/Arreglo.png)


![Mocp_notify en acción](https://github.com/Tarrasquero/notify_mocp.py/blob/master/Screenshot-py.png)



## Novedades:
- `Redimensionado` de imagenes a 100x100

## Configuración para notificación de mocp:
- Extraer `/usr/share/doc/moc/example/config.example.gz` en `~/.moc` con el nombre `config`.
- Mover scripts: `notify_mocp.py` a `~/.moc/scripts`.
`mkdir $HOME/.moc/scripts ; mv notify_mocp.py $HOME/.moc/scripts`
- Otorgar permisos de ejecución:  `chmod +x notify_mocp.py`
- Buscar la linea: `#OnSongChange=` que debería quedar parecida a esta: `OnSongChange= "$HOME/scripts/notify_mocp.py %a %t %r %f"` 
