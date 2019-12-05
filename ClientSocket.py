class my_class(object):
    pass

#!/usr/bin/env
# 
#
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import sys
import csv
from io import StringIO

# Set up chat client

HOST = "192.168.1.45"


PORT = 1234


BUFSIZ = 1024
ADDR = (HOST, PORT)
NAME = ''

# Create a TCP client socket
client_socket = socket(AF_INET, SOCK_STREAM)
# Connect to the chat server
client_socket.connect(ADDR)
client_socket.send("user,0".encode("utf8"))

xList = []
yList = []


def dataWrite(str):
    f = open("DataStore.txt", "w")
    f.write(str+'\n')
    f.close()

def receive(csocket):
    #clear text file
    dataWrite("")
    while True:
        try:
            msg = csocket.recv(1024).decode("utf8")
           # print(msg)
            dataWrite(msg)
            
          
        
        except OSError:
            # Possibly client has left the chat.
            break



# Handles sending of messages
def send():  
    while True:
        try:
            # Send message to chat server
            msg = input('')
            client_socket.send(msg.encode("utf8"))
        except OSError:
            # Possibly client has left the chat.
            break

def main():
    

    # Start the receiving thread
    receive_thread = Thread(target=receive(client_socket))
    receive_thread.start()

    # Start the sending thread
    send_thread = Thread(target=send)
    send_thread.start()

    # Wait for child threads to stop
    receive_thread.join()
    send_thread.join()

if __name__ == "__main__":
    main()



serverName = '192.168.1.45'

