import socket
import threading
from threading import Thread         

#count = 0
DATA_FILE = "employee_data.xml"
BACKUP_INTERVAL = 5  # Backup interval in minutes
#host = '127.0.0.1'    # listen on the local host only
#host = 'example.org'  # listen on IP that resolves to this host name
host = '127.0.0.1'              # leave blank to listen on any IP or interface
ports = [8888, 12346, 12347]          # above 1023 are non-privileged, 1-65535

for port in ports:
    s = socket.socket()                 # open a socket
    s.bind((host, port))                # bind to a host and port
    s.listen(2)                         # start listening 
                                        # optional (in Python 3.5) backlog pending connections

    print( "Listening on " + str(host) + ":" + str(port))


def handle_connection(conn, addr):
    while True:                     # loop to recv data
        data = conn.recv(1024)      # recv data
        if not data:                # no more data to recv (socket closed!!)
            break                   # break loop
        print("recv: " + str(data))
        with open("employee_data.html", "a") as f:
                        f.write(data.decode())

                    webbrowser.open("employee_data.html")
        conn.sendall(data)          # send data back

    print("Connection closed: " + str(addr))
    conn.close()                    # close connection


while True:                               # loop for connections ( each in a parallel thread )
    conn, addr = s.accept()               
    print("Connection from " +  str(addr)) 
    t = Thread(target=handle_connection, args=(conn,addr))  # create a new thread
    numclient = threading.active_count()
    print(numclient)
    t.start()# start it   
     


s.close()