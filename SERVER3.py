import socket
import threading
from threading import Thread
import webbrowser



def handle_connection(conn, addr):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            print("recv: " + str(data))
            with open("employee_data.html", "a", newline=None) as f:
                f.write('\n' + data.decode() + '\n')

            webbrowser.open("employee_data.html")
            conn.sendall(data)
        except Exception as e:
            print(f"An error occurred whilst receiving data from client {addr}: {str(e)}")

    print("Connection closed: " + str(addr))
    conn.close()


def start_server(port):
    s = socket.socket()
    host = ''
    s.bind((host, port))
    s.listen(5)
    print("Listening on " + str(host) + ":" + str(port))

    while True:
        conn, addr = s.accept()
        # count+=1
        # print(count)                          
        # if count>=2:
        #     server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #     server_sock.connect(("localhost", 12357))
        #     server_sock.sendall(conn.recv(1024))
        #     print("forwarding...")
        print("Connection from " + str(addr)+ "on"+ str(host) + ":" + str(port)) 
        t = Thread(target=handle_connection, args=(conn, addr))
        t.start()

    s.close()


def main():
    ports = [12346, 8888]  # Add the ports you want to host the server on

    threads = []
    for port in ports:
        t = threading.Thread(target=start_server, args=(port,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


if __name__ == "__main__":
    main()