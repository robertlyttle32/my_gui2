import socket
import sys
import time

#serverIP = 'host'
#serverPort = 5103

BUFFER_SIZE = 400
MESSAGE = "0x1"
TCP_IP = ""
TCP_PORT = 0

def tcp(TCP_IP, TCP_PORT):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        #s.close()
        def avc_connection():
                #bytes(string, 'utf-8')
                #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                #s.connect((TCP_IP, TCP_PORT))
                s.send(bytes(MESSAGE, 'utf-8'))
                data = s.recv(BUFFER_SIZE)
                #s.close()
                print ("received data:", data)


        try:
                while True:
                        avc_connection()

        except KeyboardInterrupt:
                s.close()
                print("connection broken")
                pass

