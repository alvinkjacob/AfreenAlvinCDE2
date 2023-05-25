import socket

def Main():
    host = '0.0.0.0'
    port = 8888

    s = socket.socket()
    s.bind((host, port))

    s.listen(5)
    print ("Server is runnning ... machines can connect on port 8888")
    c, addr = s.accept()
    print("Connection from: " +str(addr))

    while True:
        data = c.recv(1024).decode('utf-8')
        if not data:
            break
        print ("the connected user says: "+ data)
        data = data.upper()
        print ("Sending back in upper case!: " +data)
        c.send(data.encode('utf-8'))
    c.close()
    

if __name__ == '__main__':
    Main()
