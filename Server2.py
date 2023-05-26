import socket
import threading
from threading import Thread         

DATA_FILE = "employee_data.xml"
BACKUP_INTERVAL = 5  # Backup interval in minutes
#host = '127.0.0.1'    # listen on the local host only
#host = 'example.org'  # listen on IP that resolves to this host name
host = ''              # leave blank to listen on any IP or interface
port = 12346         # above 1023 are non-privileged, 1-65535
  
s = socket.socket()                 # open a socket
s.bind((host, port))                # bind to a host and port
s.listen(5)                         # start listening 
                                    # optional (in Python 3.5) backlog pending connections

print( "Listening on " + str(host) + ":" + str(port))


def handle_connection(conn, addr):
    while True:                     # loop to recv data
        data = conn.recv(1024)      # recv data
        if not data:                # no more data to recv (socket closed!!)
            break                   # break loop
        print("recv: " + str(data))
        conn.sendall(data)          # send data back

    print("Connection closed: " + str(addr))
    conn.close()                    # close connection


while True:                               # loop for connections ( each in a parallel thread )
    conn, addr = s.accept()               # block and wait for incoming connections
    print("Connection from " +  str(addr))
    t = Thread(target=handle_connection, args=(conn,addr))  # create a new thread
    t.start()                             # start it 
    num_client = threading.activeCount() - 1
    print(num_client)
    if num_client>=3:
        print("busy")


s.close()