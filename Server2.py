import socket

def Main():
    host = '0.0.0.0'
    port = 8080

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))

    s.listen(5)

    while True:
        c, addr = s.accept()
        print("Connection from: " +str(addr))

        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_sock.connect(("localhost", 8888))

        server_sock.sendall(c.recv(1024))
        print("forwarding...")

        #c.close()
        #server_sock.close()

    

if __name__ == '__main__':
    Main()
