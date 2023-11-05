import socket
import threading
import pyautogui

def handle_client(client_socket, addr):
    try:
        while True:
            # receive and print client messages
            request = client_socket.recv(1024).decode("utf-8")
            if request.lower() == "close":
                client_socket.send("closed".encode("utf-8"))
                break
            elif request.lower() == "mark":
                mark()
            elif request.lower() == "start":
                startrec()
            elif request.lower() == "stop":
                stoprec()
            else:
                cilck(request)
            print(f"Received: {request}")
            # convert and send accept response to the client
            response = "accepted"
            client_socket.send(response.encode("utf-8"))
    except Exception as e:
        print(f"Error when hanlding client: {e}")
    finally:
        client_socket.close()
        print(f"Connection to client ({addr[0]}:{addr[1]}) closed")


def run_server():
    server_ip = "127.0.0.1"  # server hostname or IP address
    port = 8000  # server port number
    # create a socket object
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # bind the socket to the host and port
        server.bind((server_ip, port))
        # listen for incoming connections
        server.listen()
        print(f"Listening on {server_ip}:{port}")

        while True:
            # accept a client connection
            client_socket, addr = server.accept()
            print(f"Accepted connection from {addr[0]}:{addr[1]}")
            # start a new thread to handle the client
            thread = threading.Thread(target=handle_client, args=(client_socket, addr,))
            thread.start()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.close()


def mark():
    print("marked")
    # press f12
    pyautogui.keyDown('f12')

def startrec():
    print("startrec")
    # press f5
    pyautogui.keyDown('f8')

def stoprec():
    print("stoprec")
    # press f6
    pyautogui.keyDown('f5')

def cilck(content):
    iconpath = f'resource/{content}.png'
    pyautogui.click(pyautogui.locateCenterOnScreen(iconpath),
                    button='left', clicks=1, interval=0.25)

run_server()