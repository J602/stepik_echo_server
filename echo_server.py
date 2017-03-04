# encoding: utf-8
import socket

if __name__=='__main__':
    IP = '0.0.0.0'
    PORT = 2222
    BUF_SIZE = 1024
    ERROR_COUNT = 10

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.bind((IP, PORT))
        s.listen(ERROR_COUNT)
        conn, adr = s.accept()
        with conn:
            while True:
                data = conn.recv(BUF_SIZE)
                if not data:
                    break
                elif data.decode('utf-8').strip() == 'close':
                    break
                else:
                    conn.send(data)

