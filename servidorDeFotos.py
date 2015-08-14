# SERVIDOR A ESCUTA NA PORTA 10000, ACEITA LIGACOES, REGISTA A DATA,
# TIRA UMA FOTO, A DATA E O NOME DA FOTO E ENVIA ESSE NOME PARA O CLIENTE
# !/usr/bin/env python

import socket
import time
import picamera
import datetime

host = ''
port = 10000
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)

while True:
    csock, caddr = sock.accept()
    print "Connection from: " + `caddr`
    req = csock.recv(1024)
    print req
    data = datetime.datetime.now().strftime("%y%m%d%H%M%S")
    file = "/var/www/fotos/pic" + data + ".jpg"
    with picamera.PiCamera() as camera:
        camera.start_preview()
        time.sleep(2)
        camera.capture(file)
        camera.stop_preview()
    print data
    csock.send(data)
    csock.close()
