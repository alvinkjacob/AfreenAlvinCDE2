import socket

def Main():
    host = '0.0.0.0'
    port = 8888

    s = socket.socket()
    s.bind((host, port))

    s.listen(5)
    print("Listening on" +str(host)+":" +str(port))

    c, addr = s.accept()
    print("Connection from: " +str(addr))
    while True:
        data = c.recv(1024).decode('utf-8')
        if not data:
            break
        print("data received: "+str(data))
        c.send(data.encode('utf-8'))
    print("Connection closed: " +str(addr))
    c.close()

        #c.close()
        #server_sock.close()

    

if __name__ == '__main__':
    Main()
