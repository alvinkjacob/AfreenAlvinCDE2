import socket

def Main():
    host = '127.0.0.1'
    port = 8888

    s = socket.socket()
    s.connect((host, port))

    message = input("You are now connected to the server. Please enter a message-> ")
    while message != 'q':
        s.send(message.encode('utf-8'))

        data = s.recv(1024).decode('utf-8')
        print("Message received from server: " +str(data))
        message = input("->")
    s.close()
    


if __name__ == '__main__':
    Main()
