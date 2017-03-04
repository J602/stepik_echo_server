# encoding: utf-8
import socket
import select

if __name__ == '__main__':
    IP = '0.0.0.0'
    PORT = 2222
    BUF_SIZE = 1024
    ERROR_COUNT = 10

    connection_list = []

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.bind((IP, PORT))
        s.listen(ERROR_COUNT)

        connection_list.append(s)

        while True:
            read_conn, write_conn, error_conn = select.select(connection_list,[],[])
            for conn in read_conn:
                if conn == s:
                    conn, adr = s.accept()
                    connection_list.append(conn)
                else:
                    print(adr)
                    data = conn.recv(BUF_SIZE)
                    if not data:
                        connection_list.remove(conn)
                        conn.close()
                        break
                    elif data.decode('utf-8').strip() == 'close':
                        connection_list.remove(conn)
                        conn.close()
                        break
                    else:
                        conn.send(data)
