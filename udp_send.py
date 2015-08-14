import socket

mensagem = "JAIME SILVA"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(mensagem, ("192.168.1.128",33336))
