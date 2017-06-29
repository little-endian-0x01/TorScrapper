import socks
import socket

#Importing Stem libraries
from stem import Signal
from stem.control import Controller

#Initiating Connection
with Controller.from_port(port=9051) as controller:
    controller.authenticate("16:AE80E3930E42F7A3606823FA19CD0A3E721813EF8798ABFE86DB91DD09")
    controller.signal(Signal.NEWNYM)

# TOR SETUP GLOBAL Vars
SOCKS_PORT = 9050  # TOR proxy port that is default from torrc, change to whatever torrc is configured to
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", SOCKS_PORT)
socket.socket = socks.socksocket


# Perform DNS resolution through the socket
def getaddrinfo(*args):
    return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]


socket.getaddrinfo = getaddrinfo