import socket
import threading
import pyautogui
import os
import logging

logging.basicConfig(level=logging.INFO)

def client_handler(client_socket):
    try:
        while True:
            message_handler(client_socket.recv(1024).decode("utf-8").lower())
            client_socket.send('received'.encode("utf-8"))
    except Exception as e:
        logging.error(f"Error when handling client: {e}")
    finally:
        client_socket.close()
        logging.info("Connection closed")

def run_server(server_ip, port=8000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        try:
            server.bind((server_ip, port))
            server.listen()
            logging.info(f"Listening on {server_ip}:{port}")
            while True:
                client_socket, addr = server.accept()
                logging.info(f"Accepted connection from {addr[0]}:{addr[1]}")
                thread = threading.Thread(target=client_handler, args=(client_socket,))
                thread.start()
        except Exception as e:
            logging.error(f"Error: {e}")

def obtain_ip():
    ip = socket.gethostbyname(socket.gethostname())
    if ip.startswith("192.168.1"):
        return ip

def click(content):
    try:
        pyautogui.click(pyautogui.locateCenterOnScreen(getpicabsdir(content)),
                        button='left', clicks=1, interval=0.25)
    except Exception as e:
        logging.error(f"Error: {e}")

def repeatclickuntilreach():
    while True:
        try:
            pyautogui.locateOnScreen(getpicabsdir('confirm'))
        except:
            click('flag')
        else:
            break
    markcontent()
    click('confirm')

# def get pic abs dir:
def getpicabsdir(picname):
    # judge exist
    picpath = os.path.join(os.path.abspath('resource'), f'{picname}.png')
    if os.path.exists(picpath):
        return picpath
    else:
        logging.error(f"Error: {picpath} not exist")
        return False

def markcontent():
    import datetime
    pyautogui.typewrite(f'{datetime.datetime.now()}')

def message_handler(message):
    print(f"Received message: {message}")
    if message == "startrec":
        pyautogui.keyDown('f8')
    elif message == "stop":
        pyautogui.keyDown('f5')
    elif message == "test":
        import datetime
        print(datetime.datetime.now())
    elif message == "mark":
        click('flag')
        repeatclickuntilreach()

def main():
    ip = obtain_ip()
    if ip:
        run_server(ip)

if __name__ == "__main__":
    main()
