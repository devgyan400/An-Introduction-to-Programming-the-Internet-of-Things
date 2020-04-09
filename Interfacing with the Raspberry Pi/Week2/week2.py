import socket
import sys

if __name__ == '__main__':
    ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = "192.168.137.155"
    port = 1234

    try:
        ms.bind((ip, port))
    except socket.error:
        print('Failed to connect')
        sys.exit()

    ms.listen(5)

    while True:
        connection, address = ms.accept()
        data = connection.recv(1000)
        if data:
            print('Got a request!')
        print(data)
        if not data:
            break
    connection.close()
    ms.close()
