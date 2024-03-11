import socket
import time

def send_signal(host = '192.168.0.155', port = 12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            s.sendall(b'Hello, server')
            data = s.recv(1024)
            print("Получен ответ от сервера")
            time.sleep(1) # Задержка перед отправкой следующего сигнала

if __name__ == '__main__':
    send_signal()
