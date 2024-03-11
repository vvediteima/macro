import socket

def create_server(host = '0.0.0.0', port = 12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Сервер запущен и прослушивает {host}:{port}")

        conn, addr = s.accept()
        with conn:
            print(f"Подключен клиент {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print("Получен сигнал от клиента")
                conn.sendall(b'Signal received')
                
if __name__ == '__main__':
    create_server()
