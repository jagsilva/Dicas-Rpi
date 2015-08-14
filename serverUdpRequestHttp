# Servidor
# Recebe dados udp na porta 12000
# cria uma thread e envia os dados por http para um site

import socket
from thread import *
import time
import requests

def tred(data,addr):
        print data
        partes = data.split(";")
        payload = {'datahora':partes[0],'lat':partes[1],'lng':partes[2],'vel':partes[3],'ign':partes[4]}
        r = requests.get('http://www.jagsilva.pton.org/ulex.php',params=payload)
        print(r.url)

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(("", 12000))

while 1:
        data, addr = s.recvfrom(1024)

        print data.strip(), addr
        start_new_thread(tred,(data,addr))
